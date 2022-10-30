#!/bin/bash

docker build -t solr-pri .
docker run --name solr-pri-container -p 8983:8983 -it --rm solr-pri
