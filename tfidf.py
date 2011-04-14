#!/usr/bin/env python
#


import math
from operator import itemgetter
import sys, string, re

def freq(mot, document):
  return document.split(None).count(mot)

def motFrequence(document):
  return len(document.split(None))

def frequenceDocsContenant(mot,listeDocuments):
  frequence = 0
  for document in listeDocuments:
    if freq(mot,document) > 0:
      frequence += 1
  return frequence

def tf(mot, document):
  return (freq(mot,document) / float(motFrequence(document)))

def idf(mot, listeDocuments):
  return math.log(len(listeDocuments) / frequenceDocsContenant(mot,listeDocuments))

def tfidf(mot, document, listeDocuments):
  return (tf(mot,document) * idf(mot,listeDocuments))

if __name__ == '__main__':
  listeDocuments = []
  a = open("Documents/textstatistics/2008/cegodnia.txt")
  text1 = a.read() 
  a.close()
  a = open("Documents/textstatistics/2008/ferghana.txt")
  text2 = a.read()
  a.close()
  a = open("Documents/textstatistics/2008/gazieta.txt")
  text3 = a.read()
  a.close()
  a = open("Documents/textstatistics/2008/kommersant.txt")
  text4 = a.read()
  a.close()
  a = open("Documents/textstatistics/2008/literaturnaia.txt")
  text5 = a.read()
  a.close()
  a = open("Documents/textstatistics/2008/novaiaGazieta.txt")
  text6 = a.read()
  a.close()
  a = open("Documents/textstatistics/2008/novIsvestia.txt")
  text7 = a.read()
  a.close()
  listeDocuments.append(text2)
  listeDocuments.append(text3)
  listeDocuments.append(text4)
  listeDocuments.append(text5)
  listeDocuments.append(text6)
  listeDocuments.append(text7)
  listeDocuments.append(text1)




  mots = {}
  documentNum = 0
  for mot in listeDocuments[documentNum].split(None):
    mots[mot] = tfidf(mot,listeDocuments[documentNum],listeDocuments)
  for item in sorted(mots.items(), key=itemgetter(1), reverse=True):
    print "%f <= %s" % (item[1], item[0])