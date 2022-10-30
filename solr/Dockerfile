FROM solr:8.10

COPY assets/reviews.json /data/reviews.json

COPY solr/schema.json /data/schema.json

COPY solr/startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
