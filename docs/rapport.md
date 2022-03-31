# Rapport de projet

## Groupe
* Hebert Thomas


## Description des choix importants d'implémentation

Le fichier main permet de lancer le jeu et de calculer les résultats. Toutes les fonctions de stratégies se trouvent dans le fichier withoutBudget.py.

La première structure de données importante est le dictionnaire LP. Il est commun à toutes les fonctions et va stocker pour chaque indice de militant, qui sont les clés, un tuple composé du chemin à parcourir dans la journée et de l'indice de l'électeur qu'il vise. Ce dernier permet de vérifier qu'il a bien atteint son but.

Les fonctions aleatoire et tetu sont quasiment identiques à la différence que tetu récupère le dictionnaire des chemins LP pour être sûr de garder les mêmes électeurs tout du long.

La fonction stochastique va récupérer les k premières (j'ai placé k = 15 pour les tests) stratégies pertinentes. La pertinence ici correspond à avoir au moins 1 militant sur au moins 3 électeurs différents. ces stratégies sont ensuite assignées à des probabilités, fixées à 0.5 au départ. Le coup choisi est celui dont la probabilité est la plus élevée, ou aléatoirement si elles sont toutes égales. Si le dernier coup joué est victorieux, la probabilité de ce dernier augmente de 0.25, et baisse de 0.25 en cas de défaite ou égalité. Pour stocker tout cela, j'utilise un dictionnaire lStoch dont les clés sont les tuples des coups et les valeurs la probabilité associée.

La fonction MR (meilleure réponse) va jouer une meilleure réponse au coup précédent de l'adversaire. Pour cela, on augmente chaque valeur de ce coup de 1 et on retranche les militants en trop en parant de la gauche. Cela assure d'avoir le même nombre d'électeurs que le coup précédent de l'adversaire, mais surtout d'avoir le plus souvent un électeur de plus. Pour cela je n'ai juste qu'à gérer une liste d'entiers représentant la répartition des militants sur les électeurs, d'ajouter 1 à chaque valeur et de soustraire les militants en trop à partir de la gauche.

La fonction fictitious va jouer en meilleure réponse pour l'utilité espérée selon la fréquence observée des stratégies de l'autre parti. Pour cela on utilise un tableau de gains entre tous les coups possibles et les coups de l'adversaire. Pour cela j'ai codé une fonction genereStrats qui va générer toutes les coups possibles avec pour longueur le nombre d'électeurs et dont le total des valeurs ne peut dépasser le nombre de militants. Je calcule ensuite le gain associé entre un coup et celui de l'adversaire avec la fonction gagnant qui va me renvoyer le nombre d'électeurs gagnés avec ce coup face à l'adversaire. Je stocke ensuite le tableau de probabilités avec un dictionnaire FPAdvers dont les clés sont les tuples des coups que l'adversaire a joué jusqu'à présent et les valeurs sont des listes qui contiennent le nombre d'occurence de la stratégie en clé et la probabilité que l'adversaire rejoue ce coup. A chaque appel, si l'adversaire joue un coup qui n'est pas dans le dictionnaire, il est ajouté avec une occurence de 1, sinon son occurence est incrémentée de 1. Ensuite toutes les probabilités sont recalculées. Pour choisir le coup à jouer, il faut calculer l'espérance de chaque coup possible : c'est une somme des multiplications entre le gain et la probabilité d'apparition du coup adverse parcouru. On choisi donc celui qui a l'espérance la plus élevée.

## Description des résultats

![aleatoire vs aleatoire](/docs/resultats/101328.png "Aléatoire VS aléatoire")
