# -*- coding: utf-8 -*-

fichier=open("GDN_pos_filtered.txt")
dico=dict()
for ligne in fichier:
    words=ligne.split(" ")
    for w in words:
        if w not in dico:
            dico[w]=0
        dico[w]+=1

distribution=open("distribution_gdn.txt", "w")
for word in dico:
    distribution.write(word + " "+str(dico[word])+"\n")
distribution.close()