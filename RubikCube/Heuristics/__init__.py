__author__ = 'Twitch'
import GameModels
class Heuristics:

    def __init__(self):
        pass

    def H(self, representation):
        return 1

class RubikCubeHeuristics(Heuristics):

# per ogni pannello assegno punteggio a seconda di quanti e quali tasselli hanno stesso colore del centro :
        #  1 spigolo : 24
        #  1 vertice : 23
        #  2 spigoli : 22                                  indici spigoli sono : 0, 2, 6, 8
        #  2 vertici : 21                                  indici vertici sono : 1, 3, 5, 7
        #  3 spigoli : 20                                  indice centro : 4
        #  3 vertici : 19
        #  4 spigoli : 18
        #  4 vertici : 17
        #  1 vertice & 1 spigoli : 16
        #  1 vertice & 2 spigoli : 15
        #  1 vertice & 3 spigoli : 14
        #  1 vertice & 4 spigoli : 13
        #  2 vertici & 1 spigoli : 12
        #  2 vertici & 2 spigoli : 11
        #  2 vertici & 3 spigoli : 10
        #  2 vertici & 4 spigoli : 9
        #  3 vertici & 1 spigoli : 8
        #  3 vertici & 2 spigoli : 7
        #  3 vertici & 3 spigoli : 6
        #  3 vertici & 4 spigoli : 5
        #  4 vertici & 1 spigolo : 4
        #  4 vertici & 2 spigoli : 3
        #  4 vertici & 3 spigoli : 2
        #  4 vertici & 4 spigoli : 1
        # selezionando il cubo avente minimo valore euristico ho maggior probabilita di prendere cubo in cui sono piu vicino soluzione

    def H(self, representation): #prende in input un cubo associato ad uno stato
        numero_spigoli = 0
        numero_vertici = 0
        valutazione = 0

        #PANNELLO FRONTALE
        centro = representation.fronte[4]

        if representation.fronte[0] == centro: #spigolo alto sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.fronte[2] == centro: #spigolo alto destra
            numero_spigoli = numero_spigoli + 1
        if representation.fronte[6] == centro: #spigolo basso sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.fronte[8] == centro: #spigolo basso destra
            numero_spigoli = numero_spigoli + 1
        if representation.fronte[1] == centro: #vertice alto centro
            numero_vertici = numero_vertici + 1
        if representation.fronte[3] == centro: #vertice centro sinistra
            numero_vertici = numero_vertici + 1
        if representation.fronte[5] == centro: #vertice centro destra
            numero_vertici = numero_vertici + 1
        if representation.fronte[7] == centro: #vertice basso centro
            numero_vertici = numero_vertici + 1

        if numero_spigoli == 1:
            if numero_vertici == 4:
                valutazione = valutazione + 4  # 4 vertici ed 1 spigolo
            elif numero_vertici == 3:
                valutazione = valutazione + 8  # 3 vertici ed 1 spigolo
            elif numero_vertici == 2:
                valutazione = valutazione + 12 # 2 vertici ed 1 spigolo
            elif numero_vertici == 1:
                valutazione = valutazione + 16 # 1 vertice ed 1 spigolo
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_spigoli == 2:
            if numero_vertici == 4:
                valutazione = valutazione + 3  # 4 vertici e 2 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 7  # 3 vertici e 2 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 11 # 2 vertici e 2 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 15 # 1 vertice e 2 spigoli
            else:
                valutazione = valutazione + 22 # 2 spigoli
        elif numero_spigoli == 3:
            if numero_vertici == 4:
                valutazione = valutazione + 2  # 4 vertici e 3 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 6  # 3 vertici e 3 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 10 # 2 vertici e 3 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 14 # 1 vertice e 3 spigoli
            else:
                valutazione = valutazione + 20 # 3 spigoli
        elif numero_spigoli == 4:
            if numero_vertici == 4:
                valutazione = valutazione + 1  # 4 vertici e 4 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 5  # 3 vertici e 4 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 9 # 2 vertici e 4 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 13 # 1 vertice e 4 spigoli
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_vertici == 1:
            valutazione = valutazione + 23     # 1 vertice
        elif numero_vertici == 2:
            valutazione = valutazione + 21     # 2 vertici
        elif numero_vertici == 3:
            valutazione = valutazione + 19     # 3 vertici
        elif numero_vertici == 4:
            valutazione = valutazione + 17     # 4 vertici


        #ripristino contatori
        numero_spigoli = 0
        numero_vertici = 0

        #PANNELLO POSTERIORE
        centro = representation.retro[4]

        if representation.retro[0] == centro: #spigolo alto sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.retro[2] == centro: #spigolo alto destra
            numero_spigoli = numero_spigoli + 1
        if representation.retro[6] == centro: #spigolo basso sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.retro[8] == centro: #spigolo basso destra
            numero_spigoli = numero_spigoli + 1
        if representation.retro[1] == centro: #vertice alto centro
            numero_vertici = numero_vertici + 1
        if representation.retro[3] == centro: #vertice centro sinistra
            numero_vertici = numero_vertici + 1
        if representation.retro[5] == centro: #vertice centro destra
            numero_vertici = numero_vertici + 1
        if representation.retro[7] == centro: #vertice basso centro
            numero_vertici = numero_vertici + 1

        if numero_spigoli == 1:
            if numero_vertici == 4:
                valutazione = valutazione + 4  # 4 vertici ed 1 spigolo
            elif numero_vertici == 3:
                valutazione = valutazione + 8  # 3 vertici ed 1 spigolo
            elif numero_vertici == 2:
                valutazione = valutazione + 12 # 2 vertici ed 1 spigolo
            elif numero_vertici == 1:
                valutazione = valutazione + 16 # 1 vertice ed 1 spigolo
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_spigoli == 2:
            if numero_vertici == 4:
                valutazione = valutazione + 3  # 4 vertici e 2 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 7  # 3 vertici e 2 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 11 # 2 vertici e 2 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 15 # 1 vertice e 2 spigoli
            else:
                valutazione = valutazione + 22 # 2 spigoli
        elif numero_spigoli == 3:
            if numero_vertici == 4:
                valutazione = valutazione + 2  # 4 vertici e 3 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 6  # 3 vertici e 3 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 10 # 2 vertici e 3 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 14 # 1 vertice e 3 spigoli
            else:
                valutazione = valutazione + 20 # 3 spigolo
        elif numero_spigoli == 4:
            if numero_vertici == 4:
                valutazione = valutazione + 1  # 4 vertici e 4 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 5  # 3 vertici e 4 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 9 # 2 vertici e 4 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 13 # 1 vertice e 4 spigoli
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_vertici == 1:
            valutazione = valutazione + 23     # 1 vertice
        elif numero_vertici == 2:
            valutazione = valutazione + 21     # 2 vertici
        elif numero_vertici == 3:
            valutazione = valutazione + 19     # 3 vertici
        elif numero_vertici == 4:
            valutazione = valutazione + 17     # 4 vertici


        #ripristino contatori
        numero_spigoli = 0
        numero_vertici = 0

        #PANNELLO SUPERIORE
        centro = representation.alto[4]

        if representation.alto[0] == centro: #spigolo alto sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.alto[2] == centro: #spigolo alto destra
            numero_spigoli = numero_spigoli + 1
        if representation.alto[6] == centro: #spigolo basso sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.alto[8] == centro: #spigolo basso destra
            numero_spigoli = numero_spigoli + 1
        if representation.alto[1] == centro: #vertice alto centro
            numero_vertici = numero_vertici + 1
        if representation.alto[3] == centro: #vertice centro sinistra
            numero_vertici = numero_vertici + 1
        if representation.alto[5] == centro: #vertice centro destra
            numero_vertici = numero_vertici + 1
        if representation.alto[7] == centro: #vertice basso centro
            numero_vertici = numero_vertici + 1

        if numero_spigoli == 1:
            if numero_vertici == 4:
                valutazione = valutazione + 4  # 4 vertici ed 1 spigolo
            elif numero_vertici == 3:
                valutazione = valutazione + 8  # 3 vertici ed 1 spigolo
            elif numero_vertici == 2:
                valutazione = valutazione + 12 # 2 vertici ed 1 spigolo
            elif numero_vertici == 1:
                valutazione = valutazione + 16 # 1 vertice ed 1 spigolo
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_spigoli == 2:
            if numero_vertici == 4:
                valutazione = valutazione + 3  # 4 vertici e 2 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 7  # 3 vertici e 2 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 11 # 2 vertici e 2 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 15 # 1 vertice e 2 spigoli
            else:
                valutazione = valutazione + 22 # 2 spigoli
        elif numero_spigoli == 3:
            if numero_vertici == 4:
                valutazione = valutazione + 2  # 4 vertici e 3 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 6  # 3 vertici e 3 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 10 # 2 vertici e 3 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 14 # 1 vertice e 3 spigoli
            else:
                valutazione = valutazione + 20 # 3 spigolo
        elif numero_spigoli == 4:
            if numero_vertici == 4:
                valutazione = valutazione + 1  # 4 vertici e 4 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 5  # 3 vertici e 4 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 9 # 2 vertici e 4 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 13 # 1 vertice e 4 spigoli
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_vertici == 1:
            valutazione = valutazione + 23     # 1 vertice
        elif numero_vertici == 2:
            valutazione = valutazione + 21     # 2 vertici
        elif numero_vertici == 3:
            valutazione = valutazione + 19     # 3 vertici
        elif numero_vertici == 4:
            valutazione = valutazione + 17     # 4 vertici


        #ripristino contatori
        numero_spigoli = 0
        numero_vertici = 0

        #PANNELLO INFERIORE
        centro = representation.basso[4]

        if representation.basso[0] == centro: #spigolo alto sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.basso[2] == centro: #spigolo alto destra
            numero_spigoli = numero_spigoli + 1
        if representation.basso[6] == centro: #spigolo basso sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.basso[8] == centro: #spigolo basso destra
            numero_spigoli = numero_spigoli + 1
        if representation.basso[1] == centro: #vertice alto centro
            numero_vertici = numero_vertici + 1
        if representation.basso[3] == centro: #vertice centro sinistra
            numero_vertici = numero_vertici + 1
        if representation.basso[5] == centro: #vertice centro destra
            numero_vertici = numero_vertici + 1
        if representation.basso[7] == centro: #vertice basso centro
            numero_vertici = numero_vertici + 1

        if numero_spigoli == 1:
            if numero_vertici == 4:
                valutazione = valutazione + 4  # 4 vertici ed 1 spigolo
            elif numero_vertici == 3:
                valutazione = valutazione + 8  # 3 vertici ed 1 spigolo
            elif numero_vertici == 2:
                valutazione = valutazione + 12 # 2 vertici ed 1 spigolo
            elif numero_vertici == 1:
                valutazione = valutazione + 16 # 1 vertice ed 1 spigolo
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_spigoli == 2:
            if numero_vertici == 4:
                valutazione = valutazione + 3  # 4 vertici e 2 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 7  # 3 vertici e 2 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 11 # 2 vertici e 2 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 15 # 1 vertice e 2 spigoli
            else:
                valutazione = valutazione + 22 # 2 spigoli
        elif numero_spigoli == 3:
            if numero_vertici == 4:
                valutazione = valutazione + 2  # 4 vertici e 3 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 6  # 3 vertici e 3 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 10 # 2 vertici e 3 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 14 # 1 vertice e 3 spigoli
            else:
                valutazione = valutazione + 20 # 3 spigolo
        elif numero_spigoli == 4:
            if numero_vertici == 4:
                valutazione = valutazione + 1  # 4 vertici e 4 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 5  # 3 vertici e 4 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 9 # 2 vertici e 4 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 13 # 1 vertice e 4 spigoli
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_vertici == 1:
            valutazione = valutazione + 23     # 1 vertice
        elif numero_vertici == 2:
            valutazione = valutazione + 21     # 2 vertici
        elif numero_vertici == 3:
            valutazione = valutazione + 19     # 3 vertici
        elif numero_vertici == 4:
            valutazione = valutazione + 17     # 4 vertici


        #ripristino contatori
        numero_spigoli = 0
        numero_vertici = 0

        #PANNELLO LATERALE SINISTRO
        centro = representation.sinistra[4]

        if representation.sinistra[0] == centro: #spigolo alto sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.sinistra[2] == centro: #spigolo alto destra
            numero_spigoli = numero_spigoli + 1
        if representation.sinistra[6] == centro: #spigolo basso sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.sinistra[8] == centro: #spigolo basso destra
            numero_spigoli = numero_spigoli + 1
        if representation.sinistra[1] == centro: #vertice alto centro
            numero_vertici = numero_vertici + 1
        if representation.sinistra[3] == centro: #vertice centro sinistra
            numero_vertici = numero_vertici + 1
        if representation.sinistra[5] == centro: #vertice centro destra
            numero_vertici = numero_vertici + 1
        if representation.sinistra[7] == centro: #vertice basso centro
            numero_vertici = numero_vertici + 1

        if numero_spigoli == 1:
            if numero_vertici == 4:
                valutazione = valutazione + 4  # 4 vertici ed 1 spigolo
            elif numero_vertici == 3:
                valutazione = valutazione + 8  # 3 vertici ed 1 spigolo
            elif numero_vertici == 2:
                valutazione = valutazione + 12 # 2 vertici ed 1 spigolo
            elif numero_vertici == 1:
                valutazione = valutazione + 16 # 1 vertice ed 1 spigolo
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_spigoli == 2:
            if numero_vertici == 4:
                valutazione = valutazione + 3  # 4 vertici e 2 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 7  # 3 vertici e 2 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 11 # 2 vertici e 2 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 15 # 1 vertice e 2 spigoli
            else:
                valutazione = valutazione + 22 # 2 spigoli
        elif numero_spigoli == 3:
            if numero_vertici == 4:
                valutazione = valutazione + 2  # 4 vertici e 3 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 6  # 3 vertici e 3 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 10 # 2 vertici e 3 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 14 # 1 vertice e 3 spigoli
            else:
                valutazione = valutazione + 20 # 3 spigolo
        elif numero_spigoli == 4:
            if numero_vertici == 4:
                valutazione = valutazione + 1  # 4 vertici e 4 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 5  # 3 vertici e 4 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 9 # 2 vertici e 4 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 13 # 1 vertice e 4 spigoli
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_vertici == 1:
            valutazione = valutazione + 23     # 1 vertice
        elif numero_vertici == 2:
            valutazione = valutazione + 21     # 2 vertici
        elif numero_vertici == 3:
            valutazione = valutazione + 19     # 3 vertici
        elif numero_vertici == 4:
            valutazione = valutazione + 17     # 4 vertici

        #ripristino contatori
        numero_spigoli = 0
        numero_vertici = 0

        #PANNELLO LATERALE DESTRO
        centro = representation.destra[4]

        if representation.destra[0] == centro: #spigolo alto sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.destra[2] == centro: #spigolo alto destra
            numero_spigoli = numero_spigoli + 1
        if representation.destra[6] == centro: #spigolo basso sinistra
            numero_spigoli = numero_spigoli + 1
        if representation.destra[8] == centro: #spigolo basso destra
            numero_spigoli = numero_spigoli + 1
        if representation.destra[1] == centro: #vertice alto centro
            numero_vertici = numero_vertici + 1
        if representation.destra[3] == centro: #vertice centro sinistra
            numero_vertici = numero_vertici + 1
        if representation.destra[5] == centro: #vertice centro destra
            numero_vertici = numero_vertici + 1
        if representation.destra[7] == centro: #vertice basso centro
            numero_vertici = numero_vertici + 1

        if numero_spigoli == 1:
            if numero_vertici == 4:
                valutazione = valutazione + 4  # 4 vertici ed 1 spigolo
            elif numero_vertici == 3:
                valutazione = valutazione + 8  # 3 vertici ed 1 spigolo
            elif numero_vertici == 2:
                valutazione = valutazione + 12 # 2 vertici ed 1 spigolo
            elif numero_vertici == 1:
                valutazione = valutazione + 16 # 1 vertice ed 1 spigolo
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_spigoli == 2:
            if numero_vertici == 4:
                valutazione = valutazione + 3  # 4 vertici e 2 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 7  # 3 vertici e 2 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 11 # 2 vertici e 2 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 15 # 1 vertice e 2 spigoli
            else:
                valutazione = valutazione + 22 # 2 spigoli
        elif numero_spigoli == 3:
            if numero_vertici == 4:
                valutazione = valutazione + 2  # 4 vertici e 3 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 6  # 3 vertici e 3 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 10 # 2 vertici e 3 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 14 # 1 vertice e 3 spigoli
            else:
                valutazione = valutazione + 20 # 3 spigolo
        elif numero_spigoli == 4:
            if numero_vertici == 4:
                valutazione = valutazione + 1  # 4 vertici e 4 spigoli
            elif numero_vertici == 3:
                valutazione = valutazione + 5  # 3 vertici e 4 spigoli
            elif numero_vertici == 2:
                valutazione = valutazione + 9 # 2 vertici e 4 spigoli
            elif numero_vertici == 1:
                valutazione = valutazione + 13 # 1 vertice e 4 spigoli
            else:
                valutazione = valutazione + 24 # 1 spigolo
        elif numero_vertici == 1:
            valutazione = valutazione + 23     # 1 vertice
        elif numero_vertici == 2:
            valutazione = valutazione + 21     # 2 vertici
        elif numero_vertici == 3:
            valutazione = valutazione + 19     # 3 vertici
        elif numero_vertici == 4:
            valutazione = valutazione + 17     # 4 vertici


        return valutazione # valore minore ==> potenziale cubo maggiore

