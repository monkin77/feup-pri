## Setup
Run SOLR instance with docker:
```console
cd solr
docker build -t solr-pri .
docker run --name solr-pri-container -p 8983:8983 -it solr-pri
```

## Important requests

**suggester**: http://localhost:8983/solr/reviews/suggest?q.op=AND&q=tech

**spellchecker**: http://localhost:8983/solr/reviews/spellcheck?q=teck

**faceting**: http://localhost:8983/solr/reviews/select?q=*:*&facet=true&facet.field=industry&facet.field=employees&facet.field=revenue&facet.field=interview.experience&facet.field=interview.difficulty&facet.limit=1000

Possible fields to use facets: industry, employees, revenue, interview.experience, interview.difficulty

This query also returns results (response field) but that can be ignored, only facet_counts matters.

Use facet.sort=<count/index> to alternate between most popular and lexicographic order