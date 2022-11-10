FROM solr:8.10

COPY assets/reviews.json /data/reviews.json
COPY solr/schema.json /data/schema.json
COPY solr/startup.sh /scripts/startup.sh

COPY solr/stopwords.txt /data/stopwords.txt
COPY solr/synonyms.txt /data/synonyms.txt

ENTRYPOINT ["/scripts/startup.sh"]
