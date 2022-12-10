# PRI Project <NAME TO DECIDE>
 
Run SOLR instance with docker:
```console
cd solr
docker build -t solr-pri .
docker run --name solr-pri-container -p 8983:8983 -it solr-pri
```

### Working directory -> root folder

### Important requests

**suggester**: http://localhost:8983/solr/reviews/suggest?q.op=AND&q=tech

**spellchecker**: http://localhost:8983/solr/reviews/spellcheck?q=teck

**faceting**:
