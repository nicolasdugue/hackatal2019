# -*- coding: utf-8 -*-

fichier=open("distribution_gdn_sorted.txt")
dico=set()
for ligne in fichier:
    tab=ligne.split(" ")
    if int(tab[1].strip()) > 500:
        dico.add(tab[0].strip())
fichier.close()

fichier=open("frwac_common_sorted.txt")
fichier_res=open("frwac_common_sorted_filtered.txt","w")
for ligne in fichier:
    tab=ligne.split(" ")
    if tab[0].strip() in dico:
        fichier_res.write(ligne)
fichier_res.close()
fichier.close()

fichier=open("gdn_common_sorted.txt")
fichier_res=open("gdn_common_sorted_filtered.txt","w")
for ligne in fichier:
    tab=ligne.split(" ")
    if tab[0].strip() in dico:
        fichier_res.write(ligne)
fichier_res.close()
fichier.close()


fichier=open("distribution_gdn_sorted.txt")
dico=set()
for ligne in fichier:
    tab=ligne.split(" ")
    if int(tab[1].strip()) > 5000:
        dico.add(tab[0].strip())
fichier.close()

fichier=open("frwac_common_sorted.txt")
fichier_res=open("frwac_common_sorted_Uberfiltered.txt","w")
for ligne in fichier:
    tab=ligne.split(" ")
    if tab[0].strip() in dico:
        fichier_res.write(ligne)
fichier_res.close()
fichier.close()

fichier=open("gdn_common_sorted.txt")
fichier_res=open("gdn_common_sorted_Uberfiltered.txt","w")
for ligne in fichier:
    tab=ligne.split(" ")
    if tab[0].strip() in dico:
        fichier_res.write(ligne)
fichier_res.close()
fichier.close()

fichier=open("distribution_gdn_sorted.txt")
dico=set()
for ligne in fichier:
    tab=ligne.split(" ")
    if int(tab[1].strip()) > 100:
        dico.add(tab[0].strip())
fichier.close()

fichier=open("frwac_common_sorted.txt")
fichier_res=open("frwac_common_sorted_Lowfiltered.txt","w")
for ligne in fichier:
    tab=ligne.split(" ")
    if tab[0].strip() in dico:
        fichier_res.write(ligne)
fichier_res.close()
fichier.close()

fichier=open("gdn_common_sorted.txt")
fichier_res=open("gdn_common_sorted_Lowfiltered.txt","w")
for ligne in fichier:
    tab=ligne.split(" ")
    if tab[0].strip() in dico:
        fichier_res.write(ligne)
fichier_res.close()
fichier.close()