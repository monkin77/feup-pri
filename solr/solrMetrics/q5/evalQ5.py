import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..')
sys.path.append( mymodule_dir )
from metrics import get_metrics

import json
from itertools import cycle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from sklearn.metrics import PrecisionRecallDisplay

USE_INTERPOLATION = True

### First step: read the qrels file and fetch query results from Solr's REST API 
QRELS_FILE = "relevantResults.txt"
# get here the url with edisMax
QUERY_URL = "http://localhost:8983/solr/reviews/select?_=1668349399598&defType=edismax&fl=*+score&indent=true&q=%22Health+Technology%22&q.op=AND&qf=name+industry+rating+description&start=0"
# get here the url with edisMax and weights
QUERY_URL_WEIGHT = "http://localhost:8983/solr/reviews/select?_=1668337947107&defType=edismax&fl=*+score&indent=true&q=%22Health+Technology%22~20%0ATechnology%5E2&q.op=AND&qf=name+industry%5E1.5+rating+description&start=0"

get_metrics(True, QRELS_FILE, QUERY_URL, QUERY_URL_WEIGHT)
get_metrics(False, QRELS_FILE, QUERY_URL, QUERY_URL_WEIGHT)
