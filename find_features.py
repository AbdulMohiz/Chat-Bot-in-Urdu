# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:01:06 2017
@author: Awais
"""


def find_features(file_name,query,feature_frequency,ngram_window):
    
    file_name=str(file_name)[2:len(str(file_name))-2]
    import nltk
    from nltk.util import ngrams
    from bs4 import BeautifulSoup
    
    #feature_frequency =9;
    #ngram_window = 3;
    #query = 'دنیا';
    curr_file=file_name;
    #curr_file='corpus/Technology3.txt';
    with open(curr_file, encoding='utf8') as infile:
        html = BeautifulSoup(infile, "html.parser")
        single_file_data={"file_name":curr_file,"title":str(html)}
        tokens=nltk.word_tokenize(single_file_data['title']);
        #print(tokens);
    #print("without stopwords"+tokens);
    #from stop_word_removal import stop_words_removal
    #tokens=stop_words_removal(tokens2);
    #print("with stopwords"+tokens)
    #print("without stopwords"+tokens)
    # Gets the Ngram based on the ngram size defined above
    data=[];
    bg=ngrams(tokens,ngram_window);
    x=0;
    count=0;
    for ng in bg:
        x=x+1;
        # if the ngram contains the query, append it to data
        if (str(ng).find(query)>0):
            data.append(ng);
            #print(ng);
            count+=1;
    # print the ngram array
    #print(data)
    
    
    
    # code to get unigrams for frequency distribution
    new_data=[];
    new_bg=ngrams(tokens,1);
    for ng in new_bg:
        new_data.append(ng);
    
    
    import re, codecs
    Encode, Decode, Reader, Writer = codecs.lookup("UTF-8")
    
    all_words=[];
    #string="";
    # get frequency distribution of new_data
    fdist = nltk.FreqDist(new_data)
    for k,v in fdist.items():
        # deal only if its frequency is > feature_frequency
        if(v>feature_frequency):
            #print (k,v)
            
            # remove unnecessary charachters below
            k = re.sub(",", "", str(k))
            k = re.sub("'", "", str(k))
            k = re.sub("\(", "", str(k))
            k = re.sub("\)", "", str(k))
            # append them to all_words
            all_words.append(k);
            
    #print(all_words);
    
    # remove stop words from the above created list.
    from stop_word_removal import stop_words_removal
    data2=stop_words_removal(all_words)
    #features=data2.split(" ",2)
    features_string = str(data2);
    new_features = nltk.word_tokenize(features_string)
    #print("features are :: "+str(new_features))
    #print("ngrams are ::"+str(data))
    
    
    potential_features=[];
                       
    for j in range(0,len(new_features)):
        if(new_features[j]!=''):
            if(str(data).find(new_features[j])>0):
                potential_features.append(new_features[j]);
                #print("feature found"+new_features[j])
        # Maximum size - The last item resides at x-1
        #print(data);
    

    return potential_features