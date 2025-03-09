"""
                Sentiment Analysis

DataSet => Text Preprocessing Part 1 => Text Preprocessing Part 2 => Text to Vectors
Text Preprocessing Part 1
1. Tokenization
2. Lowercase words
3. Regular Expressions

Text Preprocessing Part 2
1. Stemming
2. Lemmatization
3. Stop Words

Text->Vector (text will be represented by numerical format)
1. One not encoded
2. Bag of words(BOD)
3. TF-IDF
4. Word2Vec
5. AvgWord2Vec
"""

"""

One not encoding

    Text                        O/P           Unique words vocabulary
                                              The food is good bad Pizza amazing
 D1 The food is good            1             1    0   0  0    0   0      0 (vector representation of The word, others arw 0)
 D2 The food is bad             0             0    1   0  0    0   0      0 (vector representation of food word, others are 0)
 D3 Pizza is amazing            1
 
D1 will be -> (matrix size 4X7)
 [
    [1 0 0 0 0 0 0], (The)
    [0 1 0 0 0 0 0], (food)
    [0 0 1 0 0 0 0], (is)
    [0 0 0 1 0 0 0]  (bad)
 ]
 
D2 will be -> (matrix size 4X7)
 [
    [1 0 0 0 0 0 0], (The)
    [0 1 0 0 0 0 0], (food)
    [0 0 1 0 0 0 0], (is)
    [0 0 0 0 1 0 0]  (bad)
 ]
 
D3 will be -> (matrix size 3X7)
 [
    [0 0 0 0 0 1 0], (Pizza)
    [0 0 1 0 0 0 0], (is)
    [0 0 0 0 0 0 1], (amazing)
 ]
 
 Advantages
1. Easy to implement with Python (having specific libraries to do it)

Disadvantages
1. Sparse Matrix -> over fitting
2. ML algorithm, we need fixed size matrix, which is not available here
3. No semantic meaning is being capture.
4. Vocabulary is not capture

------------------------------------------------------------------------------------------------
Bag of words (BOW)

Dataset                     O/P     Lowercase all the words => stopwords =>
He is a good boy.           1       good boy (sentence1)
He is a bad boy.            1       good girl (sentence2)
Boy and girl are good.      1       boy girl good (sentence3)

Vocabulary  frequency(high to low)
good        3
boy         2
girl        2

Then

    good boy girl
S1  1    1   0
S2  1    0   1
S3  1    1   1

Two types of BOW -> Binary BOW and normal BOW -

If let say S1 contains 2 good then with normal BOW s1 => 2 1 0 (count updated based on frequency), 
but in binary BOW it will remain same as before s1 => 1 1 0

Advantages
1. Simple and intuitive.
2. Fixed size Input, suited for ML algos.

Disadvantages
1. SParse matrix or array overfitting.
2. Ordering of words getting changed, high frequency will comes first, means meaning also changed.
3. Out of vocabulary (Let say in S3 we have 'boy girl good school', but this school is not present in matrix, so it will be rejected/omitted.)
4. Semantic meaning is still not getting captured.
"""
