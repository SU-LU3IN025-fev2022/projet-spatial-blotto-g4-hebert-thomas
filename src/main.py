# -*- coding: utf-8 -*-

# Nicolas, 2021-03-05
from __future__ import absolute_import, print_function, unicode_literals

import random 
import numpy as np
import sys
from itertools import chain


import pygame

from pySpriteWorld.gameclass import Game,check_init_game_done
from pySpriteWorld.spritebuilder import SpriteBuilder
from pySpriteWorld.players import Player
from pySpriteWorld.sprite import MovingSprite
from pySpriteWorld.ontology import Ontology
import pySpriteWorld.glo

from search.grid2D import ProblemeGrid2D
from search import probleme
import withoutBudget
import copy



# ---- ---- ---- ---- ---- ----
# ---- Misc                ----
# ---- ---- ---- ---- ---- ----




# ---- ---- ---- ---- ---- ----
# ---- Main                ----
# ---- ---- ---- ---- ---- ----

game = Game()

def init(_boardname=None):
    global player,game
    name = _boardname if _boardname is not None else 'blottoMap'
    game = Game('./Cartes/' + name + '.json', SpriteBuilder)
    game.O = Ontology(True, 'SpriteSheet-32x32/tiny_spritesheet_ontology.csv')
    game.populate_sprite_names(game.O)
    game.fps = 20  # frames per second
    game.mainiteration()
    player = game.player
    
