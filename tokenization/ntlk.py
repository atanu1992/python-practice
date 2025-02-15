# Corpus
corpus = """Python syntax is straightforward and has no complex structures, like C++ or Java. Also, it emphasizes code readability by using English keywords and eliminating the need for delimiters. This makes Python code easy to read and understand."""

# Import necessary libraries
from nltk.tokenize import sent_tokenize

# Download 'punkt' if not already downloaded
# import nltk
# nltk.download('punkt')

# Tokenization: Sentence/document -> Paragraph
documents = sent_tokenize(corpus)
print(type(documents))
print(documents)

print('\n')
# Iterate over it
for sentence in documents:
    print(sentence)

# Tokenization:
# paragraph -> words
print('\n------- Paragraph -> words ------------')
from nltk.tokenize import word_tokenize

words = word_tokenize(corpus)
print(words)

print('\n------- Sentence -> words ------------')
# sentence -> words
for sentence in documents:
    print(word_tokenize(sentence))

print('\n------- wordpunct_tokenize function ------------')
# Word punctuation, here in corpus you can see apostophies
from nltk.tokenize import wordpunct_tokenize
wordpunct = wordpunct_tokenize(corpus)
print(wordpunct)

print('\n------- TreebankWordDetokenizer function ------------')
# full stop is not separated word, but last full stop will be separated.
from nltk.tokenize import TreebankWordDetokenizer
tokenizer = TreebankWordDetokenizer()
tree_words = tokenizer.tokenize(corpus)
print(tree_words)

# Question - Difference between wordpunct_tokenize and TreebankWordDetokenizer ?
# Ans - TreebankWordDetokenizer allow fullstops with word, except the last one, wordpunct_tokenize consider every fullstops as separate word