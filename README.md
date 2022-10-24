# PRI Project <NAME TO DECIDE>
 
Run SOLR instance with docker:
```console
docker build -t solr-pri .
docker run --name solr-pri-container -p 8983:8983 -it solr-pri
```

### Working directory -> root folder