def main():

    #for arg in sys.argv:
    iterations = 100 # default
    if len(sys.argv) >= 2:
        iterations = int(sys.argv[1])
    # print ("Iterations: ")
    # print (iterations)
    
    init()
    
    p1 = sys.argv[2]
    if (p1.lower() == "stochastique"):
            k1 = 15
    p2 = sys.argv[3]
    if (p2.lower() == "stochastique"):
            k2 = 15
    

    
    #-------------------------------
    # Initialisation
    #-------------------------------
    
    nbLignes = game.spriteBuilder.rowsize
    nbCols = game.spriteBuilder.colsize
       
    # print("lignes", nbLignes)
    # print("colonnes", nbCols)
    
    
    players = [o for o in game.layers['joueur']]
    nbPlayers = len(players)
    #print("Trouvé ", nbPlayers, " militants")
    
       
           
    # on localise tous les états initiaux (loc du joueur)
    # positions initiales des joueurs
    initStates = [o.get_rowcol() for o in players]
    #print ("Init states:", initStates)
    
    # on localise tous les secteurs d'interet (les votants)
    # sur le layer ramassable
    goalStates = [o.get_rowcol() for o in game.layers['ramassable']]
    #print ("Goal states:", goalStates)
    
        
    # on localise tous les murs
    # sur le layer obstacle
    wallStates = [w.get_rowcol() for w in game.layers['obstacle']]
    #print ("Wall states:", wallStates)
    
    def legal_position(row,col):
        # une position legale est dans la carte et pas sur un mur
        return ((row,col) not in wallStates) and row>=0 and row<nbLignes and col>=0 and col<nbCols
    
    
    
        
    #-------------------------------
    # Attributaion aleatoire des fioles 
    #-------------------------------
    
    objectifs = goalStates
    random.shuffle(objectifs)
    
    g =np.ones((nbLignes,nbCols),dtype=bool)  # par defaut la matrice comprend des True  
    for w in wallStates:            # putting False for walls
        g[w]=False

    # initialisation du dico stochastique
    if p1.lower() == "stochastique":
        lStoch1 = dict()
    if p2.lower() == "stochastique":
        lStoch2 = dict()
    
    # initialisation de la liste de tous les coups possibles et du dico fictitious
    if p1.lower() == "fictitious":
        coupsPossibles1 = withoutBudget.genereStrats(len(initStates), len(objectifs))
        FPAdvers1 = dict()
    if p2.lower() == "fictitious":
        coupsPossibles2 = withoutBudget.genereStrats(len(initStates), len(objectifs))
        FPAdvers2 = dict()
    
    scoreC = (0,0)
    
    coup1 = []
    coup2 = []
    LP = dict()
    
    for d in range(14):
        
        scoreD = dict()
        for i in range(len(objectifs)):
            scoreD[i] = (0,0)
        
        coup1Old = copy.deepcopy(coup1)
        coup2Old = copy.deepcopy(coup2)
        
        # calcul du coup à jouer en fonction de la stratégie employée
        if d == 0:
            if p1.lower() != "stochastique":
                LP1, coup1 = withoutBudget.aleatoire(g, initStates, objectifs, 1)
            else:
                LP1, coup1 = withoutBudget.stochastique(g, initStates, objectifs, 1, k1, lStoch1, coup1Old, coup2Old)
            if p2.lower() != "stochastique":
                LP2, coup2 = withoutBudget.aleatoire(g, initStates, objectifs, 2)
            else:
                LP2, coup2 = withoutBudget.stochastique(g, initStates, objectifs, 2, k2, lStoch2, coup2Old, coup1Old)
            
            LP = LP1.copy()
            LP.update(LP2)
        
        else:
            if p1.lower() == "aleatoire":
                LP1, coup1 = withoutBudget.aleatoire(g, initStates, objectifs, 1)
            elif p1.lower() == "tetu":
                LP1, coup1 = withoutBudget.tetu(g, initStates, objectifs, LP, 1)
            elif p1.lower() == "stochastique":
                LP1, coup1 = withoutBudget.stochastique(g, initStates, objectifs, 1, k1, lStoch1, coup1Old, coup2Old)
            elif p1.lower() == "mr":
                LP1, coup1 = withoutBudget.MR(g, initStates, objectifs, 1, coup2Old)
            else:
                LP1, coup1 = withoutBudget.fictitious(g, initStates, objectifs, 1, coupsPossibles1, FPAdvers1, coup2Old)
            
            if p2.lower() == "aleatoire":
                LP2, coup2 = withoutBudget.aleatoire(g, initStates, objectifs, 2)
            elif p2.lower() == "tetu":
                LP2, coup2 = withoutBudget.tetu(g, initStates, objectifs, LP, 2)
            elif p2.lower() == "stochastique":
                LP2, coup2 = withoutBudget.stochastique(g, initStates, objectifs, 2, k2, lStoch2, coup2Old, coup1Old)
            elif p2.lower() == "mr":
                LP2, coup2 = withoutBudget.MR(g, initStates, objectifs, 2, coup1Old)
            else:
                LP2, coup2 = withoutBudget.fictitious(g, initStates, objectifs, 2, coupsPossibles2, FPAdvers2, coup1Old)
            
            LP = LP1.copy()
            LP.update(LP2)
        
        posPlayers = initStates
        Finished = []
        
        for i in range(iterations):
            if len(Finished) == len(LP):
                break;
            
            # déplacement des militants
            for j in LP:
                if j not in Finished:
                    path = (LP[j])[0]
                    row, col = path[i]
                    posPlayers[j] = (row, col)
                    players[j].set_rowcol(row, col)
                    elect = (LP[j])[1]
                    if (row, col) == objectifs[elect]:
                        Finished.append(j)
                        t1, t2 = scoreD[elect]
                        if j%2 == 0:
                            t1 +=1
                        else:
                            t2 += 1
                        scoreD[elect] = (t1,t2)
            
            game.mainiteration()
        
        # calcul du score du jour
        tot1 = 0
        tot2 = 0
        for res in scoreD:
            t1, t2 = scoreD[res]
            if t1 > t2:
                tot1 += 1
            elif t1 < t2:
                tot2 += 1
        f1 = scoreC[0]
        f1 += tot1
        f2 = scoreC[1]
        f2 += tot2
        scoreC = (f1, f2)
    
    print("Score parti 1 :", scoreC[0], " ; Score parti 2 :", scoreC[1])
                
      

if __name__ == '__main__':
    main()
    


