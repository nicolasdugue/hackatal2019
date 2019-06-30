#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 15:17:26 2019

@author: dugue
"""
fichier = open("GDN_pos_filtered.txt.tt")
res = open("GDN_pos_filtered.txt","w")

def translate_pos(pos):
    if pos == "ADV":
        return "adv"
    elif "VER" in pos:
        return "v"
    elif pos == "INT":
        return "i"
    elif pos == "NOM":
        return "n"
    elif pos == "ADJ":
        return "a"
    return "n"
for ligne in fichier:
    tab=ligne.split("\t")
    if tab[1] == "SENT":
        res.write(".\n")
    else:
        res.write(tab[2].strip()+"_"+translate_pos(tab[1])+" ")
res.close()
        
    
