import json
from itertools import cycle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from sklearn.metrics import PrecisionRecallDisplay


### First step: read the qrels file and fetch query results from Solr's REST API 
QRELS_FILE = "q1/results.txt"
# get here the url with edisMax
QUERY_URL = "http://localhost:8983/solr/reviews/select?_=1668191500840&defType=edismax&fl=name,+rating,+reviews,+description,+happiness*,+ratings*,+headquarters,+employees,+industry,+revenue,+custom_rating,+ceo*,+interview*,+locations*,+roles*,+salary*,+score&indent=true&q=telecommunication%0A%5B4+TO+5%5D&q.op=OR&qf=name+industry+rating&rows=20"
# get here the url with edisMax and weights
QUERY_URL_WEIGHT = "http://localhost:8983/solr/#/reviews/query?q=telecommunication%0A%5B4%20TO%205%5D&q.op=OR&defType=edismax&indent=true&qf=name%20industry%20rating&fl=name,%20rating,%20reviews,%20description,%20happiness*,%20ratings*,%20headquarters,%20employees,%20industry,%20revenue,%20custom_rating,%20ceo*,%20interview*,%20locations*,%20roles*,%20salary*,%20score&rows=20"

# Read qrels to extract relevant documents
relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))
# Get query results from Solr instance
results = requests.get(QUERY_URL).json()['response']['docs']

# get the results with weights
results_weight = requests.get(QUERY_URL_WEIGHT).json()['response']['docs']

# get the results with no schema
results_no_schema = json.load(open('noSchema.json', encoding="utf8"))['response']['docs']

# In a second step, we calculate some common evaluation metrics that can be used to compare systems and to assess their performance.
# METRICS TABLE
# Define custom decorator to automatically calculate metric based on key
metrics = {}
def metric(f): return metrics.setdefault(f.__name__, f)

@metric
def ap(results, relevant):
  """Average Precision"""

  precision_values = [
      len([
          doc
          for doc in results[:idx]
          if doc['name'] in relevant
      ]) / idx
      for idx in range(1, len(results) + 1)
  ]
  
  return sum(precision_values) / len(relevant)

@metric
def p10(results, relevant, n=10):
  """Precision at N"""
  return len([doc for doc in results[:n] if doc['name'] in relevant])/n

@metric
def r10(results, relevant, n=10):
  """Recall at N"""
  return len([doc for doc in results[:n] if doc['name'] in relevant])/len(relevant)

## check what is this
@metric
def ndcg(results, relevant):
  """Normalized Discounted Cumulative Gain"""

  dcg = 0
  for idx, doc in enumerate(results):
      if doc['name'] in relevant:
          dcg += 1 / np.log2(idx + 2)

  idcg = 0
  for idx, doc in enumerate(relevant):
      idcg += 1 / np.log2(idx + 2)

  return dcg / idcg

def calculate_metric(key, results, relevant):
  return metrics[key](results, relevant)

# Define metrics to be calculated
evaluation_metrics = {
    'ap': 'Average Precision',
    'p10': 'Precision at 10 (P@10)',
    'r10': 'Recall at 10 (R@10)',
    'ndcg': 'Normalized Discounted Cumulative Gain (NDCG)'
}

# Calculate all metrics and export results as LaTeX table
df = pd.DataFrame([['Metric','Value']] +
    [
        [evaluation_metrics[m], calculate_metric(m, results, relevant)]
        for m in evaluation_metrics
    ]
)

with open('q1/results.tex','w') as tf:
    tf.write(df.to_latex())

# In a third step, we calculate the Precision-Recall curve for the query results, to provide
# a more visual clue about the systems' performance.

# PRECISION-RECALL CURVE
# Calculate precision and recall values as we move down the ranked list
precision_values = [
    len([
        doc 
        for doc in results[:idx]
        if doc['name'] in relevant
    ]) / idx 
    for idx, _ in enumerate(results, start=1)
]

recall_values = [
    len([
        doc for doc in results[:idx]
        if doc['name'] in relevant
    ]) / len(relevant)
    for idx, _ in enumerate(results, start=1)
]

precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

# Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
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
disp.plot()
plt.savefig('q1/precision_recall.pdf')
