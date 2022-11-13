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
QUERY_URL = "http://localhost:8983/solr/reviews/select?_=1668256462851&defType=edismax&indent=true&q=Telecommunications&q.op=OR&qf=name+industry+description&rows=10"
# get here the url with edisMax and weights
QUERY_URL_WEIGHT = "http://localhost:8983/solr/reviews/select?_=1668256701596&defType=edismax&indent=true&q=Telecommunications&q.op=OR&qf=name%5E1.5+industry%5E2+description&rows=10"


get_metrics(True, QRELS_FILE, QUERY_URL, QUERY_URL_WEIGHT)
get_metrics(False, QRELS_FILE, QUERY_URL, QUERY_URL_WEIGHT)
