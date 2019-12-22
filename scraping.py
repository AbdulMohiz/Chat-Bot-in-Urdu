from requests import get
from bs4 import BeautifulSoup
from stop_word_removal import stop_words_removal
import re
import nltk

# coding = utf-8
#wikipedia.set_lang("Urdu")
#پاکستاں
#se = "خان"
se = "پاکستان"
se2 = "دارالحکومت"
se3 = "دنیا"
se4 = "استاد"
se5 = "علم"
se6 = "سائنسی"
url = "https://ur.wikipedia.org/wiki/" + se
page = get(url)
soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
ff = soup.findAll("p")
#print(ff)


def sent(scrappp, query):
    sentence = []
    sentence = ".".join((sentence for sentence in scrappp.split(".")
                         if query not in sentence))
            #sentence = [al for al in sentence if not re.match(r'[^\w]', al, re.I)]
            #sentence = [w1 for w1 in sentence if not re.match(r'[A-Z]+', w1, re.I)]
            #sentence = "".join(sentence)
    return sentence


tb = soup.find('div', class_="mw-parser-output")
a = tb.get_text('p')
aa = tb.findAll('p')
#print(aa)
#print(a)
scrap = tb.get_text()

#print(nltk.word_tokenize(scrap))
print(scrap.find("انسان"))


for sc in nltk.word_tokenize(scrap):
    if se.find(se) in sc:
        sentence = "۔".join((s for s in sc.split("۔")
                             if se not in s))
        print(sentence)


for soo in scrap.split(" "):
    #print(soo)
    if se in soo:
        sentence = "۔".join((s for s in scrap.split("۔")
                           if se not in s))
        #print(sentence)


#print(sent(scrap, se5))
a = scrap.find(se)



def find_features(scra, query, feature_frequency, ngram_window):
    #file_name = str(file_name)[2:len(str(file_name)) - 2]
    import nltk
    from nltk.util import ngrams
    import re
    from stop_word_removal import stop_words_removal
    from bs4 import BeautifulSoup

    # feature_frequency =9;
    # ngram_window = 3;
    # query = 'دنیا';
    tokens = nltk.word_tokenize(scra)
    tokens = [w for w in tokens if not re.match(r'[A-Z]+', w, re.I)]
    tokens = [r for r in tokens if not re.match(r'[^\w]', r, re.I)]
    final = stop_words_removal(tokens)
    #print(final)
    # print("without stopwords"+tokens);
    # from stop_word_removal import stop_words_removal
    # tokens=stop_words_removal(tokens2);
    # print("with stopwords"+tokens)
    # print("without stopwords"+tokens)
    # Gets the Ngram based on the ngram size defined above
    data = []
    bg = ngrams(tokens, ngram_window)
    x = 0
    count = 0
    for ng in bg:
        x = x + 1
        # if the ngram contains the query, append it to data
        if (str(ng).find(query) > 0):
            data.append(ng)
            # print(ng);
            count += 1
    # print the ngram array
    # print(data)

    # code to get unigrams for frequency distribution
    new_data = []
    new_bg = ngrams(tokens, 1)
    for ng in new_bg:
        new_data.append(ng)

    import re, codecs
    Encode, Decode, Reader, Writer = codecs.lookup("UTF-8")

    all_words = []
    # string="";
    # get frequency distribution of new_data
    fdist = nltk.FreqDist(new_data)
    for k, v in fdist.items():
        # deal only if its frequency is > feature_frequency
        if (v > feature_frequency):
            # print (k,v)

            # remove unnecessary charachters below
            k = re.sub(",", "", str(k))
            k = re.sub("'", "", str(k))
            k = re.sub("\(", "", str(k))
            k = re.sub("\)", "", str(k))
            # append them to all_words
            all_words.append(k)

    # print(all_words);

    # remove stop words from the above created list.
    from stop_word_removal import stop_words_removal
    data2 = stop_words_removal(all_words)
    # features=data2.split(" ",2)
    features_string = str(data2)
    new_features = nltk.word_tokenize(features_string)
    new_features = [w1 for w1 in data2 if not re.match(r'[A-Z]+', w1, re.I)]
    new_features = [al for al in data2 if not re.match(r'[^\w]', al, re.I)]
    # print("features are :: "+str(new_features))
    # print("ngrams are ::"+str(data))

    potential_features = []
    sentence = []
    for j in range(0, len(new_features)):
        if (new_features[j] != ''):
            if (str(data).find(new_features[j]) > 0):
                potential_features.append(new_features[j])
                # print("feature found"+new_features[j])
        # Maximum size - The last item resides at x-1
        # print(data);
        a = " ".join(potential_features)
        sentence = ".".join(s for s in a.split(".")
                            if query not in s)

    return potential_features


result = find_features(scrap, se, 9, 5)
print(result)