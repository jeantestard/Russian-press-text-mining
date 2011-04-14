import sys, string, re


file = sys.argv[1]
req = sys.argv[2]
tailleContexte = int( sys.argv[3] )

a = open(file)
text = a.read() 
a.close()

mots = text.split()
requete = re.compile(req, re.IGNORECASE)

for index in range( len(mots) ):
    if requete.match( mots[index] ):
        debut = max(0, index-tailleContexte)
        fin = min(len(mots), index+tailleContexte+1)
        gauche = string.join( mots[debut:index] )
        droite = string.join( mots[index+1:fin] )
        print "%s [%s] %s" % (gauche, mots[index], droite)
