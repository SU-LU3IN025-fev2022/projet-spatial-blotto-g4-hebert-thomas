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

def aleatoire(initStates, wallStates, objectifs, players, game):

    listPaths = []
    CoupleMilEl = []
    g =np.ones((nbLignes,nbCols),dtype=bool) 
    for w in wallStates:     
        g[w]=False
        
    for i in range(len(initStates)):
        elect = random.randrange(4)
        p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
        path = probleme.astar(p)
        listPaths.append(path)
        CoupleMilEl.append(elect)
    
    posPlayers = initStates
    
    Finished = []
    score = dict()
    for i in range(len(objectifs)):
        score[i] = (0,0) 

    for i in range(10000): 
            
        if len(Finished) == len(listPaths):
            break;
            
        for j in range(len(listPaths)):
            if j not in Finished:
                path = listPaths[j]
                row,col = path[i]
                posPlayers[j]=(row,col)
                players[j].set_rowcol(row,col)
                elect = CoupleMilEl[j]
                if (row,col) == objectifs[elect]:
                    Finished.append(j)
                    t1, t2 = score[elect]
                    if j%2 == 0:
                        t1 +=1
                    else:
                        t2 += 1
                    score[elect] = (t1,t2) 
            
        # on passe a l'iteration suivante du jeu
        game.mainiteration()

                    
            
                
        pygame.quit()

        tot1 = 0
        tot2 = 0
        for res in score:
            t1, t2 = score[res]
            if t1 > t2:
                tot1 += 1
            elif t1 < t2:
                tot2 += 1
        print("score parti 1:", tot1, "; score parti 2:", tot2)