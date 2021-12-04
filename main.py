from grafo import Grafo
from dijkstra import Dijkstra
from busca import Busca
from floyd_warshall import *

grafo1 = Grafo()
grafo1.ler('fln_pequena.net')
busca = Busca(grafo1,2)
dijkstra = Dijkstra(grafo1,2)

grafo2 = Grafo()
grafo2.ler("teste.txt")
floyd_warshall(grafo2)
print("\n")
floyd_warshall(grafo1)

# Testar para casos maiores depois 