#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import libvoikko, codecs
from nltk.tokenize import word_tokenize

v = libvoikko.Voikko(u"fi")

infile = codecs.open('test.txt', 'r',"utf-8")
outfile = codecs.open("lol.txt", "w", "utf-8")
for line in infile:
#    print line
    lemmas = []
    for word in word_tokenize(line):         
#        print v.analyze(word)
        if (v.analyze(word)):
            lemmas.append(v.analyze(word)[0]['BASEFORM'])
        else:
            lemmas.append(word)
    outfile.write(' '.join(lemmas)+"\n")    
outfile.close()
