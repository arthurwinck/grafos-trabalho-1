from grafo import Grafo

class No():
    def __init__(self, index):
        self.index = index
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


    def gerarNos(self):
        for vertice in self.grafo.vertices:
            no = No(vertice.index)

            if vertice == self.vertice:
                no.distancia = 0

            self.nos.append(no)

    def checarVisitados(self):
        condicao = True
        
        for no in self.nos:
            if no.visitado == False:
                condicao = False
        
        return condicao

    def verticeDistanciaMin(self):
        verticeMin = None
        distMin = -1

        for no in self.nos:
            if no.visitado == False:
                if distMin == -1:
                    verticeMin = self.grafo.vertices[no.index]
                    distMin = no.distancia
                else:
                    if distMin > no.distancia:
                        verticeMin = self.grafo.vertices[no.index]
                        distMin = no.distancia

        return verticeMin

    def executar(self):
        condicao = self.checarVisitados()
        
        while condicao == False:
            #Descobrir o vértice com menor distância
            # verticeMin = u
            verticeMin = self.verticeDistanciaMin()
            verticeMin.visitado = True

            #Buscar os vizinhos desse vértice
            listaVizinhos = self.grafo.vizinhos(verticeMin)
            
            #foreach
            #vertice = v
            for vertice in listaVizinhos:
                if self.nos[vertice.index].visitado == False:
                    # If Dv > Du + w((u,v))
                    if self.nos[self.vertice.index].distancia > self.nos[verticeMin.index].distancia + self.grafo.getAresta(self.vertice, verticeMin):
                        # Dv = Du + w((u,v))
                        self.nos[self.vertice.index].distancia = self.nos[verticeMin.index].distancia + self.grafo.getAresta(self.vertice, verticeMin)
                        self.nos[self.vertice.index].antecessor = self.nos[self.verticeMin.index]

        return "Ainda preciso implementar"