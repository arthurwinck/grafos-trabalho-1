from grafo import Grafo
from dijkstra import Dijkstra
from busca import Busca
from floyd_warshall import *

grafo1 = Grafo()
grafo1.ler('fln_pequena.net')
print(grafo1.peso(2, 3))
print(grafo1.haAresta(2, 3))
print(grafo1.indice_to_vertice[9].grau)
print(grafo1.vizinhos(2))

print("\n")

busca = Busca(grafo1,2)
dijkstra = Dijkstra(grafo1,2)

print("\n")

grafo2 = Grafo()
grafo2.ler("teste.txt")
floyd_warshall(grafo2)
print("\n")
floyd_warshall(grafo1)
