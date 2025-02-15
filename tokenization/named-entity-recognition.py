sentence = "The Eiffel Tower was built from 1887 to 1889 by french engineer Gistave Eiffel, whose company specialized in building metal frameworks and structures."

"""
Here name entity tags will be 
Person Eg:- Gistave Eiffel
Place or location:- Paris (not given in above sentence)
Date Eg:- 1887-1889, or any particular data 01-01-1887
Time Eg:- 2 years, or may be 2 days, 2 months
Money Eg:- 1 million dollar (not present in above sentence)
Organization Eg:- iNeuron Pvt Ltd (not from above sentence)
Percent Eg:- 20%, twenty percent (not from above senctence)
"""

import nltk
nltk.download('maxent_ne_chunker')
nltk.download('words')
wordTokenize = nltk.word_tokenize(sentence)
# print(wordTokenize)
tag_elements = nltk.pos_tag(wordTokenize)

nltk.ne_chunk(tag_elements).draw()