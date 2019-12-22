from nltk.util import ngrams
from multi import task
from task1_ import array_questions
import nltk, re, string, collections
import nltk
from ngram import NGram



c = task()
cor = array_questions()


Ques = c[:len(c) // 2]
Ans = c[len(c) // 2:]
n = 0
se = [n]
se[0] = nltk.word_tokenize("پاکستان")
tex = se + Ques
print(tex)


grams = {}
words = 3

for k,i in enumerate(tex):
    v = NGram(i)


def comp(sa):
    for l in v.search(se, threshold=0.1):
        print("output:: ", l[0], "Next", l[1])


print(comp(se))


#grams = [tex[i:i+N] for i in xrange(len(tex)-N+1)]
"""for k,i in enumerate(tex):
    if k < len(tex) - 1:
        w1 = tex[k]
        w2 = tex[k + 1]
        gram = (w1, w2)
        print()
        if gram in grams:
            grams[gram] = grams[gram] + 1
        else:
            grams[gram] = 1


sorted_bigrams = sorted(grams.items(), key = lambda pair:pair[1], reverse = True)

for bigram, count in sorted_bigrams:
    print(bigram, ":", count)

"""
#for k,v in enumerate(c):
    #print(ngram.NGram.compare(se, v, n=2))
#print(c)
#tri = nltk.collocations.TrigramAssocMeasures()
#finder = TrigramCollocationFinder.from_words((c))
#finder.apply_freq_filter(3)
#print(finder.nbest(tri.pmi, 500000))

