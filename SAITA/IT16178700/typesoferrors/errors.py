# WordNet implementation
from nltk.corpus import wordnet
from nltk.corpus.reader import Synset

syn = wordnet.synsets("error")[0]

print("Syntax name : ", syn.name())

# Defining the word
print("\nSyntax meaning : ", syn.definition())

# list of phrases that use the word in context
print("\nSyntax example : ", syn.examples())

syn.hypernym_paths()
[[Synset('address'), Synset('already'), Synset('in'), Synset('use'),
  Synset('unable'), Synset('to'), Synset('open'), Synset('logs'),
  Synset('application'), Synset('run'), Synset('failed')]]
