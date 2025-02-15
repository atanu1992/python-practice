"""
Stopwords
A stop word is a commonly used word (such as “the”, “a”, “an”, or “in”) that a search engine has been programmed to ignore, both when indexing entries for searching and when retrieving them as the result of a search query.

We would not want these words to take up space in our database or take up valuable processing time. For this, we can remove them easily, by storing a list of words that you consider to stop words.
"""
from nltk.corpus import stopwords

from tokenization.ntlk import sentence

paragraph = "I have three visions for India. In 3000 years of our history people from all over the world have come and invaded us, captured our lands, conquered our minds. From Alexander onwards the Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of them came and looted us, took over what was ours. Yet we have not done this to any other nation. We have not conquered anyone. We have not grabbed their land, their culture and their history and tried to enforce our way of life on them. Why? Because we respect the freedom of others. That is why my FIRST VISION is that of FREEDOM. I believe that India got its first vision of this in 1857, when we started the war of Independence. It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us. We have 10 percent growth rate in most areas. Our poverty levels are falling. Our achievements are being globally recognised today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect? MY SECOND VISION for India is DEVELOPMENT. For fifty years we have been a developing nation. It is time we see ourselves as a developed nation. We are among top five nations in the world in terms of GDP.I have a THIRD VISION. India must stand up to the world. Because I believe that unless India stands up to the world, no one will respect us. Only strength respects strength. We must be strong not only as a military power but also as an economic power. Both must go hand-in-hand. My good fortune was to have worked with three great minds. Dr.Vikram Sarabhai, of the Dept. of Space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material. I was lucky to have worked with all three of them closely and consider this the great opportunity of my life."

# from nltk.corpus import stopwords

import nltk
# nltk.download('stopwords')
# englishWords = stopwords.words('english')
# print(englishWords)

print("\n Stopwords ")
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
sentences = nltk.sent_tokenize(paragraph)
print("Original sentence :- ",sentences)

### Apply stopwords and filter and then apply stemming
for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words) # converting all the words to sentences

print("Sentences with porter stemmer :- ",sentences)

### Apply stopwords and filter and then apply SnowballStemmer
from nltk.stem import SnowballStemmer
snowBall = SnowballStemmer('english')

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [snowBall.stem(word) for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words) # converting all the words to sentences

print("Sentences with snow ball stemmer :- ",sentences)

### Apply stopwords and filter and then apply WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
wordLemma = WordNetLemmatizer()

for i in range(len(sentences)):
    sentences[i] = sentences[i].lower()
    words = nltk.word_tokenize(sentences[i])
    words = [wordLemma.lemmatize(word, pos='v') for word in words if word not in set(stopwords.words('english'))]
    sentences[i]=' '.join(words) # converting all the words to sentences

print("Sentences with WordNet Lemmatizer :- ",sentences)