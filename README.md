# Hackatal 2019 : équipe Karaoké

## Participants

- Adrien Bardet
- Nicolas Dugué
- Loïc Grobol

## Etude Embeddings -> Dossier EtudeEmbeddings

L'objectif est de comparer les représentations apprises sur un corpus dit "neutre", i.e. non connoté politiquement, le corpus frWac (wikipedia). 
Ces embeddings sont préappris avec Word2vec et sont ceux disponibles en ligne sur le site de Jean-Philippe Fauconnier [https://fauconnier.github.io/#data]. Ils sont appris avec cbow et de dimension 700.
Nous avons choisi des embeddings appris sur des lemmes.

Pour notre étude, nous conservons uniquement les catégories les plus porteuses de sens, i.e., les verbes, les noms, mais également les déterminants, adjectifs et interjections (qui peuvent servir à qualifier noms et verbes).
Les étiquettes morpho-syntaxiques sont marquées ainsi : 
    
    manger_v
    pomme_n
    très_adv
    beau_a
    hé_i
    
Nous partons ensuite du corpus étiqueté morpho-syntaxiquement par Damien Nouvel [http://damien.nouvels.net/fr/debats2019]. Nous utilisons le fichier suivant :
    
    > head GDN.txt.tt 
    Afin	KON	afin
    d'	PRP	de
    éviter	VER:infi	éviter
    de	PRP	de
    creuser	VER:infi	creuser
    les	DET:ART	le
    inégalités	NOM	inégalité
    ne	ADV	ne
    plus	ADV	plus
    augmenter	VER:infi	augmenter
    
Nous conservons uniquement les POS qui nous intéressent :

    cat GDN.txt.tt | awk 'NF==3 {print}{}' | awk '/(VER.+|NOM|ADJ|ADV|INT|SENT)/' >> GDN_pos_filtered.txt.tt

Puis nous créons un fichier du grand débat phrase par phrase en utilisant uniquement les termes que nous considérons avec le fichier *lemme_to_txt.py* : le résultat est **GDN_pos_filtered.txt**.
Nous passons ensuite word2vec sur ce dernier pour obtenir nos embeddings, semblables à ceux de frWac.

Pour conserver uniquement les vecteurs communs aux deux corpus, nous utilisons *common_embeddings.py* : **frwac_common_sorted.txt** et **gdn_common_sorted.txt** en sont les résultats.
Afin de ne pas considérer dans la suite un vocabulaire trop large, et surtout des mots dont la fréquence est faible dans le corpus du grand débat, nous utilisons *distrib.py* pour calculer la fréquence de notre vocabulaire dans le fichier **GDN_pos_filtered.txt**. Le résultat est stocké dans **distribution_gdn_sorted.txt**.

## Dépendances: 

 
* Convertvec: 	https://github.com/marekrei/convertvec  
* Moses :	https://github.com/moses-smt/mosesdecoder  
* NmtpyTorch:	https://github.com/lium-lst/nmtpytorch  
