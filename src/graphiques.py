import matplotlib.pyplot as plt

# Les campagnes se font sur 14 jours et il y a 7 campagnes
y = [1, 2, 3, 4, 5, 6, 7]

# aleatoire vs aleatoire
AVA1 = [21, 20, 20, 20, 21, 23, 19]
AVA2 = [24, 21, 22, 22, 24, 19, 23]
plt.plot(y, AVA1, label = "Aléatoire")
plt.plot(y, AVA2, label = "Aléatoire")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Aléatoire VS aléatoire")
plt.savefig("../docs/resultats/aleatoireVSaleatoire.jpg")
plt.show()

# aleatoire vs tetu
AVT1 = [19, 22, 17, 33, 26, 24, 22]
AVT2 = [17, 20, 25, 15, 21, 19, 24]
plt.plot(y, AVT1, label = "Aléatoire")
plt.plot(y, AVT2, label = "Tetu")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Aléatoire VS Tétu")
plt.savefig("../docs/resultats/aleatoireVStetu.jpg")
plt.show()

# aleatoire vs stochastique
AVS1 = [22, 21, 26, 19, 20, 21, 21]
AVS2 = [24, 23, 20, 26, 25, 21, 22]
plt.plot(y, AVS1, label = "Aléatoire")
plt.plot(y, AVS2, label = "Stochastique")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Aléatoire VS Stochastique")
plt.savefig("../docs/resultats/aleatoireVSstochastique.jpg")
plt.show()

# aleatoire vs meilleure reponse
AVMR1 = [27, 27, 21, 25, 21, 26, 24]
AVMR2 = [31, 31, 34, 33, 35, 30, 29]
plt.plot(y, AVMR1, label = "Aléatoire")
plt.plot(y, AVMR2, label = "Meilleure réponse")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Aléatoire VS Meilleure réponse")
plt.savefig("../docs/resultats/aleatoireVSmr.jpg")
plt.show()

# aleatoire vs fictitious play
AVF1 = [20, 20, 23, 25, 23, 19, 23]
AVF2 = [22, 23, 22, 24, 19, 22, 23]
plt.plot(y, AVF1, label = "Aléatoire")
plt.plot(y, AVF2, label = "Fictitious play")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Aléatoire VS Fictitious play")
plt.savefig("../docs/resultats/aleatoireVSfictitious.jpg")
plt.show()


# tetu vs tetu
TVT1 = [14, 28, 14, 14, 14, 0, 14]
TVT2 = [14, 28, 14, 14, 28, 0, 14]
plt.plot(y, TVT1, label = "Tétu")
plt.plot(y, TVT2, label = "Tétu")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Tétu VS Tétu")
plt.savefig("../docs/resultats/tetuVStetu.jpg")
plt.show()

# tetu vs stochastique
TVS1 = [28, 17, 14, 14, 16, 14, 15]
TVS2 = [28, 28, 28, 28, 26, 28, 26]
plt.plot(y, TVS1, label = "Tétu")
plt.plot(y, TVS2, label = "Stochastique")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Tétu VS Stochastique")
plt.savefig("../docs/resultats/tetuVSstochastique.jpg")
plt.show()

# tetu vs meilleure reponse
TVMR1 = [14, 28, 15, 27, 28, 14, 27]
TVMR2 = [40, 41, 54, 40, 41, 54, 41]
plt.plot(y, TVMR1, label = "Tétu")
plt.plot(y, TVMR2, label = "Meilleure réponse")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Tétu VS Meilleure réponse")
plt.savefig("../docs/resultats/tetuVSmr.jpg")
plt.show()

# tetu vs fictitious play
TVF1 = [28, 15, 14, 14, 15, 14, 15]
TVF2 = [27, 28, 15, 19, 27, 28, 41]
plt.plot(y, TVF1, label = "Tétu")
plt.plot(y, TVF2, label = "Fictitious play")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Tétu VS Fictitious play")
plt.savefig("../docs/resultats/tetuVSfictitious.jpg")
plt.show()


# stochastique vs stochastique
SVS1 = [18, 17, 17, 20, 19, 19, 18]
SVS2 = [20, 18, 15, 18, 21, 18, 21]
plt.plot(y, SVS1, label = "Stochastique")
plt.plot(y, SVS2, label = "Stochastique")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Stochastique VS Stochastique")
plt.savefig("../docs/resultats/stochastiqueVSstochastique.jpg")
plt.show()

# stochastique vs meilleure reponse
SVMR1 = [28, 25, 24, 28, 24, 28, 25]
SVMR2 = [34, 35, 33, 34, 31, 31, 33]
plt.plot(y, SVMR1, label = "Stochastique")
plt.plot(y, SVMR2, label = "Meilleure réponse")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Stochastique VS Meilleure réponse")
plt.savefig("../docs/resultats/stochastiqueVSmr.jpg")
plt.show()

# stochastique vs fictitious play
SVF1 = [21, 21, 25, 22, 24, 25, 22]
SVF2 = [23, 22, 23, 26, 23, 19, 20]
plt.plot(y, SVF1, label = "Stochastique")
plt.plot(y, SVF2, label = "Fictitious play")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Stochastique VS Fictitious play")
plt.savefig("../docs/resultats/stochastiqueVSfictitious.jpg")
plt.show()


# meilleure reponse vs meilleure reponse
MRVMR1 = [2, 5, 3, 4, 4, 6, 5]
MRVMR2 = [2, 6, 2, 4, 3, 5, 6]
plt.plot(y, MRVMR1, label = "Meilleure réponse")
plt.plot(y, MRVMR2, label = "Meilleure réponse")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Meilleure réponse VS Meilleure réponse")
plt.savefig("../docs/resultats/mrVSmr.jpg")
plt.show()

# meilleure reponse vs fictitious play
MRVF1 = [18, 19, 19, 18, 18, 20, 18]
MRVF2 = [48, 49, 48, 50, 50, 49, 50]
plt.plot(y, SVF1, label = "Meilleure réponse")
plt.plot(y, SVF2, label = "Fictitious play")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Meilleure réponse VS Fictitious play")
plt.savefig("../docs/resultats/mrVSfictitious.jpg")
plt.show()


# fictitious play vs fictitious play
FVF1 = [20, 24, 21, 22, 22, 22, 17]
FVF2 = [17, 27, 28, 16, 20, 20, 25]
plt.plot(y, FVF1, label = "Fictitious play")
plt.plot(y, FVF2, label = "Fictitious play")
plt.legend(loc = "upper left")
plt.xlabel("Numéro de campagne")
plt.ylabel("Nombre d'électeurs récoltés")
plt.title("Fictitious play VS Fictitious play")
plt.savefig("../docs/resultats/fictitiousVSfictitious.jpg")
plt.show()