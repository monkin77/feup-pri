FROM solr:8.10

COPY assets/reviews.json /data/reviews.json
COPY solr/schema.json /data/schema.json
COPY solr/startup.sh /scripts/startup.sh

COPY solr/stopwords.txt /data/stopwords.txt
COPY solr/synonyms.txt /data/synonyms.txt

COPY solr/cors_web.xml /opt/solr-8.10.1/server/solr-webapp/webapp/WEB-INF/web.xml

ENTRYPOINT ["/scripts/startup.sh"]
