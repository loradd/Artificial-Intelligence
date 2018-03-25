# Si importano le librerie PyBrain necessarie:
#   a) allenamento della rete basato su Algoritmo di BackPropagation
from pybrain.supervised import BackpropTrainer
#   b) creazione della rete neurale con pesi inizialmente arbitrari
from pybrain.tools.shortcuts import buildNetwork
#   c) predisposizione del contenuto del Data Set
from pybrain.datasets import SupervisedDataSet

# Nuovo Data Set con due valori di input seguiti da un output
dataset = SupervisedDataSet(2, 1)
# Nuova Rete Neurale con un neurone output e due neuroni output
net = buildNetwork(2, 3, 1)
# File di input dal quale recuperare il contenuto del DataSet
dataFile = open('datadata.txt', 'r')
# Lettura Linea per Linea del contenuto di "datadata"
line = dataFile.readline()
while line:
    read = tuple(line.strip().split(','))
    # Creating Dataset from Data File
    dataset.addSample(read[:2], read[2:])
    line = dataFile.readline()

# Fase di allenamento basato su Backpropagation
trainer = BackpropTrainer(net, dataset, verbose=True)

import sys
orig_stdout = sys.stdout
final = file('results/trainingresults.txt', 'w+')
sys.stdout = final
print("Neural Net Test before Training Session:")
# Test Iniziale della rete prima l'addestramento
print(trainer.testOnData(dataset=dataset, verbose=True),)

temp_std_out = sys.stdout
sys.stdout = orig_stdout

##########
trained = False
# Allenamento continua finche' la rete non arriva ad una precisione pari a 0,0000001
acceptableError = 0.0001
while not trained:
    error = trainer.train()
    if error < acceptableError:
        trained = True
##########

sys.stdout = temp_std_out
print("\nNeural Net Test after Training Session:")
# Test Finale della rete dopo l'addestramento
print(trainer.testOnData(dataset=dataset, verbose=True), )
sys.stdout = orig_stdout
final.close()

"""
Codice di stampa del contenuto della rete neurale

for mod in net.modules:
  print "Module:", mod.name
  if mod.paramdim > 0:
    print "--parameters:", mod.params
  for conn in net.connections[mod]:
    print "-connection to", conn.outmod.name
    if conn.paramdim > 0:
       print "- parameters", conn.params
  if hasattr(net, "recurrentConns"):
    print "Recurrent connections"
    for conn in net.recurrentConns:
       print "-", conn.inmod.name, " to", conn.outmod.name
       if conn.paramdim > 0:
          print "- parameters", conn.params
"""
