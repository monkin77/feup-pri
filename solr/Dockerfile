FROM solr:8.10

COPY ../assets/reviews.json /data/reviews.json

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
