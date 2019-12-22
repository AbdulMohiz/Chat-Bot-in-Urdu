#By Abdul Mohiz

from task1_ import array_questions
from tokenize import tokenize
from nltk.tokenize import word_tokenize


def task():
    a = array_questions()
    n = 1
    #demo = [a[i:i+n] for i in range(0, len(a), n)]
    k = []
    tokenize_sentence = [word_tokenize(i) for i in a]
    for i in tokenize_sentence:
        k.append(i)
    return k
