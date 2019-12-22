from task1_ import array_questions
import math

corpus_token = array_questions()
dict_of_words = {}
for i, s in enumerate(corpus_token):
    tokenize_words = s.split(' ')
    dict_of_words[i] = [(word, tokenize_words.count(word)) for word in tokenize_words]
#print(dict_of_words)



#remove duplicates
term_frequency = {}

for i in range(0, len(corpus_token)):
    list_no_duplicates = []
    for wordFreq in dict_of_words[i]:
        if wordFreq not in list_no_duplicates:
            list_no_duplicates.append(wordFreq)
        term_frequency[i] = list_no_duplicates
#print(term_frequency)



#Nomalized Term Frequency
normalized_termFrequency = {}
for i in range(0, len(corpus_token)):
    s = dict_of_words[i]
    length_sentence = len(s)
    list_normalized = []
    for wordFreq in term_frequency[i]:
        normalized_frequency = wordFreq[1]/length_sentence
        list_normalized.append((wordFreq[0], normalized_frequency))
    normalized_termFrequency[i] = list_normalized
#print(normalized_termFrequency)



#calculate inverse document frequency

#print(corpus_token)
all_documents = ''
for sentence in corpus_token:
    all_documents += sentence + ''
all_documents_toknized = all_documents.split(' ')
#print(all_documents_toknized)



doc_no_duplicates = []
for word in all_documents_toknized:
    if word not in doc_no_duplicates:
        doc_no_duplicates.append(word)
#print(doc_no_duplicates)



#no of documents where term T appears
dic_of_no_of_docs = {}

for index, vocab in enumerate(doc_no_duplicates):
    count = 0
    for s in corpus_token:
        if vocab in s:
            count += 1
    dic_of_no_of_docs[index] = (vocab, count)
#print(dic_of_no_of_docs)



#calculate IDF
dic_of_IDF = {}

for i in range(0, len(normalized_termFrequency)):
    list_of_IDFcals = []
    for word in normalized_termFrequency[i]:
        for x in range(0, len(dic_of_no_of_docs)):
            if word[0] == dic_of_no_of_docs[x][0]:
                list_of_IDFcals.append((word[0], math.log(len(corpus_token)/ dic_of_no_of_docs[x][1])))
    dic_of_IDF[i] = list_of_IDFcals
#print(dic_of_IDF)

#print(normalized_termFrequency[8])
#multiply to find TF-IDF
dictOFTF_IDF = {}
listOFTF_IDF = []
for i in range(20,len(normalized_termFrequency)):
    TFsentence = normalized_termFrequency[i]
    IDFsentence = dic_of_IDF[i]
    """
    #listOFTF_IDF = []
    
    
    for x in range(0, len(TFsentence)):
        listOFTF_IDF.append((TFsentence[x][0],TFsentence[x][1]*IDFsentence[x][1]))
    dictOFTF_IDF[i] = listOFTF_IDF"""
    #print(TFsentence)
    print(IDFsentence)
    #print(len(TFsentence))
#print(listOFTF_IDF)

