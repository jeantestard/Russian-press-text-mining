import sys, string, re


thesaurus = sys.argv[1]
corpus = sys.argv[2]

a = open(corpus)
text = string.split( a.read() ) 
a.close()

a = open(thesaurus)
lines = a.readlines()
a.close()

dic = {}
scores = {}


categorie = "Defaut"
scores[categorie] = 0


for line in lines:
    if line[0:2] == '>>':
        categorie = string.strip( line[2:] )
        scores[categorie] = 0
    else:
        line = line.strip()
        if len(line) > 0:
            lexeme = re.compile(line, re.IGNORECASE)
            dic[lexeme] = categorie


for token in text:
    for lexeme in dic.keys():
        if lexeme.match( token ):
            categ = dic[lexeme]
            scores[categ] = scores[categ] + 1

for key in scores.keys():
    print key, ":", scores[key] 
