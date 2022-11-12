In this query, we are searching for companies related to telecommunications.

Using a no-boost search, we are looking for companies with any telecommunications relations, 
doesn't giving any weight in the field where it appears (name, industry, description).

Using the boost, we are weighting the telecommunications results on industry and name with weights of,
respectively, 2 and 1.5. This way, we get the results focused on the name and industry, getting more
precise results on the telecommunications fields, since the description field uses stemming and 
other filter techniques that will catch some unwanted results (this is intentional since descriptions 
normally have similar words).

Despite having an average precision of 1, without schema, we don't get good values because it's not retrieving
all the results we were expecting. Actually, it has a recall and precision at 10 of 0.2, since it just 
retrieves 2 of the relevant results, which is not what we want.
