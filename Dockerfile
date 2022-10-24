FROM solr:8.10

COPY assets/processed_reviews.json /data/reviews.json

COPY assets/schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
