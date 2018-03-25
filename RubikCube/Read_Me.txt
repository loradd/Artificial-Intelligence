INTELLIGENZA ARTIFICIALE I - AA 2013/2014
HOMEWORK 1 : CUBO DI RUBIK ( RICERCA GUIDATA DA EURISTICA )

STRUTTURA DEL CUBO DI RUBIK:
Per definizione, un "Cubo di Rubik" consiste in un cubo nel quale ogni faccia è suddivisa a formare
una matrice quadrata N x N di tasselli colorati di eguali dimensioni, dove N è un numero intero costante 
per ogni faccia dell'istanza di cubo. 
Ogni tassello può assumere uno ed un solo valore ( colore ) da un insieme di colori scelti arbitrariamente
avente cardinalità esattamente pari al numero di facce del cubo ( 6 elementi ), ciò con la condizione che 
per ognuno dei colori nell'insieme vi siano esattamente N x N tasselli associati ( di quel colore ).

OPERAZIONI LEGALI SUL CUBO:
Ad ogni passo è possibile modellare la configurazione dei tasselli per mezzo di operazioni di rotazione 
definite sulle singole facce del cubo; in particolare, supponendo riferimento fisso ad una faccia del 
cubo arbitraria ( FACCIA FRONTALE ), è possibile individuare le seguenti tipologie di rotazione possibili:
		A) ROTAZIONE FACCIA SINISTRA 	
		B) ROTAZIONE FACCIA DESTRA
		C) ROTAZIONE FACCIA INFERIORE
		D) ROTAZIONE FACCIA SUPERIORE
		E) ROTAZIONE FACCIA POSTERIORE
		F) ROTAZIONE FACCIA FRONTALE
Per ognuna di tali tipologie è inoltre possibile differenziare i casi di rotazione in senso ORARIO ed in 
senso ANTIORARIO in base a che la rotazione sia verso destra o sinistra rispetto al pannello soggetto 
dell'operazione. 

PROBLEMA:
Partendo da una configurazione arbitraria dei pannelli di una istanza di "Cubo di Rubik", lo scopo del
rompicapo è quello di giungere, per mezzo di una successione di lecite operazioni di rotazione delle 
facce del cubo, alla situazione in cui ogni faccia sia composta da pannelli di uno ed un solo colore.

RAPPRESENTAZIONE DEL PROBLEMA:
Nell'implementazione del rompicapo si è supposto che:
	- N = 3 ( ogni faccia è una matrice 3 x 3 )
	- Colori = { Arancione, Blu, Rosso, Bianco, Verde, Giallo } ( colori possibili singolo tassello )
	- Il punto di osservazione del cubo durante le operazioni di rotazione rimane fisso ad una faccia ( faccia frontale ).

La rappresentazione del cubo è stata realizzata per mezzo di un insieme di matrici di caratteri 3 x 3 di cardinalità
esattamente pari al numero di facce del cubo, in particolare, ogni locazione in esse potrà assumere un unico valore tra:
	- 'A' per tassello di colore Arancione
	- 'B' per tassello di colore Blu
	- 'R' per tassello di colore Rosso
	- 'V' per tassello di colore Verde
	- 'G' per tassello di colore Giallo
	- 'W' per tassello di colore Bianco

Essendo stato supposto di mantenere fisso il punto di osservazione del cubo durante le operazioni di rotazione, 
le matrici definite sono: 
	- "alto" per la faccia sovrastante alla faccia frontale
	- "basso" per la faccia sottostante alla faccia frontale
	- "destra" perla faccia laterale alla destra della faccia frontale
	- "sinistra" per la faccia laterale alla sinistra della faccia frontale
	- "retro" per la faccia posteriore alla faccia frontale
	- "fronte" per la faccia frontale 
NOTA:
Supponendo di avere un Cubo di Rubik in vetro nel quale ogni faccia è composta da tasselli numerati in ordine
STRETTAMENTE CRESCENTE dal più alto a sinistra al più basso a destra, è facile vedere che, mantenendo fisso su
una delle facce il punto di osservazione, i tasselli della faccia retrostante sembrano esser disposti in modo che:
	- le RIGHE sono ordinate in modo STRETTAMENTE CRESCENTE da sinistra verso destra
	- le colonne sono ordinate in modo che la successione dei valori minimi di ognuna è STRETTAMENTE
	   DECRESCENTE
