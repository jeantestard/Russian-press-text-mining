

import logging, gensim, bz2, codecs, re
from gensim import corpora, models, similarities

documents = [open("/workspace/corpus/novIsvestia.txt").read(),
             open("/workspace/corpus/cegodnia.txt").read(),
             open("/workspace/corpus/kommersant.txt").read(),
             open("/workspace/corpus/novaiaGazieta.txt").read(),
             open("/workspace/corpus/literaturnaia.txt").read(),
             open("/workspace/corpus/gazieta.txt").read(),
             open("/workspace/corpus/ferghana.txt").read()]

liste = codecs.open("/workspace/lsi/src/stoplist","r","utf-8").read()
stoplist = set(re.compile("\s").split(liste))
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in documents]


allTokens = sum(texts, [])
tokensOnce = set(word for word in set(allTokens) if allTokens.count(word) == 1)
texts = [[word for word in text if word not in tokensOnce]
          for text in texts]


dictionary = corpora.Dictionary(texts)
dictionary.save('/workspace/lsi/src/dic.dict') 
print dictionary


corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.saveCorpus('/workspace/lsi/src/corpus.mm', corpus)



corpus = corpora.MmCorpus('/workspace/lsi/src/corpus.mm')
print corpus

lsi = models.LsiModel(corpus, numTopics=200)


index = similarities.MatrixSimilarity(lsi[corpus])



doc = open("/workspace/lsi/src/requete").read()
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow] 



sims = index[lsi[vec_lsi]]
sims = sorted(enumerate(sims), key = lambda item: -item[1])
print sims