#!/bin/bash

cd ..
docker build -t solr-pri -f solr/Dockerfile .
docker run --name solr-pri-container -p 8983:8983 -it --rm solr-pri
