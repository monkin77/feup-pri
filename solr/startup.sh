#!/bin/bash

precreate-core reviews

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Wait for solr to properly start
sleep 2

cp /data/stopwords.txt /var/solr/data/reviews/conf
cp /data/synonyms.txt /var/solr/data/reviews/conf

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/reviews/schema

# Populate collection
bin/post -c reviews /data/reviews.json

# Restart in foreground mode so we can access the interface
solr restart -f
