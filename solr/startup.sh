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

# Add suggester component
curl -X POST -H 'Content-type:application/json'  -d '{
  "add-searchcomponent": {
    "name": "suggest",
    "class": "solr.SuggestComponent",
    "suggester": {
        "name": "reviewsSuggester",
        "lookupImpl": "FreeTextLookupFactory",
        "dictionaryImpl": "DocumentDictionaryFactory",
        "field": "description_suggest",
        "suggestFreeTextAnalyzerFieldType": "basicText",
        "exactMatchFirst": "true",
        "buildOnStartup": "true"
    }
  }
}' http://localhost:8983/solr/reviews/config

# Add suggester request handler
curl -X POST -H 'Content-type:application/json'  -d '{
  "add-requesthandler": {
    "name": "/suggest",
    "class": "solr.SearchHandler",
    "startup": "lazy",
    "defaults": {
        "suggest": true,
        "suggest.count": 10,
        "suggest.dictionary": "reviewsSuggester"
    },
    "components": [
        "suggest"
    ]
  }
}' http://localhost:8983/solr/reviews/config

# Add spellchecker
curl -X POST -H 'Content-type:application/json'  -d '{
  "add-searchcomponent": {
    "name": "spellchecker",
    "class": "solr.SpellCheckComponent",
    "spellchecker": {
        "name": "default",
        "classname": "solr.IndexBasedSpellChecker",
        "spellcheckIndexDir": "./spellchecker",
        "field": "description_suggest",
        "buildOnCommit": "true"
    }
  }
}' http://localhost:8983/solr/reviews/config

# Add spellchecker request handler
curl -X POST -H 'Content-type:application/json'  -d '{
  "add-requesthandler": {
    "name": "/spellcheck",
    "class": "org.apache.solr.handler.component.SearchHandler",
    "startup": "lazy",
    "defaults": {
        "spellcheck": "true",
        "spellcheck.dictionary": "default",
        "suggest.count": 10,
        "df": "description_suggest",
        "spellcheck.collate": "true"
    },
    "last-components": [
        "spellchecker"
    ]
  }
}' http://localhost:8983/solr/reviews/config

# Populate collection
bin/post -c reviews /data/reviews.json

# Restart in foreground mode so we can access the interface
solr restart -f
