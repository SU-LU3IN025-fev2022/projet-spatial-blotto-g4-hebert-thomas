from search import probleme
import numpy as np
from search.grid2D import ProblemeGrid2D
import random
import copy

class WrongTeam(Exception):
    def __init__(self, message):
        self.message = message


def gagnant(monCoup, coupAdvers):
    moi = 0
    for i in range(len(monCoup)):
        if monCoup[i] > coupAdvers[i]:
            moi += 1
        
    return moi

def genereStrats(militants, electeurs):
    if electeurs == 1:
        return [[militants]]
    strats = []
    for i in range(militants+1):
        for strat in genereStrats(militants-i, electeurs-1):
            strats.append([i] + strat)
    
    stratsF = []
    for s in strats:
        if sum(s) == militants:
            stratsF.append(s)
    return stratsF

def aleatoire(g, initStates, objectifs, equipe):
    if equipe not in {1,2}:
        raise WrongTeam("Erreur numéro d'équipe")
    
    LP = dict()
    coupSuiv = [0 for e in range(len(objectifs))]
    
    if equipe == 1:
        for i in range(0, len(initStates), 2):
            random.seed(None)
            elect = random.randrange(len(objectifs)-1)
            p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
            path = probleme.astar(p)
            LP[i] = (path, elect)
            coupSuiv[elect] += 1
    if equipe == 2:
        for i in range(1, len(initStates), 2):
            random.seed(None)
            elect = random.randrange(len(objectifs)-1)
            p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
            path = probleme.astar(p)
            LP[i] = (path, elect)
            coupSuiv[elect] += 1
    
    return (LP, coupSuiv)

def tetu(g, initStates, objectifs, LP, equipe):
    if equipe not in {1,2}:
        raise WrongTeam("Erreur numéro d'équipe")
    
    newLP = dict()
    coupSuiv = [0 for e in range(len(objectifs))]
    
    if equipe == 1:
        for i in range(0, len(initStates), 2):
            elect = (LP[i])[1]
            p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
            path = probleme.astar(p)
            newLP[i] = (path, elect)
            coupSuiv[elect] += 1
    if equipe == 2:
        for i in range(1, len(initStates), 2):
            elect = (LP[i])[1]
            p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
            path = probleme.astar(p)
            newLP[i] = (path, elect)
            coupSuiv[elect] += 1
    
    return (newLP, coupSuiv)

def stochastique(g, initStates, objectifs, equipe, k, lStoch, monCoup, coupAdvers):
    if equipe not in {1,2}:
        raise WrongTeam("Erreur numéro d'équipe")
    
    if not lStoch:
        for i in range(k):
            l = 0
            min = (len(objectifs) // 2) + 1
            monCoup = [0 for e in range(len(objectifs))]
            for j in range(0, len(initStates), 2):
                if min != 0:
                    monCoup[l] += 1
                    l += 1
                    min -= 1
                else:
                    random.seed(None)
                    elect = random.randrange(len(objectifs)-1)
                    monCoup[elect] += 1
            lStoch[tuple(monCoup)] = 0.5
    
    if monCoup != [] and coupAdvers != []:
        if gagnant(monCoup, coupAdvers) > gagnant(coupAdvers, monCoup):
            coup = tuple(monCoup)
            lStoch[coup] += 0.25
        else:
            coup = tuple(monCoup)
            lStoch[coup] -= 0.25
        
        coupSuiv = list(max(lStoch, key=lStoch.get))
    else:
        random.seed(None)
        coupSuiv = list(random.choice(list(lStoch)))
    
    coupSuiv2 = copy.deepcopy(coupSuiv)
    LP = dict()
    
    j = 0
    if equipe == 1:
        for i in range(0, len(initStates), 2):
            elect = -1
            while(elect == -1):
                if coupSuiv[j] != 0:
                    elect = j
                    coupSuiv[j] -= 1
                else:
                    j += 1
            p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
            path = probleme.astar(p)
            LP[i] = (path, elect)
    if equipe == 2:
        for i in range(1, len(initStates), 2):
            elect = -1
            while(elect == -1):
                if coupSuiv[j] != 0:
                    elect = j
                    coupSuiv[j] -= 1
                else:
                    j += 1
            p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
            path = probleme.astar(p)
            LP[i] = (path, elect)
    
    return (LP, coupSuiv2)
            

def MR(g, initStates, objectifs, equipe, coupAdvers):
    if equipe not in {1,2}:
        raise WrongTeam("Erreur numéro d'équipe")
    
    coupSuiv = [e+1 for e in coupAdvers]
    tot = sum(coupSuiv) - (len(initStates)//2)
    j = 0
    while(tot != 0):
        coupSuiv[j] -= 1
        tot -= 1
        if coupSuiv[j] == 0:
            j += 1
    
    coupSuiv2 = copy.deepcopy(coupSuiv)
    LP = dict()
    
    j = 0
    if equipe == 1:
        for i in range(0, len(initStates), 2):
            elect = -1
            while(elect == -1):
                if coupSuiv[j] != 0:
                    elect = j
                    coupSuiv[j] -= 1
                else:
                    j += 1
            p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
            path = probleme.astar(p)
            LP[i] = (path, elect)
    if equipe == 2:
        for i in range(1, len(initStates), 2):
            elect = -1
            while(elect == -1):
                if coupSuiv[j] != 0:
                    elect = j
                    coupSuiv[j] -= 1
                else:
                    j += 1
            p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
            path = probleme.astar(p)
            LP[i] = (path, elect)
    
    return (LP, coupSuiv2)

def fictitious(g, initStates, objectifs, equipe, coupsPossibles, FPAdvers, coupAdvers):
    if equipe not in {1,2}:
        raise WrongTeam("Erreur numéro d'équipe")
    
    CA = tuple(coupAdvers)
    if CA not in FPAdvers:
        FPAdvers[CA] = [1, 0.0]
    else:
        (FPAdvers[CA])[0] += 1
        
    tot = 0
    for k in FPAdvers:
        tot += (FPAdvers[k])[0]
    
    for k in FPAdvers:
        (FPAdvers[k])[1] = (FPAdvers[k])[0]/tot
        
    espmax = 0
    coupSuiv = []
    for strat in coupsPossibles:
        esp = 0
        for k in FPAdvers:
            advers = list(k)
            esp += gagnant(strat, advers) * (FPAdvers[k])[1]
        if esp > espmax:
            espmax = esp
            coupSuiv = copy.deepcopy(strat)
    
    coupSuiv2 = copy.deepcopy(coupSuiv)
    LP = dict()
    
    j = 0
    if equipe == 1:
        for i in range(0, len(initStates), 2):
            elect = -1
            while(elect == -1):
                if coupSuiv[j] != 0:
                    elect = j
                    coupSuiv[j] -= 1
                else:
                    j += 1
            p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
            path = probleme.astar(p)
            LP[i] = (path, elect)
    if equipe == 2:
        for i in range(1, len(initStates), 2):
            elect = -1
            while(elect == -1):
                if coupSuiv[j] != 0:
                    elect = j
                    coupSuiv[j] -= 1
                else:
                    j += 1
            p = ProblemeGrid2D(initStates[i],objectifs[elect],g,'manhattan')
            path = probleme.astar(p)
            LP[i] = (path, elect)
    
    return (LP, coupSuiv2)