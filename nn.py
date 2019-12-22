from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from multi import task
from task1_ import array_questions
from towards_datascience import transform

a = task()

Ques = a[:len(a) // 2]
Ans = a[len(a) // 2:]
n = 0
text_input = [n]
txt = u"آپ کے جوتے"
text_input[0] = word_tokenize(txt)
new_corpus = text_input + Ques

taa = transform(new_corpus)

print(taa)


"""from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

corpus = [
    'All my cats in a row',
    'When my cat sits down, she looks like a Furby toy!',
    'The cat from outer space',
    'Sunshine loves to sit like this for some reason.'
]

vectorizer = CountVectorizer()
features = vectorizer.fit_transform(corpus).todense()
print(vectorizer.vocabulary_)

for f in features:
    print(euclidean_distances(features[0], f))
"""