""" Stemming is the process of reducing a word to its word stem that affixes to suffixes
  and prefixes or to the roots of words known as lemma. Stemming is important in
  Natural language processing (NLU) and Natural language processing (NLP)
  In stemming we will get stem word.
"""

"""
Tokenization

Corpus = Sentences, 
Documents = Sentences, 
Vocabulary = Unique words, 
Words = 
"""

"""
Usage of stemming :-
Classification problem, 
comments on product is a positive review or negative review,
Reviews -> eating, eat, eaten => eat, going, goes, gone => go,
Email spam check
"""

from nltk.stem import PorterStemmer
stemming = PorterStemmer()

words = ['eating','eats', 'eaten', 'writing', 'writes', 'programming', 'programs', 'history', 'finally', 'finalized', 'congratulations']

for word in words:
    print(word+' ---> '+stemming.stem(word))

""" 
Disadvantage of stemming :- 
Like it change history => histori, congratulations => congratul some words meaning can be changed 
"""

"""---------------------------------------------------------------------------------------------------------"""

"""
Regexp Stemmer
The Regexp Stemmer, or Regular Expression Stemmer, is a stemming algorithm that utilizes regular expressions to identify and remove suffixes from words. It allows users to define custom rules for stemming by specifying patterns to match and remove.
"""

from nltk.stem import RegexpStemmer
regexStemmer = RegexpStemmer('ing$|s$|e$|able$', min=4)
output = regexStemmer.stem('eating')
print("\n RegexpStemmer output of eating is "+output)
print('\n')

"""---------------------------------------------------------------------------------------------------------"""

"""
Snowball Stemmer, better than porter stemmer
"""
from nltk.stem import SnowballStemmer
snowBall = SnowballStemmer('english')

for word in words:
    print(word+" word -> "+snowBall.stem(word))