from grafo import Grafo
from dijkstra import Dijkstra
from busca import Busca

grafo1 = Grafo()
grafo1.ler('fln_pequena.net')
busca = Busca(grafo1,2)
dijkstra = Dijkstra(grafo1,2)