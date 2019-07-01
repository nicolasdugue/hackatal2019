# Hackatal 2019 : équipe Karaoké

## Participants

- Adrien Bardet
- Nicolas Dugué
- Loïc Grobol

## Etude Embeddings -> Dossier EtudeEmbeddings

L'objectif est de comparer les représentations apprises sur un corpus dit "neutre", i.e. non connoté politiquement, le corpus frWac (wikipedia) avec des embeddings appris sur le corpus du grand débat national GDN). L'hypothèse, c'est que le contexte spécifique du GDN doit amener à des représentations très différentes de celle du corpus neutre, marquées par des contextes liés aux sujets du GDN mais également à l'époque dans laquelle s'ancre le GDN [#exemple]. Pour cela, nous considérons des embeddings qui sont préappris avec Word2vec sur le corpus frWac (wikipedia) et qui sont ceux disponibles en ligne sur le site de Jean-Philippe Fauconnier [https://fauconnier.github.io/#data]. Ils sont appris avec cbow et de dimension 700. Nous avons choisi des embeddings appris sur des lemmes.

Pour notre étude, nous conservons uniquement les catégories les plus porteuses de sens, i.e., les verbes, les noms, mais également les déterminants, adjectifs et interjections (qui peuvent servir à qualifier noms et verbes, et qui doivent par ailleurs être pour la plupart invariants d'un corpus à l'autre, ils offrent donc un point de comparaison).
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

#### Exemples intéressants

- manifester_v
- grenade_n
- gauche_n
- insoumis_a
- monarque_n
- évasion_n
- maçonnique_a
- fonctionnaire_n
- patriote_a
- laïcité_n
- féministe_a
- mariage_n
- famille_n

### Procruste

Afin de comparer les représentations pré-apprises sur le corpus wikipedia, et celles apprises sur le corpus du grand débat national (gdn), nous souhaitons tenter l'alignement des deux espaces via un procruste afin ensuite d'analyser les vecteurs qui divergent le plus une fois projetés dans le même espace.

Afin que l'alignement des deux espaces soit exploitable, il s'agit de n'aligner que du vocabulaire dont les représentations sont proches dans les deux corpus (wikipedia et gdn). Nous faisons l'hypothèse que c'est le cas pour les mots les plus fréquents, et nous réalisons donc l'alignement uniquement sur ce sous-ensemble du vocabulaire.

Nous exploitons donc les résultats données par *distrib.py* qui a calculé la fréquence de notre vocabulaire dans le fichier **GDN_pos_filtered.txt** et stocké le résultat dans **distribution_gdn_sorted.txt**. Nous utilisons ensuite **filter_matrix_for_procruste.py** afin de créer les fichiers *frwac_common_sorted_filtered.txt* et *gdn_common_sorted_filtered.txt* qui contiennent uniquement les vecteurs des mots présents plus de **500** fois dans le corpus du GDN : 

	$ wc -l frwac_common_sorted_filtered.txt 
	3105 frwac_common_sorted_filtered.txt

Le script crée également les fichiers *frwac_common_sorted_Uberfiltered.txt* et *gdn_common_sorted_Uberfiltered.txt* qui contiennent uniquement les vecteurs des mots présents plus de **5000** fois dans le corpus du GDN : 

	$ wc -l frwac_common_sorted_Uberfiltered.txt 
	615 frwac_common_sorted_Uberfiltered.txt
	
Enfin, le script crée les fichiers *frwac_common_sorted_Lowfiltered.txt* et *gdn_common_sorted_Lowfiltered.txt* qui contiennent uniquement les vecteurs des mots présents plus de **100** fois dans le corpus du GDN : 

	wc -l frwac_common_sorted_Lowfiltered.txt 
	6675 frwac_common_sorted_Lowfiltered.txt
	
Le procruste peut être appris par exemple sur la matrice *Uberfiltered* puis être exploité sur les matrices moins filtrées.


## Dépendances: 

 
* Convertvec: 	https://github.com/marekrei/convertvec  
* Moses :	https://github.com/moses-smt/mosesdecoder  
* NmtpyTorch:	https://github.com/lium-lst/nmtpytorch  
