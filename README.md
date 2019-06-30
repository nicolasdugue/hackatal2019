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

### Exemples

#### Gilet GDN

	>>> from gensim.models import KeyedVectors
	>>> wv_from_text = KeyedVectors.load_word2vec_format('gdn_common_sorted.txt', binary=False)
	>>> wv_from_text.most_similar("gilet_n")
	[('jaune_a', 0.9214566946029663), ('jaune_n', 0.6313734650611877), ('enfiler_v', 0.5787583589553833), ('détonateur_n', 0.5656031370162964), ('jacquerie_n', 0.5498842000961304), ('pacifiste_a', 	0.5418269634246826), ('contestataire_n', 0.5362532734870911), ('étincelle_n', 0.5354418754577637), ('manif_n', 0.5342225432395935), ('chienlit_n', 0.5236349105834961)]

#### Gilet frWac

	>>> from gensim.models import KeyedVectors
	>>> wv_from_text = KeyedVectors.load_word2vec_format('frwac_common_sorted.txt'', binary=False)
	>>> wv_from_text.most_similar("gilet_n")
	[('veste_n', 0.7116566896438599), ('pantalon_n', 0.6993970274925232), ('pull_n', 0.6646631360054016), ('pare-balles_n', 0.6379226446151733), ('jupe_n', 0.6134262084960938), ('blouson_n', 		0.60909503698349), ('chemise_n', 0.5901532769203186), ('casquette_n', 0.5671770572662354), ('jupette_n', 0.5362040996551514), ('enfiler_v', 0.5351220369338989)]

## Dépendances: 

 
* Convertvec: 	https://github.com/marekrei/convertvec  
* Moses :	https://github.com/moses-smt/mosesdecoder  
* NmtpyTorch:	https://github.com/lium-lst/nmtpytorch  
