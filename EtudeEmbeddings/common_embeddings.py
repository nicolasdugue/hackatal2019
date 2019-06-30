# -*- coding: utf-8 -*-

frwac=open("frWac_postag_no_phrase_700_skip_cut50.txt")
gdn=open("gdn_postag_no_phrase_700_skip_cut50.txt")

frwacVoc=set()
gdnVoc=set()

for ligne in frwac:
    frwacVoc.add(ligne.split(" ")[0].strip())

for ligne in gdn:
    gdnVoc.add(ligne.split(" ")[0].strip())
    
intersection=frwacVoc.intersection(gdnVoc)

frwac_common=open("frwac_common.txt","w")
gdn_common=open("gdn_common.txt","w")

frwac.close()
gdn.close()
frwac=open("frWac_postag_no_phrase_700_skip_cut50.txt")
gdn=open("gdn_postag_no_phrase_700_skip_cut50.txt")

for ligne in frwac:
    if ligne.split(" ")[0].strip() in intersection:
        frwac_common.write(ligne)

for ligne in gdn:
    if ligne.split(" ")[0].strip() in intersection:
        gdn_common.write(ligne)
frwac_common.close()
gdn_common.close()

    