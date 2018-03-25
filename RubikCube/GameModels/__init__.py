__author__ = 'Twitch'
import Heuristics as H

#from array import *

class RubikCubeRepresentation:

    def __init__(self, alto, basso, sinistra, destra, fronte, retro):
        self.alto = alto #lato sopra
        self.basso = basso #lato sotto
        self.sinistra = sinistra #lato sinistro
        self.destra = destra #lato destro
        self.fronte = fronte #lato frontale
        self.retro = retro #lato posteriore

def copy(self, source_state):
    dest_state = RubikCubeRepresentation( source_state.alto, source_state.basso, source_state.sinistra, source_state.destra, source_state.fronte, source_state.retro)
    return dest_state

class RubikCubeState:

    def __init__(self, parent, alto, basso, sinistra, destra, fronte, retro, heuristic):
        self.parent = parent
        self.H = heuristic
        self.representation = RubikCubeRepresentation(alto, basso, sinistra, destra, fronte, retro)

class Game:

    def __init__(self, initialState=None, heuristic=None):
        self.state = initialState
        self.heuristic = heuristic

    def neighbors(self, state):
        out = set([])
        return out

    def getState(self):
        return self.state

    def solution(self, state):
        return True



class RubikCubeGame(Game):


    def __init__(self, alto, basso, sinistra, destra, fronte, retro, heuristic):
        self.state = RubikCubeState(None, alto, basso, sinistra, destra, fronte, retro, heuristic)

    def neighbors(self, state, rep_alfa, rep_beta):
        heuristic = H.RubikCubeHeuristics()
        out = set([])
        # GENERO PASSI SUCCESSIVI RAGGIUNGIBILI

        #    ROTAZIONE ORARIA PANNELLO LATERALE SINISTRO
        rep_beta = RubikCubeRepresentation([state.representation.retro[6], state.representation.alto[1], state.representation.alto[2], state.representation.retro[3], state.representation.alto[4], state.representation.alto[5], state.representation.retro[0], state.representation.alto[7], state.representation.alto[8]],
                                           [state.representation.fronte[0], state.representation.basso[1], state.representation.basso[2], state.representation.fronte[3], state.representation.basso[4], state.representation.basso[5], state.representation.fronte[6], state.representation.basso[7], state.representation.basso[8]],
                                           [state.representation.sinistra[6], state.representation.sinistra[3], state.representation.sinistra[0], state.representation.sinistra[7], state.representation.sinistra[4], state.representation.sinistra[1], state.representation.sinistra[8], state.representation.sinistra[5], state.representation.sinistra[2]],
                                           state.representation.destra,
                                           [state.representation.alto[0], state.representation.fronte[1], state.representation.fronte[2], state.representation.alto[3], state.representation.fronte[4], state.representation.fronte[5], state.representation.alto[6], state.representation.fronte[7], state.representation.fronte[8]],
                                           [state.representation.basso[6], state.representation.retro[1], state.representation.retro[2], state.representation.basso[3], state.representation.retro[4], state.representation.retro[5], state.representation.basso[0], state.representation.retro[7], state.representation.retro[8]])
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

        #   ROTAZIONE ANTIORARIA PANNELLO LATERALE SINISTRO
        rep_beta = RubikCubeRepresentation([state.representation.fronte[0], state.representation.alto[1], state.representation.alto[2], state.representation.fronte[3], state.representation.alto[4], state.representation.alto[5], state.representation.fronte[6], state.representation.alto[7], state.representation.alto[8]],
                                           [state.representation.retro[6], state.representation.basso[1], state.representation.basso[2], state.representation.retro[3], state.representation.basso[4], state.representation.basso[5], state.representation.retro[0], state.representation.basso[7], state.representation.basso[8]],
                                           [state.representation.sinistra[2], state.representation.sinistra[5], state.representation.sinistra[8], state.representation.sinistra[1], state.representation.sinistra[4], state.representation.sinistra[7], state.representation.sinistra[0], state.representation.sinistra[3], state.representation.sinistra[6]],
                                           state.representation.destra,
                                           [state.representation.basso[0], state.representation.fronte[1], state.representation.fronte[2], state.representation.basso[3], state.representation.fronte[4], state.representation.fronte[5], state.representation.basso[6], state.representation.fronte[7], state.representation.fronte[8]],
                                           [state.representation.alto[6], state.representation.retro[1], state.representation.retro[2], state.representation.alto[3], state.representation.retro[4], state.representation.retro[5], state.representation.alto[0], state.representation.retro[7], state.representation.retro[8]])
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

    #   ROTAZIONE ORARIA PANNELLO LATERALE DESTRO (alto,basso, sinistra, destra, fronte, retro)
        rep_beta = RubikCubeRepresentation([state.representation.alto[0], state.representation.alto[1], state.representation.fronte[2], state.representation.alto[3], state.representation.alto[4], state.representation.fronte[5], state.representation.alto[6], state.representation.alto[7], state.representation.alto[8]],
                                           [state.representation.basso[0], state.representation.basso[1], state.representation.retro[8], state.representation.basso[3], state.representation.basso[4], state.representation.retro[5], state.representation.basso[6], state.representation.basso[7], state.representation.retro[2]],
                                           state.representation.sinistra,
                                           [state.representation.destra[6], state.representation.destra[3], state.representation.destra[0], state.representation.destra[7], state.representation.destra[4], state.representation.destra[1], state.representation.destra[8], state.representation.destra[5], state.representation.destra[2]],
                                           [state.representation.fronte[0], state.representation.fronte[1], state.representation.basso[2], state.representation.fronte[3], state.representation.fronte[4], state.representation.basso[5], state.representation.fronte[6], state.representation.fronte[7], state.representation.basso[8]],
                                           [state.representation.retro[0], state.representation.retro[1], state.representation.alto[8], state.representation.retro[3], state.representation.retro[4], state.representation.alto[5], state.representation.retro[6], state.representation.retro[7], state.representation.alto[2]])
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

    #   ROTAZIONE ANTIORARIA PANELLO LATERALE DESTRO
        rep_beta = RubikCubeRepresentation([state.representation.alto[0], state.representation.alto[1], state.representation.retro[8], state.representation.alto[3], state.representation.alto[4], state.representation.retro[5], state.representation.alto[6], state.representation.alto[7], state.representation.retro[2]],
                                           [state.representation.basso[0], state.representation.basso[1], state.representation.fronte[2], state.representation.basso[3], state.representation.basso[4], state.representation.fronte[5], state.representation.basso[6], state.representation.basso[7], state.representation.fronte[8]],
                                           state.representation.sinistra,
                                           [state.representation.destra[2], state.representation.destra[5], state.representation.destra[8], state.representation.destra[1], state.representation.destra[4], state.representation.destra[7], state.representation.destra[0], state.representation.destra[3], state.representation.destra[6]],
                                           [state.representation.fronte[0], state.representation.fronte[1], state.representation.alto[2], state.representation.fronte[3], state.representation.fronte[4], state.representation.alto[5], state.representation.fronte[6], state.representation.fronte[7], state.representation.alto[8]],
                                           [state.representation.retro[0], state.representation.retro[1], state.representation.basso[8], state.representation.retro[3], state.representation.retro[4], state.representation.basso[5], state.representation.retro[6], state.representation.retro[7], state.representation.basso[2]])
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

    #   ROTAZIONE ORARIA PANNELLO SUPERIORE
        rep_beta = RubikCubeRepresentation([state.representation.alto[6], state.representation.alto[3], state.representation.alto[0], state.representation.alto[7], state.representation.alto[4], state.representation.alto[1], state.representation.alto[8], state.representation.alto[5], state.representation.alto[2]],
                                           state.representation.basso,
                                           [state.representation.fronte[0], state.representation.fronte[1], state.representation.fronte[2], state.representation.sinistra[3], state.representation.sinistra[4], state.representation.sinistra[5], state.representation.sinistra[6], state.representation.sinistra[7], state.representation.sinistra[8]],
                                           [state.representation.retro[8], state.representation.retro[7], state.representation.retro[6], state.representation.destra[3], state.representation.destra[4], state.representation.destra[5], state.representation.destra[6], state.representation.destra[7], state.representation.destra[8]],
                                           [state.representation.destra[0], state.representation.destra[1], state.representation.destra[2], state.representation.fronte[3], state.representation.fronte[4], state.representation.fronte[5], state.representation.fronte[6], state.representation.fronte[7], state.representation.fronte[8]],
                                           [state.representation.retro[0], state.representation.retro[1], state.representation.retro[2], state.representation.retro[3], state.representation.retro[4], state.representation.retro[5], state.representation.sinistra[2], state.representation.sinistra[1], state.representation.sinistra[0]])
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

    #   ROTAZIONE ANTIORARIA PANNELLO SUPERIORE
        rep_beta = RubikCubeRepresentation([state.representation.alto[2], state.representation.alto[5], state.representation.alto[8], state.representation.alto[1], state.representation.alto[4], state.representation.alto[7], state.representation.alto[0], state.representation.alto[3], state.representation.alto[6]],
                                           state.representation.basso,
                                           [state.representation.retro[8], state.representation.retro[7], state.representation.retro[6], state.representation.sinistra[3], state.representation.sinistra[4], state.representation.sinistra[5], state.representation.sinistra[6], state.representation.sinistra[7], state.representation.sinistra[8]],
                                           [state.representation.fronte[0], state.representation.fronte[1], state.representation.fronte[2], state.representation.destra[3], state.representation.destra[4], state.representation.destra[5], state.representation.destra[6], state.representation.destra[7], state.representation.destra[8]],
                                           [state.representation.sinistra[0], state.representation.sinistra[1], state.representation.sinistra[2], state.representation.fronte[3], state.representation.fronte[4], state.representation.fronte[5], state.representation.fronte[6], state.representation.fronte[7], state.representation.fronte[8]],
                                           [state.representation.retro[0], state.representation.retro[1], state.representation.retro[2], state.representation.retro[3], state.representation.retro[4], state.representation.retro[5], state.representation.destra[2], state.representation.destra[1], state.representation.destra[0]])
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

    #   ROTAZIONE ORARIA PANNELLO INFERIORE
        rep_beta = RubikCubeRepresentation(state.representation.alto,
                                           [state.representation.basso[6], state.representation.basso[3], state.representation.basso[0], state.representation.basso[7], state.representation.basso[4], state.representation.basso[1], state.representation.basso[8], state.representation.basso[5], state.representation.basso[2]],
                                           [state.representation.sinistra[0], state.representation.sinistra[1], state.representation.sinistra[2], state.representation.sinistra[3], state.representation.sinistra[4], state.representation.sinistra[5], state.representation.fronte[6], state.representation.fronte[7], state.representation.fronte[8]],
                                           [state.representation.destra[0], state.representation.destra[1], state.representation.destra[2], state.representation.destra[3], state.representation.destra[4], state.representation.destra[5], state.representation.retro[2], state.representation.retro[1], state.representation.retro[0]],
                                           [state.representation.fronte[0], state.representation.fronte[1], state.representation.fronte[2], state.representation.fronte[3], state.representation.fronte[4], state.representation.fronte[5], state.representation.destra[6], state.representation.destra[7], state.representation.destra[8]],
                                           [state.representation.sinistra[8], state.representation.sinistra[7], state.representation.sinistra[6], state.representation.retro[3], state.representation.retro[4], state.representation.retro[5], state.representation.retro[6], state.representation.retro[7], state.representation.retro[8]])
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

    #   ROTAZIONE ANTIORARIA PANNELLO INFERIORE
        rep_beta = RubikCubeRepresentation(state.representation.alto,
                                           [state.representation.basso[2], state.representation.basso[5], state.representation.basso[8], state.representation.basso[1], state.representation.basso[4], state.representation.basso[7], state.representation.basso[0], state.representation.basso[3], state.representation.basso[6]],
                                           [state.representation.retro[0], state.representation.sinistra[1], state.representation.sinistra[2], state.representation.retro[3], state.representation.sinistra[4], state.representation.sinistra[5], state.representation.retro[6], state.representation.sinistra[7], state.representation.sinistra[8]],
                                           [state.representation.fronte[0], state.representation.destra[1], state.representation.destra[2], state.representation.fronte[3], state.representation.destra[4], state.representation.destra[5], state.representation.fronte[6], state.representation.destra[7], state.representation.destra[8]],
                                           [state.representation.sinistra[0], state.representation.fronte[1], state.representation.fronte[2], state.representation.sinistra[3], state.representation.fronte[4], state.representation.fronte[5], state.representation.sinistra[6], state.representation.fronte[7], state.representation.fronte[8]],
                                           [state.representation.destra[6], state.representation.retro[1], state.representation.retro[2], state.representation.destra[3], state.representation.retro[4], state.representation.retro[5], state.representation.destra[3], state.representation.retro[7], state.representation.retro[8]])
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

    #   ROTAZIONE ORARIA PANNELLO FRONTALE
        rep_beta = RubikCubeRepresentation([state.representation.alto[0], state.representation.alto[1], state.representation.alto[2], state.representation.alto[3], state.representation.alto[4], state.representation.alto[5], state.representation.sinistra[8], state.representation.sinistra[5], state.representation.sinistra[2]],
                                           [state.representation.destra[6], state.representation.destra[3], state.representation.destra[0], state.representation.basso[3], state.representation.basso[4], state.representation.basso[5], state.representation.basso[6], state.representation.basso[7], state.representation.basso[8]],
                                           [state.representation.sinistra[0], state.representation.sinistra[1], state.representation.basso[0], state.representation.sinistra[3], state.representation.sinistra[4], state.representation.basso[1], state.representation.sinistra[6], state.representation.sinistra[7], state.representation.basso[2]],
                                           [state.representation.alto[6], state.representation.destra[1], state.representation.destra[2], state.representation.alto[7], state.representation.destra[4], state.representation.destra[5], state.representation.alto[8], state.representation.destra[7], state.representation.destra[8]],
                                           [state.representation.fronte[6], state.representation.fronte[3], state.representation.fronte[0], state.representation.fronte[7], state.representation.fronte[4], state.representation.fronte[1], state.representation.fronte[8], state.representation.fronte[5], state.representation.fronte[2]],
                                           state.representation.retro)
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

    #   ROTAZIONE ANTIORARIA PANNELLO FRONTALE
        rep_beta = RubikCubeRepresentation([state.representation.alto[0], state.representation.alto[1], state.representation.alto[2], state.representation.alto[3], state.representation.alto[4], state.representation.alto[5], state.representation.destra[0], state.representation.destra[3], state.representation.destra[6]],
                                           [state.representation.sinistra[2], state.representation.sinistra[5], state.representation.sinistra[8], state.representation.basso[3], state.representation.basso[4], state.representation.basso[5], state.representation.basso[6], state.representation.basso[7], state.representation.basso[8]],
                                           [state.representation.sinistra[0], state.representation.sinistra[1], state.representation.alto[8], state.representation.sinistra[3], state.representation.sinistra[4], state.representation.alto[7], state.representation.sinistra[6], state.representation.sinistra[7], state.representation.alto[6]],
                                           [state.representation.basso[2], state.representation.destra[1], state.representation.destra[2], state.representation.basso[1], state.representation.destra[4], state.representation.destra[5], state.representation.basso[0], state.representation.destra[7], state.representation.destra[8]],
                                           [state.representation.fronte[2], state.representation.fronte[5], state.representation.fronte[8], state.representation.fronte[1], state.representation.fronte[4], state.representation.fronte[7], state.representation.fronte[0], state.representation.fronte[3], state.representation.fronte[6]],
                                           state.representation.retro)
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

    #   ROTAZIONE ORARIA PANNELLO POSTERIORE
        rep_beta = RubikCubeRepresentation([state.representation.destra[2], state.representation.destra[5], state.representation.destra[8], state.representation.alto[3], state.representation.alto[4], state.representation.alto[5], state.representation.alto[6], state.representation.alto[7], state.representation.alto[8]],
                                           [state.representation.basso[0], state.representation.basso[1], state.representation.basso[2], state.representation.basso[3], state.representation.basso[4], state.representation.basso[5], state.representation.sinistra[0], state.representation.sinistra[3], state.representation.sinistra[6]],
                                           [state.representation.alto[2], state.representation.sinistra[1], state.representation.sinistra[2], state.representation.alto[1], state.representation.sinistra[4], state.representation.sinistra[5], state.representation.alto[2], state.representation.sinistra[7], state.representation.sinistra[8]],
                                           [state.representation.destra[0], state.representation.destra[1], state.representation.basso[6], state.representation.destra[3], state.representation.destra[4], state.representation.basso[7], state.representation.destra[6], state.representation.destra[7], state.representation.basso[8]],
                                           state.representation.fronte,
                                           [state.representation.retro[2], state.representation.retro[5], state.representation.retro[8], state.representation.retro[1], state.representation.retro[4], state.representation.retro[7], state.representation.retro[0], state.representation.retro[3], state.representation.retro[6]])
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

    #   ROTAZIONE ANTIORARIA PANNELLO POSTERIORE
        rep_beta = RubikCubeRepresentation([state.representation.sinistra[6], state.representation.sinistra[3], state.representation.sinistra[0], state.representation.alto[3], state.representation.alto[4], state.representation.alto[5], state.representation.alto[6], state.representation.alto[7], state.representation.alto[8]],
                                           [state.representation.basso[0], state.representation.basso[1], state.representation.basso[2], state.representation.basso[3], state.representation.basso[4], state.representation.basso[5], state.representation.destra[2], state.representation.destra[5], state.representation.destra[8]],
                                           [state.representation.basso[6], state.representation.sinistra[1], state.representation.sinistra[2], state.representation.basso[7], state.representation.sinistra[4], state.representation.sinistra[5], state.representation.basso[8], state.representation.sinistra[7], state.representation.sinistra[8]],
                                           [state.representation.destra[0], state.representation.destra[1], state.representation.alto[0], state.representation.destra[3], state.representation.destra[4], state.representation.alto[1], state.representation.destra[6], state.representation.destra[7], state.representation.alto[2]],
                                           state.representation.fronte,
                                           [state.representation.retro[6], state.representation.retro[3], state.representation.retro[0], state.representation.retro[7], state.representation.retro[4], state.representation.retro[1], state.representation.retro[8], state.representation.retro[5], state.representation.retro[2]])
        n = RubikCubeState(state, rep_beta.alto, rep_beta.basso, rep_beta.sinistra, rep_beta.destra, rep_beta.fronte, rep_beta.retro, heuristic.H(rep_beta)) #euristica lavora su una rappresentazione di stato non sullo stato direttamente
        out.add(n)

        return out

    def solution(self, state):
        fronte = state.representation.fronte[0]
        basso = state.representation.basso[0]
        alto = state.representation.alto[0]
        sinistra = state.representation.sinistra[0]
        destra = state.representation.destra[0]
        retro = state.representation.retro[0]
        for i in range(1, 9):
            if fronte <> state.representation.fronte[i] or basso <> state.representation.basso[i] or alto <> state.representation.alto[i] or sinistra <> state.representation.sinistra[i] or destra <> state.representation.destra[i] or retro <> state.representation.retro[i]:
                return False
        return True


