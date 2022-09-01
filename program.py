import albero
from albero import Nodo

#from albero import AlberoBinario

'''
    Es 1: 3 punti
    Si definisca la funzione es7(tree,insieme,k ) ricorsiva (o che fa uso 
    di funzioni o metodi ricorsive/i) che:
    - riceve come argomenti:
      - l'albero 'tree'  formato da nodi del tipo Nodo definito nella libreria 
        albero.py allegata, 
      - un insieme di caratteri 
      - un intero k
    - torna come risultato il numero di nodi dell'albero aventi 
      ESATTAMENTE  k figli i quali hanno  identificatori   
      presenti nell'insieme.
    
    Esempio: sia k=2 e ins={1,2,3,5,9}, allora la funzione es1
    - sull'albero a sinistra deve restituire 2 (per i figli dei nodi 4 e 2)
    - sull'albero a destra deve restituire 3 (per i figli dei nodi 7, 9 e 10).


              5                                     7              
      ________|_____________                _______|______         
     |          |           |              |              |        
     20         4           6              5              9        
     |     _____|______                 ___|___        ___|__      
     11   |   |  |  |  |               |       |      |      |     
          10  2  9  8  7               10      8      3      1     
            __|__                     _|_     _|_    _|_    _|_    
           |     |                   |   |   |   |  |   |  |   |   
           3     1                   1   2   12  13 15  6  4   0   
                                                                   
    '''
'''
class Nodo:
    def __init__(self,V):
        self.id=V
        self.f=[]
 '''       
        

def es7(tree,insieme,k):
  
    
    for item in tree.f:
        
        if len(item.f) >= k:
            print("ID:", item.id)
            print("length",len(item.f))
            print("maggiore")
            
            for el1 in item.f:
                print(el1.id)
                
                for i in insieme:
                    print(el1.id," - ",i)

            print("***************")

        es7(item,insieme,k)

        
    pass
    
    
    
    

n12 = Nodo(1)
n11 = Nodo(3)

n10 = Nodo(7)
n9 = Nodo(8)
n8 = Nodo(9)
n7 = Nodo(2)    
n6 = Nodo(10)

n5 = Nodo(11)
n4 = Nodo(6)
n3 = Nodo(4)
n2 = Nodo(20)
n1 = Nodo(5)

n1.f.extend([n2,n3,n4])
n2.f.append(n5)
n3.f.extend([n6,n7,n8,n9,n10])
n7.f.extend([n11,n12])

k = 2
insieme = [1,2,3,5,9]
insieme2 = [20,4]

#print(len(n1.f))

es7(n1,insieme,k)
    
    





















