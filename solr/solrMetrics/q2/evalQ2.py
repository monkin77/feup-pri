import os
import sys

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..')
sys.path.append( mymodule_dir )
from metrics import get_metrics

USE_INTERPOLATION = True

### First step: read the qrels file and fetch query results from Solr's REST API 
QRELS_FILE = "relevantResults.txt"
# get here the url with edisMax
QUERY_URL = "http://localhost:8983/solr/reviews/select?_=1668355769457&defType=edismax&indent=true&q=Sport&q.op=OR&qf=name&start=0"
# get here the url with edisMax and weights
QUERY_URL_WEIGHT = "http://localhost:8983/solr/reviews/select?_=1668355769457&defType=edismax&indent=true&q=Sport~1&q.op=OR&qf=name&start=0"


#get_metrics(True, QRELS_FILE, QUERY_URL, QUERY_URL_WEIGHT)
get_metrics(False, QRELS_FILE, QUERY_URL, QUERY_URL_WEIGHT)
