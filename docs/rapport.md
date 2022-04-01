# Rapport de projet

## Groupe
* Hebert Thomas


## Description des choix importants d'implémentation

Le fichier main permet de lancer le jeu et de calculer les résultats. Toutes les fonctions de stratégies se trouvent dans le fichier withoutBudget.py.

La première structure de données importante est le dictionnaire LP. Il est commun à toutes les fonctions et va stocker pour chaque indice de militant, qui sont les clés, un tuple composé du chemin à parcourir dans la journée et de l'indice de l'électeur qu'il vise. Ce dernier permet de vérifier qu'il a bien atteint son but.

Les fonctions aleatoire et tetu sont quasiment identiques à la différence que tetu récupère le dictionnaire des chemins LP pour être sûr de garder les mêmes électeurs tout du long.

La fonction stochastique va récupérer les k premières (j'ai placé k = 15 pour les tests) stratégies pertinentes. La pertinence ici correspond à avoir au moins 1 militant sur au moins 3 électeurs différents. Ces stratégies sont ensuite assignées à des probabilités, fixées à 0.5 au départ. Le coup choisi est celui dont la probabilité est la plus élevée, ou aléatoirement si elles sont toutes égales. Si le dernier coup joué est victorieux, la probabilité de ce dernier augmente de 0.25, et baisse de 0.25 en cas de défaite ou égalité. Pour stocker tout cela, j'utilise un dictionnaire lStoch dont les clés sont les tuples des coups et les valeurs la probabilité associée.

La fonction MR (meilleure réponse) va jouer une meilleure réponse au coup précédent de l'adversaire. Pour cela, on augmente chaque valeur de ce coup de 1 et on retranche les militants en trop en parant de la gauche. Cela assure d'avoir le même nombre d'électeurs que le coup précédent de l'adversaire, mais surtout d'avoir le plus souvent un électeur de plus. Pour cela je n'ai juste qu'à gérer une liste d'entiers représentant la répartition des militants sur les électeurs, d'ajouter 1 à chaque valeur et de soustraire les militants en trop à partir de la gauche.

La fonction fictitious va jouer en meilleure réponse pour l'utilité espérée selon la fréquence observée des stratégies de l'autre parti. Pour cela on utilise un tableau de gains entre tous les coups possibles et les coups de l'adversaire. Pour cela j'ai codé une fonction genereStrats qui va générer toutes les coups possibles avec pour longueur le nombre d'électeurs et dont le total des valeurs ne peut dépasser le nombre de militants. Je calcule ensuite le gain associé entre un coup et celui de l'adversaire avec la fonction gagnant qui va me renvoyer le nombre d'électeurs gagnés avec ce coup face à l'adversaire. Je stocke ensuite le tableau de probabilités avec un dictionnaire FPAdvers dont les clés sont les tuples des coups que l'adversaire a joué jusqu'à présent et les valeurs sont des listes qui contiennent le nombre d'occurence de la stratégie en clé et la probabilité que l'adversaire rejoue ce coup. A chaque appel, si l'adversaire joue un coup qui n'est pas dans le dictionnaire, il est ajouté avec une occurence de 1, sinon son occurence est incrémentée de 1. Ensuite toutes les probabilités sont recalculées. Pour choisir le coup à jouer, il faut calculer l'espérance de chaque coup possible : c'est une somme des multiplications entre le gain et la probabilité d'apparition du coup adverse parcouru. On choisi donc celui qui a l'espérance la plus élevée.

La fonction main va lancer le programme principal. Le premier argument renseigne le nombre d'itérations max par jour, le 2e la stratégie du parti 1 et le 3e la stratégie du parti 2. Pour les stratégies il faut écrire aleatoire, tetu, stochastique, mr ou fictitious.
Exemple : pyt=thon3 main.py 100 aleatoire fictitious

## Description des résultats

Tous les tests ont été réalisés sur 7 campagnes, chacune de 14 jours. Le k utilisé pour la fonction stochastique est de 15.
### Fonction aléatoire

Quand on la compare à elle-même, la fonction aléatoire ne produit pas de résultat probant, de par sa nature. Aucun parti ne peut véritablement gagner de façon certaine.

![aleatoire vs aleatoire](/docs/resultats/aleatoireVSaleatoire.jpg "Aléatoire VS aléatoire")

Si on confronte aléatoire et tétu, on remarque que les victoires de ce dernier dépend beaucoup du premier choix de stratégie le premier jour. S'il choisi une stratégie pertinente, il aura de grandes chances de gagner mais s'il choisi une stratégie inutile comme [0,0,0,0,7] par exemple, ses chances de gagner sont quasi nulles.

![aleatoire vs tetu](/docs/resultats/aleatoireVStetu.jpg "Aléatoire VS Tétu")

Stochastique obtient de bonnes performances face à aléatoire mais la nature de ce dernier fait qu'il ne peut pas prédire à 100% une stratégie gagnante parmi toutes celles pertinentes.

![aleatoire vs stochastique](/docs/resultats/aleatoireVSstochastique.jpg "Aléatoire VS Stochastique")

Meilleure réponse surpasse sans nul doute aléatoire sur chaque campagne. Comme il aura toujours tendence à choisir une stratégie parmi les meilleures, aléatoire e peut pas rivaliser vu le nombres de stratégies non pertinentes possibles.

![aleatoire vs mr](/docs/resultats/aleatoireVSmr.jpg "Aléatoire VS Meilleure réponse")

Etrangement, fictitious play ne va pas gagner à tous les coups face à aléatoire. Cela est sûrement du au caractère imprévisible d'aléatoire qui va noyer les probabilités de fictitious, ce dernier aura donc du mal à costamment trouver la meilleure réponse.

![aleatoire vs fictitious](/docs/resultats/aleatoireVSfictitious.jpg "Aléatoire VS Fictitious play")

### Fonction tétu

Face à lui-même, encore une fois tout dépend du premier jour. Si l'un des 2 partis prend l'avantage ce jour là, il le gardera pour le reste de la campagne.

![tetu vs tetu](/docs/resultats/tetuVStetu.jpg "Tétu VS Tétu")

Grâce à la ature statique de tétu, stochastique va pouvoir constamment prévoir le meilleur coup à jouer et ainsi ne jamais perdre.

![tetu vs stochastique](/docs/resultats/tetuVSstochastique.jpg "Tétu VS Stochastique")

Même cas que précédemment, meilleure réponse va constamment prévoir le meilleur coup que tétu car ce dernier ne change jamais.

![tetu vs mr](/docs/resultats/tetuVSmr.jpg "Tétu VS Meilleure réponse")

Face à fictitious, tétu ne fait pas le poids non plus. A force de jouer le même coup, fictitious aura une probabilité quasiment max sur le coup de tétu, menant à une défaite inévitable de ce dernier.

![tetu vs fictitious](/docs/resultats/tetuVSfictitious.jpg "Tétu VS Fictitious play")

### Fonction stochastique

Face à lui-même, c'est ici celui qui aura le plus de chance dans les stratégies pertinentes choisies. Globalement ils sont quasiment tout le temps très proches sur les résultats, et ils s'échangent les victoires.

![stochastique vs stochastique](/docs/resultats/stochastiqueVSstochastique.jpg "Stochastique VS Stochastique")

L'efficacité de stochastique est très inférieure à celle de meilleure réponse. Ce dernier s'adapte vite et si jamais stochastique rejoue des coups identiques a des jours précédents il sera désavantagé.

![stochastique vs mr](/docs/resultats/stochastiqueVSmr.jpg "Stochastique VS Meilleure réponse")

Fictitious a souvent l'avantage sur stochastique. Son système de probabilités est plus élaboré et plus la campagne a de jours, plus il aura répertorié tous les coups possibles de stochastiques pour des probabilités plus précises.

![stochastique vs fictitious](/docs/resultats/stochastiqueVSfictitious.jpg "Stochastique VS Fictitious play")

### Fonction MR (Meilleure Réponse)

Contre lui-même, meilleure réponse a environ 50% de chances de gagner. Chacun s'adapte à l'autre, ce qui cause une alternance des victoires, autant sur les jours que sur différentes campagnes.

![mr vs mr](/docs/resultats/mrVSmr.jpg "Meilleure réponse VS Meilleure réponse")

Difficile de trouver une constance entre meilleure réponse et fictitious. Chacun essaie de prédire l'autre mais la nature changeante de meilleure réponse peut noyer en quelque sorte les probabilités de fictitious avec un grand nombre de coups différents.

![mr vs fictitious](/docs/resultats/mrVSfictitious.jpg "Meilleure réponse VS Fictitious play")

### Fonction fictitious

La dernière comparaison à parcourir est fictitious avec lui-même. Comme prévu, les 2 s'annulent entre eux, causant là encore une alternance de victoires sur les jours et les campagnes.

![fictitious vs fictitious](/docs/resultats/fictitiousVSfictitious.jpg "Fictitious play VS Fictitious play")

### Budget de déplacement

Je n'ai malheureusement pas eu le temps d'implémenter les 2 versions de budget de déplacement.

