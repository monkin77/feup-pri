import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.corpus import wordnet as wn

f = open("synonyms.txt", "w")

for syn in wn.all_synsets():
    synonyms = ','.join(syn.lemma_names())
    f.write(synonyms + "\n")
