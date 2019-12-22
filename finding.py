#by Abdul Mohiz
from multi import task
from nltk import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from gensim.models import Word2Vec


single_word = u"پسندیدہ"
corpus_token = task()
text_input = word_tokenize(u"آپ کی پسندیدہ خوشبو کون سی ہے؟")
text_input1 = word_tokenize(u"آپ کی پسندیدہ خوشبو کون سی ہے؟")

#vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(), min_df=1)
#vect_2 = vectorizer.fit_transform(text_input1)
#for x in vectorizer.vocabulary_:
 #   print(x)

vectorizer = TfidfVectorizer()
response = vectorizer.fit_transform(text_input1)
print(response)


def computeReviewTFDict(review):
    """ Returns a tf dictionary for each review whose keys are all
    the unique words in the review and whose values are their
    corresponding tf.
    """
    # Counts the number of times the word appears in review
    reviewTFDict = {}
    for word in review:
        if word in reviewTFDict:
            reviewTFDict[word] += 1
        else:
            reviewTFDict[word] = 1
    # Computes tf for each word
    for word in reviewTFDict:
        reviewTFDict[word] = reviewTFDict[word] / len(review)
    return reviewTFDict


computeReviewTFDict(text_input)


def computeCountDict(tfDict):
    """ Returns a dictionary whose keys are all the unique words in
    the dataset and whose values count the number of reviews in which
    the word appears.
    """
    countDict = {}
    # Run through each review's tf dictionary and increment countDict's (word, doc) pair
    for review in tfDict:
        for word in review:
            if word in countDict:
                countDict[word] += 1
            else:
                countDict[word] = 1
    return countDict
countDict = computeCountDict(text_input)



def computeReviewTFIDFDict(reviewTFDict):
    """ Returns a dictionary whose keys are all the unique words in the
    review and whose values are their corresponding tfidf.
    """
    reviewTFIDFDict = {}
    #For each word in the review, we multiply its tf and its idf.
    for word in reviewTFDict:
        reviewTFIDFDict[word] = reviewTFDict[word] * idfDict[word]
    return reviewTFIDFDict

  #Stores the TF-IDF dictionaries
tfidfDict = [computeReviewTFIDFDict(review) for review in tfDict]



# Create a list of unique words
wordDict = sorted(countDict.keys())

def computeTFIDFVector(review):
    tfidfVector = [0.0] * len(wordDict)

    # For each unique word, if it is in the review, store its TF-IDF value.
    for i, word in enumerate(wordDict):
        if word in review:
            tfidfVector[i] = review[word]
    return tfidfVector


tfidfVector = [computeTFIDFVector(review) for review in tfidfDict]



def dot_product(vector_x, vector_y):
    dot = 0.0
    for e_x, e_y in zip(vector_x, vector_y):
       dot += e_x * e_y
    return dot



def magnitude(vector):
    mag = 0.0
    for index in vector:
      mag += math.pow(index, 2)
    return math.sqrt(mag)



review_similarity = dot_product(tfidfVector[0], tfidfVector[1]) / magnitude(tfidfVector[0]) * magnitude(tfidfVector[1])

print(review_similarity)

#for row in corpus_token:
 #   for elem in row:
  #      print(elem, end=' ')
