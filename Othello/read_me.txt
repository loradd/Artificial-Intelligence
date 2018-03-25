#	OTHELLO
Nel gioco di Othello, due giocatori a turno piazzano pedine del loro colore ( nero o bianco )
con lo scopo di catturare pedine avversarie fino ad arrivare a non poter più esser fatta
alcuna mossa, a quel punto colui che avrà maggior numero di pedine piazzate sarà il vincitore.

Ad ogni mossa, ogni giocatore deve catturare almeno una pedina dell'avversario ma non v'è
alcun tetto massimo di pedine catturabili.

Per catturare le pedine dell'avversario, ogni giocatore deve far in modo di disporre due
sue pedine in maniera che lungo la linea retta di interconnessione tra queste vi siano solo
pedine avversarie.
In tal caso, posizionando una delle due pedine, le pedine avversarie vengono trasformate in
pedine del giocatore:

	B N N N ===> B N N N B ===> B B B B B
	
Due pedine di un dato giocatore possono esser interconnesse lungo una linea retta orizzontale,
verticale, diagonale, l'unica condizione è che siano separate unicamente da pedine avversarie.

#	TAVOLO DA GIOCO
La tavola da gioco viene rappresentata per mezzo di una lista unidimensionale di 100 elementi,
in essa sono incluse le celle ordinarie della tavola ed un bordo aggiuntivo di celle fuori 
dalla tavola.

La decisione di includere anche un margine della tavola è dovuta al fatto che così facendo
si semplificano le operazioni di verifica che un dato elemento sia nella tavola o che una
data mossa non porti fuori dalla tavola.

Nella lista unidimensionale, ogni sottolista di 10 elementi rappresenta una riga della tavola
ed ogni elemento rappresenta ovviamente una cella della tavola.

La scelta di rappresentare la tavola come lista unidimensionale permette di evitare funzioni
di adattamento delle celle ad indici di lista, sarà infatti sufficiente indicare:

		board[ij] per ottenere la cella di indici (i, j)

Per quanto riguarda i contenuti delle celle della tavola:

		- 'W' indica una pedina bianca
		- 'B' indica una pedina nera
		- '.' indica una cella vuota
		- 'X' indica una cella del bordo esterno della tavola

dunque la tavola iniziale sarà:

	X X X X X X X X X X
	X . . . . . . . . X
	X . . . . . . . . X
	X . . . . . . . . X
	X . . . W B . . . X
	X . . . B W . . . X
	X . . . . . . . . X 
	X . . . . . . . . X 
	X . . . . . . . . X
	X X X X X X X X X X 		

Ad ogni turno non occorre far altro che ricevere la mossa scelta dal giocatore, aggiornare
la tavola di gioco e, se sono ancora possibili mosse legali, passare la mano al giocatore
avversario, altrimenti terminare il gioco e ritornare il punteggio finale.

# STRATEGIA MINIMAX
La strategia di minimax permette di stabilire il livello di analisi per ogni giocatore,
ad ogni passo ritorna il minimo valore raggiungibile con una certa mossa basandosi su una
funzione di calcolo del punteggio pesata da valori assegnati in base all'importanza della posizione
nella tabella di gioco ( la tabella è nel codice sorgente CELLS_WEIGHTS ).

