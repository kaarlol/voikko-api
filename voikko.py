#!/usr/bin/env python
# -*- coding: utf-8 -*-
import libvoikko, codecs
from nltk.tokenize import word_tokenize

v = libvoikko.Voikko(u"fi")

def lemmatisoi( text_input ):
    lemmas = []
    for word in word_tokenize( text_input ):

        if (v.analyze(word)):
            lemmas.append(v.analyze(word)[0]['BASEFORM'])
        else:
            lemmas.append(word)

    return' '.join(lemmas)
