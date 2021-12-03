from grafo import Grafo

class No():
    def __init__(self, index):
        self.index = int(index)
        #Distância do vértice inicial a esse vértice
        self.distancia = float('inf')
        #Ancestral direto
        self.antecessor = None
        #Boolean que afirma se o caminho foi visitado ou não
        self.visitado = False
        

class Dijkstra():
    def __init__(self, grafo, vertice):
        self.grafo = grafo
        self.verticeI = vertice
        # Lista de objetos nós
        self.nos = []
        self.gerarNos()
        self.executar()

    def gerarNos(self):
        for vertice in self.grafo.vertices:
            no = No(vertice.index)

            if vertice.index == self.verticeI:
                no.distancia = 0

            self.nos.append(no)

    def verticeDistanciaMin(self):
        verticeMin = None
        distMin = -1

        for no in self.nos:
            if no.visitado == False:
                if distMin == -1:
                    verticeMin = no.index
                    distMin = no.distancia
                else:
                    if distMin > no.distancia:
                        verticeMin = no.index
                        distMin = no.distancia

        return verticeMin

    def print(self):
        print("Algoritmo de Dijkstra --------------")
        for no in self.nos:
            if no.antecessor != None:
                print(f"vértice {no.index} | distância {no.distancia} | antecessor {no.antecessor.index}")
            else:
                print(f"vértice {no.index} | distância {no.distancia} | antecessor None")


    def executar(self):
        
        while True:
            
            #Descobrir o vértice com menor distância
            # verticeMin = u
            verticeMin = self.verticeDistanciaMin()
            #Não possuimos mais nenhum vértice para checar
            if verticeMin == None:
                break
            
            self.nos[verticeMin-1].visitado = True

            #Buscar os vizinhos desse vértice
            listaVizinhos = self.grafo.vizinhos(verticeMin)
            print(verticeMin,listaVizinhos)

            #foreach
            #vertice = v
            for vertice in listaVizinhos:
                if self.nos[vertice-1].visitado == False:
                    # If Dv > Du + w((u,v))
                    
                    if  self.grafo.getAresta(vertice, verticeMin) == None:
                        print(vertice, verticeMin)
                        raise Exception

                    if self.nos[vertice-1].distancia > self.nos[verticeMin-1].distancia + self.grafo.getAresta(vertice, verticeMin).peso:
                        # Dv = Du + w((u,v))
                        self.nos[vertice-1].distancia = self.nos[verticeMin-1].distancia + self.grafo.getAresta(vertice, verticeMin).peso
                        self.nos[vertice-1].antecessor = self.nos[verticeMin-1]

        self.print()

        return self.nos