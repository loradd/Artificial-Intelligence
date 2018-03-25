__author__ = 'Twitch'
import GameModels as G
import Heuristics as H
from array import *

dicOfStates = {}

def argMin(setOfStates):
    v = []
    k = []
    for sk in setOfStates:
        if sk in dicOfStates:
            v = v + [dicOfStates[sk]]
            k = k + [sk]
        else:
            dicOfStates[sk] = heuristic.H(sk.representation)

    if len(v) > 0:
        return k[v.index(min(v))]
    else:
        return None

def pick(setOfStates):
    return argMin(setOfStates)

def backpath(state):
    padre = state.parent
    lStates = [state]
    while padre!=None:
        lStates = lStates + [padre]
        padre = padre.parent
    # lStates contiene serie stati inversa
    for i in range(len(lStates)): #per ogni stato
        print 'Passo ' + str(i) + ': \n' #informazioni passo
        print 'Faccia Superiore:'
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.alto[0:3])) #prima riga faccia superiore
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.alto[3:6])) #seconda riga faccia superiore
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.alto[6:9])) #terza riga faccia superiore
        print '\n'
        print 'Faccia Inferiore'
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.basso[0:3])) #prima riga faccia inferiore
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.basso[3:6])) #seconda riga faccia inferiore
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.basso[6:9])) #terza riga faccia inferiore
        print '\n'
        print 'Faccia Laterale Sinistra'
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.sinistra[0:3])) #prima riga faccia sinistra
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.sinistra[3:6])) #seconda riga faccia sinistra
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.sinistra[6:9])) #terza riga faccia sinistra
        print '\n'
        print 'Faccia Laterale Destra'
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.destra[0:3])) #prima riga faccia destra
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.destra[3:6])) #seconda riga faccia destra
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.destra[6:9])) #terza riga faccia destra
        print '\n'
        print 'Faccia Posteriore'
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.retro[0:3])) #prima riga faccia posteriore
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.retro[3:6])) #seconda riga faccia posteriore
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.retro[6:9])) #terza riga faccia posteriore
        print '\n'
        print 'Faccia Frontale'
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.fronte[0:3])) #prima riga faccia anteriore
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.fronte[3:6])) #seconda riga faccia anteriore
        print '[ %s ]' % ' | '.join(map(str, lStates[(len(lStates)-1)-i].representation.fronte[6:9])) #terza riga faccia anteriore
        print '\n'
    return reversed(lStates)



def search(game, state0):
    sHorizon = set([])
    sExplored = set([])
    sHorizon.add(state0)
    while (len(sHorizon) > 0):
        view = pick(sHorizon)
        alfa = G.copy(None, view.representation )
        beta = G.copy(None, view.representation )
        if not (view is None):
            if game.solution(view):
                return backpath(view)
            sExplored.add(view)
            sHorizon = sHorizon | (game.neighbors(view, alfa, beta ) - sExplored)
    return None

# Main
heuristic = H.RubikCubeHeuristics()
alto = ['A', 'A', 'A', 'B', 'B', 'B', 'B', 'B', 'B'] #alto : prende 0 1 2 da sx(6,3,0)  alto
basso = ['R', 'R', 'R', 'R', 'R', 'R', 'W', 'W', 'W'] #basso : basso(5) prende 6 7 8 da dx(2,5,8)
destra = ['A', 'A', 'R', 'A', 'A', 'R', 'A', 'A', 'R'] #destra: dx1 alto(0) dx4 alto(1) dx7 alto(2)
sinistra = ['B', 'W', 'W', 'B', 'W', 'W', 'B', 'W', 'W'] #sinistra: basso(6) sx2 basso(7) sx5 basso(8) sx8
fronte = ['V', 'V', 'V', 'V', 'V', 'V', 'V', 'V', 'V'] #fronte
retro = ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'] #retro, permuta
game = G.RubikCubeGame(alto[:], basso[:], sinistra[:], destra[:], fronte[:], retro[:], heuristic=heuristic)
state0 = game.getState()
dicOfStates[state0] = heuristic.H(state0.representation)
solution = search(game, state0)
print '\nEasy...'