Dunque sostanzialmente in modo che la matrice:
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
sembra esser disposta come segue:
[6, 7, 8]
[3, 4, 5]
[0, 1, 2]
Quest'ultima è la rappresentazione della matrice tenuta in considerazione nell'implementazione delle operazioni
di rotazione ( scambio di elementi tra matrici ) coinvolgenti elementi della faccia posteriore, in particolare
del pannello superiore, laterale sinistro, laterale destro ed inferiore rispetto alla faccia frontale.

FUNZIONE EURISTICA:
La funzione euristica implementata assegna valori alle varie configurazioni del cubo valutando la configurazione
di ognuna delle facce in base ad una classifica di situazioni convenienti prestabilita.
In particolare tale classifica è strutturata sulla base delle seguenti considerazioni:
	- Il colore finale dei pannelli di una faccia è dato dal pannello centrale, ciò per via del fatto
	  che questo certamente non potrà esser spostato.
	- Passo fondamentale della gran parte degli algoritmi di risoluzione del Cubo di Rubik è quello
	  di creare una "croce" su una faccia del cubo composta dal pannello centrale e dai pannelli
	  cosiddetti "vertici" che occupano le posizioni centrali delle righe e delle colonne della faccia.
	- Ovviamente, anche i pannelli detti "spigoli" agli angoli delle facce hanno influenza sulla 
	  vicinanza della configurazione alla soluzione finale del rompicapo, va dunque tenuto conto del
	  numero di questi.
Dalle considerazioni è dunque emersa la seguente "classifica di convenienza" di una faccia:
	CONFIGURAZIONE:																	PUNTEGGIO:
	 1) 4 vertici & 4 spigoli dello stesso colore del centro ( faccia conclusa )		1
	 2) 4 vertici & 3 spigoli dello stesso colore del centro							2
	 3) 4 vertici & 2 spigoli dello stesso colore del centro							3
	 4) 4 vertici & 1 spigolo dello stesso colore del centro							4
	 5) 3 vertici & 4 spigoli dello stesso colore del centro							5
	 6) 3 vertici & 3 spigoli dello stesso colore del centro							6
	 7) 3 vertici & 2 spigoli dello stesso colore del centro							7
	 8) 3 vertici & 1 spigolo dello stesso colore del centro							8
	 9) 2 vertici & 4 spigoli dello stesso colore del centro							9
	10) 2 vertici & 3 spigoli dello stesso colore del centro							10
	11) 2 vertici & 2 spigoli dello stesso colore del centro							11
	12) 2 vertici & 1 spigolo dello stesso colore del centro							12
	13) 1 vertice & 4 spigoli dello stesso colore del centro							13
	14) 1 vertice & 3 spigoli dello stesso colore del centro							14
	15) 1 vertice & 2 spigoli dello stesso colore del centro							15
	16) 1 vertice & 1 spigolo dello stesso colore del centro							16
	17) 4 vertici dello stesso colore del centro										17
	18) 4 spigoli dello stesso colore del centro										18
	19) 3 vertici dello stesso colore del centro										19
	20)	3 spigoli dello stesso colore del centro										20
	21) 2 vertici dello stesso colore del centro										21
	22) 2 spigoli dello stesso colore del centro										22
	23) 1 vertice dello stesso colore del centro										23
	24) 1 spigolo dello stesso colore del centro										24
Terminata la valutazione per ogni faccia, il valore euristico assegnato ad ogni configurazione del cubo è dato
semplicemente dalla somma delle valutazioni delle facce che sarà minimo a cubo completo.

STRUTTURA DELL'INPUT:
Ogni faccia del cubo ( matrice ) è in realtà implementata tramite array unidimensionale ( lista ), l'inserimento
dei valori iniziali va dunque eseguito immaginando di inserire i valori considerando frontalmente ogni faccia
a partire dal tassello più in alto a sinistra fino al tassello più in basso a destra.
Ad esempio, per impostare un cubo avente faccia frontale composta da tutti tasselli rossi ad eccezione della
riga più bassa verde, occorre inserire nella lista "fronte":
	fronte = ['V','V','V','R','R','R','R','R','R']
ottenendo così la faccia frontale del cubo seguente:
				['V', 'V', 'V']
				['R', 'R', 'R']
				['R', 'R', 'R']

OUTPUT:
Nonappena trovata una soluzione, viene stampata la sequenza di configurazioni dall'inizio alla fine.								