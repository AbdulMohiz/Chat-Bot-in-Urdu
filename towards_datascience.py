

import numpy as np
import nltk
import sklearn
from task1_ import array_questions
from multi import task
from nltk import word_tokenize


#print(Ques)
#print(Ans)

#corpus_token = task()
"""for i,s in enumerate(corpus_token):
    for words in [s]:
        print('First 7 tokens from news headlines: ', words[:7])
"""

#def output(question):
 #   return Ans[euclidean()]

#print(output(u"آپ کے جوتے"))

#text_input[0] = word_tokenize(u"آپ کی پسندیدہ خوشبو کون سی ہے؟")
#print(text_input)
#text_input[0] = word_tokenize()
#(u"آپ کے جوتے")
#word_tokenize(u"اپنا نام بتائیں")

#print(corpus_token)
#new_corpus = text_input + corpus_token
#print(new_corpus[5])

from numpy import argmax




def transform(headlines):
    tokens = [w for s in headlines for w in s]
    #print()
    #print('All Tokens:')
    #print(tokens)

    results = []
    label_enc = sklearn.preprocessing.LabelEncoder()
    onehot_enc = sklearn.preprocessing.OneHotEncoder()

    encoded_all_tokens = label_enc.fit_transform(list(set(tokens)))
    encoded_all_tokens = encoded_all_tokens.reshape(len(encoded_all_tokens), 1)

    onehot_enc.fit(encoded_all_tokens)

    for headline_tokens in headlines:
        #print()
        #print('Original Input:', headline_tokens)

        encoded_words = label_enc.transform(headline_tokens)
        #print('Encoded by Label Encoder:', encoded_words)

        encoded_words = onehot_enc.transform(encoded_words.reshape(len(encoded_words), 1))
        #print('Encoded by OneHot Encoder:')
        #print(encoded_words)

        results.append(np.sum(encoded_words.toarray(), axis=0))
    return results

#transformed_input = transform(text_input)
#print(transformed_input[0])
#print('_____')
#print(transformed_results[0])

def euclidean(txt):


    a = task()

    Ques = a[:len(a) // 2]
    Ans = a[len(a) // 2:]
    n = 0
    text_input = [n]
    text_input[0] = word_tokenize(txt)
    #text_input[0] = word_tokenize(u"آپ کے جوتے")
    new_corpus = text_input + Ques

    transformed_results = transform(new_corpus)
    #print('EUCLIDEAN SIMILARITY')
    #print('Master Sentence: %s' % new_corpus[0])
    score1 = []
    news_headline1 = []
    ind = []
    for i, news_headline in enumerate(new_corpus):
        score = sklearn.metrics.pairwise.euclidean_distances([transformed_results[i]], [transformed_results[0]])[0][0]
        if score >0:
            #print('-----')
            score1.append(score)
            #print(score1)
            ind = i
            print(transformed_results[i])
            news_headline1.append(news_headline)
            print('Score: %.2f, Index  %d,Comparing Sentence: %s' % (score, ind, news_headline))
    return Ans[(score1.index(min(score1)))]


#print(euclidean())


#print("__________________")
#print()

a = task()

Ques = a[:len(a) // 2]
Ans = a[len(a) // 2:]
n = 0
text_input = [n]
#text_input[0] = word_tokenize(txt)
text_input[0] = word_tokenize(u"آپ کے جوتے")
new_corpus = text_input + Ques

def cosine():
    #a = task()

    #Ques = a[:len(a) // 2]
    #Ans = a[len(a) // 2:]
    #n = 0
    #text_input = [n]
    #text_input[0] = word_tokenize(txt)
    # text_input[0] = word_tokenize(u"آپ کے جوتے")
    #new_corpus = text_input + Ques

    transformed_cosine = transform(new_corpus)
    #print('COSINE SIMILARITY')
    #print('_________')
    score1 = []
    news_headline1 = []
    ind = []
    #print('Master Sentence: %s' % new_corpus[0])
    for i, news_headline in enumerate(new_corpus):
        score = sklearn.metrics.pairwise.cosine_similarity([transformed_cosine[i]], [transformed_cosine[0]])[0][0]
        if score > 0.4 and score < 1:
            score1.append(score)
            ind = i
            news_headline1.append(news_headline)
            #print('-----')
            #print('Score: %.2f, Integer %d, Comparing Sentence: %s' % (score, ind, news_headline))

    return news_headline1
    #Ans[(score1.index(min(score1)))]
        #score1.index(max(score1))

#print(cosine())

from stop_word_removal import stop_words_removal

def distance(txt):
    a = task()
    index = 0
    max = 0
    Ques = a[:len(a) // 2]
    Ans = a[len(a) // 2:]
    user_ques = word_tokenize(txt)
    for i, single_question in enumerate(Ques):
        count = 0
        for token in user_ques:
            for eachtoken in single_question:
                if (token == eachtoken):
                    count = count + 1

        if (count > max):
            max = count
            index = i
    return Ans[index]



def closest(number, score):
    a = abs(number-score)
    b = 1 - a
    return b


def backend(txt):
    a = task()

    Ques = a[:len(a) // 2]
    Ans = a[len(a) // 2:]
    n = 0
    text_input = [n]
    text_input[0] = word_tokenize(txt)
    #text_input[0] = word_tokenize(u"آپ کے جوتے")
    new_corpus = text_input + Ques

    transformed_results = transform(new_corpus)
    transformed_cosine = transform(new_corpus)
    return euclidean(transformed_results)




#q = output(text_input[0])






"""def transform23(headlines):
    #tokens = [w for s in corpus_token for w in s]
    tokens = [w for s in a for w in s]
    print()
    #print('All Tokens:')
    #print(tokens)

    results = []
    label_enc = sklearn.preprocessing.LabelEncoder()
    onehot_enc = sklearn.preprocessing.OneHotEncoder()

    encoded_all_tokens = label_enc.fit_transform(list(set(tokens)))
    encoded_all_tokens = encoded_all_tokens.reshape(len(encoded_all_tokens), 1)

    onehot_enc.fit(encoded_all_tokens)

    for headline_tokens in Ques:
       # print()
        #print('Original Input:', headline_tokens)

        encoded_words = label_enc.transform(headline_tokens)
        #print('Encoded by Label Encoder:', encoded_words)

        encoded_words = onehot_enc.transform(encoded_words.reshape(len(encoded_words), 1))
        #print('Encoded by OneHot Encoder:')
        #print(encoded_words)

        results.append(np.sum(encoded_words.toarray(), axis=0))
    return results"""