# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:04:07 2017

@author: Awais
"""
from urdu_tokenizer import urdu_tokenizer
from task1_ import array_questions


def tokenize(data):
    tokens=urdu_tokenizer(data)
    return tokens

#print(tokenize("میرا نام کیا ہے۔"))