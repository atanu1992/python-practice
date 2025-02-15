"""
Wordnet Lemmatizer

Lemmatization technique is like stemming. The output we will get after lemmatization is called 'lemma', which is a root
word rather than root stem, the output of stemming. After lemmatization, we will be getting a valid word that means the same thing.

NLTK provides WordNetLemmatizer class which is a thin wrapper around the wordnet corpus. This class uses morphy() function to the
WordNet corpus reader class to find a lemma.
"""
# import nltk
# nltk.download('wordnet') ### download it first, if not downloaded

from nltk.stem import WordNetLemmatizer
wordLemma = WordNetLemmatizer()

"""
lemmatize function has 2 parameters, string, pos
pos is type of string, default is pos = 'n'
other types of pos are
'n' = Noun
'v' = Verb
'a' = Adjective
'r' = Adverb
"""

output = wordLemma.lemmatize('going') ### output going
output1 = wordLemma.lemmatize('going', pos='v') ### output go
output2 = wordLemma.lemmatize('congratulation')
print(output)
print(output1)
print(output2)

words = ['eating','eats', 'eaten', 'writing', 'writes', 'programming', 'programs', 'history', 'finally', 'finalized', 'congratulations']
for word in words:
    print(word + ' word --> ' + wordLemma.lemmatize(word, pos='v'))

"""
Lemmatization is slow than stemming.
Use cases are:-
Q&A, chatbots, summarization
"""