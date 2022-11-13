import json
from itertools import cycle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from sklearn.metrics import PrecisionRecallDisplay

def get_metrics(USE_INTERPOLATION, QRELS_FILE, QUERY_URL, QUERY_URL_WEIGHT):

    # Read qrels to extract relevant documents
    relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))

    # Get query results from Solr instance
    results_normal = requests.get(QUERY_URL).json()['response']['docs']

    # get the results with weights
    results_weight = requests.get(QUERY_URL_WEIGHT).json()['response']['docs']

    # get the results with no schema
    results_no_schema = json.load(open('noSchema.json', encoding="utf8"))['response']['docs']

    all_results = [results_normal, results_weight, results_no_schema]

    _, ax = plt.subplots(figsize=(5, 5))

    colors = cycle(["red", "green",  "blue"])

    i = 0
    for results, color in zip(all_results, colors):

        # In a second step, we calculate some common evaluation metrics that can be used to compare systems and to assess their performance.
        # METRICS TABLE
        # Define custom decorator to automatically calculate metric based on key
        metrics = {}
        def metric(f): return metrics.setdefault(f.__name__, f)

        @metric
        def ap(results, relevant):
            """Average Precision"""

            # we need to do this for because the results with no schema are different
            relevant_index = []
            index = 0
            for res in results:
                if (i != 2 and res['name'] in relevant) or (i == 2 and res['name'][0] in relevant):
                    relevant_index.append(index)
                index = index + 1

            if len(relevant_index) == 0:
                return 0

            precision_values = [
                len([
                    doc
                    for doc in results[:idx]
                    if (i != 2 and doc['name'] in relevant) or (i == 2 and doc['name'][0] in relevant)
                ]) / idx
                for idx in range(1, len(results) + 1)
            ]

            precision_sum = 0
            for idx in relevant_index:
                precision_sum = precision_sum + precision_values[idx]
            
            return precision_sum / len(relevant_index)

        @metric
        def p10(results, relevant, n=10):
            if len(results) == 0:
                return 0

            """Precision at N"""
            return len([
                doc 
                for doc in results[:n] 
                if (i != 2 and doc['name'] in relevant) or (i == 2 and doc['name'][0] in relevant)
            ])/len(results)

        @metric
        def r10(results, relevant, n=10):
            """Recall at N"""
            return len([
                doc 
                for doc in results[:n] 
                if (i != 2 and doc['name'] in relevant) or (i == 2 and doc['name'][0] in relevant)
            ])/len(relevant)


        def calculate_metric(key, results, relevant):
            return metrics[key](results, relevant)

        # Define metrics to be calculated
        evaluation_metrics = {
            'ap': 'Average Precision',
            'p10': 'Precision at 10 (P@10)',
            'r10': 'Recall at 10 (R@10)',
        }

        # Calculate all metrics and export results as LaTeX table
        df = pd.DataFrame([['Metric','Value']] +
            [
                [evaluation_metrics[m], calculate_metric(m, results, relevant)]
                for m in evaluation_metrics
            ]
        )

        if i == 0:
            filename = 'results_normal.tex'
        elif i == 1:
            filename = 'results_weight.tex'
        else:
            filename = 'results_no_schema.tex'

        with open(filename,'w') as tf:
            tf.write(df.to_latex())

        # In a third step, we calculate the Precision-Recall curve for the query results, to provide
        # a more visual clue about the systems' performance.
        # PRECISION-RECALL CURVE
        precision_values = [
            len([
                doc 
                for doc in results[:idx]
                if (i != 2 and doc['name'] in relevant) or (i == 2 and doc['name'][0] in relevant)
            ]) / idx 
            for idx, _ in enumerate(results, start=1)
        ]

        recall_values = [
            len([
                doc for doc in results[:idx]
                if (i != 2 and doc['name'] in relevant) or (i == 2 and doc['name'][0] in relevant)
            ]) / len(relevant)
            for idx, _ in enumerate(results, start=1)
        ]

        if len(precision_values) == 0 or len(recall_values) == 0:
            continue

        precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

        # Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
        if USE_INTERPOLATION:
            recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
            recall_values = sorted(set(recall_values))

        # Extend matching dict to include these new intermediate steps
        for idx, step in enumerate(recall_values):
            if step not in precision_recall_match:
                if recall_values[idx-1] in precision_recall_match:
                    precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
                else:
                    precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]

        disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)

        if(i == 0):
            disp.plot(ax=ax, name=f"Precision-recall w/ schema",
                color=color, linewidth=1)
        elif(i == 1):
            disp.plot(ax=ax, name=f"Precision-recall w/ modifiers",
                    color=color, linewidth=1.5)
        elif(i == 2):
            disp.plot(ax=ax, name=f"Precision-recall schemaless",
                color=color, linewidth=1)
        i += 1

    # add the legend for the iso-f1 curves
    handles, labels = disp.ax_.get_legend_handles_labels()

    # set the legend and the axes
    ax.legend(handles=handles, labels=labels, loc="best")

    if USE_INTERPOLATION:
        ax.set_title("Interpolated Precision-Recall curve")
        plt.savefig('precision_recall_interpolation.png')
    else:
        ax.set_title("Precision-Recall curve")
        plt.savefig('precision_recall.png')
