
from grafo import Grafo

def Busca(grafo, vertice):
    if vertice < 0 or vertice >= grafo.qtdVertices():
        print("Impossivel")
        return 0
    
    else:
        visitados = [False] * (grafo.qtdVertices()+1)
        fila = []
        fila.append(vertice)
        distancia = 0
        
        print("Algoritmo de Busca em Largura ------------")
        while len(fila) != 0:
                level = fila.copy()
                fila = []
                for vert in level:
                    v = vert
                    visitados[v] = True
                    vizinhos_false = []
                    
                    for i in grafo.vizinhos(v):
                        if visitados[i] == False:
                            vizinhos_false.append(i)


                    for i in range(len(vizinhos_false)): 
                        visitados[vizinhos_false[i]] = True
                    fila.extend(vizinhos_false)
                
                level = [str(string) for string in level]
                print("%d:" % (distancia), end = ' ')
                print(",".join(level))
                
                distancia += 1

