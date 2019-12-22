# Urdu Tokenizer :
#    The purpose of Urdu Tokenizer is to do segmentation of Urdu data so that
#    data can be manipulated for the statistical analysis
# Author  : Syed Awais Kazmi
# COMSATS : SP15-R01-009   

import re, codecs
Encode, Decode, Reader, Writer = codecs.lookup("UTF-8")


def urdu_tokenizer(segment):
    
        # Removes each symbol given below using Regular Expression
        
        segment = re.sub(",", " , ", segment)
        segment = re.sub("\.", " . ", segment)
        segment = re.sub("\|", " | ", segment)
        segment = re.sub("-", " - ", segment)
        segment = re.sub("\?", " ? ", segment)
        segment = re.sub("!", " ! ", segment)
        segment = re.sub("\"", " \" ", segment)
        segment = re.sub("\'", " ' ", segment)
        segment = re.sub("\(", " ( ", segment)
        segment = re.sub("\)", " ) ", segment)
        segment = re.sub("\{", " { ", segment)
        segment = re.sub("\{", " } ", segment)
        segment = re.sub("\<", " < ", segment)
        segment = re.sub("\>", " > ", segment)
        segment = re.sub("\;", " ; ", segment)
        segment = re.sub("\:", " : ", segment)
        segment = re.sub(u"\u0964", " "+u"\u0964"+" ", segment)
        segment = re.sub(u"\u0965", " "+u"\u0965"+" ", segment)
        segment = re.sub(u"\u09F7", " "+u"\u09F7"+" ", segment)
        segment = re.sub(u"\u09FB", " "+u"\u09FB"+" ", segment)
        segment = re.sub("\s+", " ", segment)
        segment = re.sub("&amp ;", "&amp;", segment)
        segment = re.sub("&quot ;", "&quot;", segment)
        segment = re.sub("&quote ;", "&quote;", segment)                
        
        # Now Split the segments and make a list of words
        tokens = segment.split()
        return tokens

