class Grafo:
    def __init__(self):
        #Vértices é uma lista de objetos do tipo vértice
        self.vertices = []
        #Arestas é uma lista de objetos do tipo Aresta
        self.arestas = []

    def qtdVertices(self):
        return len(self.vertices)

    def qtdArestas(self):
        return len(self.arestas)

    def adicionarVertice(self, vertice):
        self.vertices.append(vertice)

    def adicionarAresta(self, aresta):
        self.arestas.append(aresta)

    def grau(self, vertice):
        #Número de vértices ligados a ele
        grau = 0
        
        for aresta in self.arestas:
            if vertice in aresta.vertices:
                grau +=1

        return grau

    def rotulo(self, vertice):
        #Rotulo ligado a um vértice
        return vertice.rotulo

    def acharVertice(self, index):
        for vertice in self.vertices:
            if int(vertice.index) == int(index):
                return vertice
            
        return None

    def vizinhos(self, vertice):
        #Todos os vértices ligados diretamente a esse vértice
        lista_vizinhos = []
        
        for aresta in self.arestas:
            if vertice == aresta.vertices[0]:
                lista_vizinhos.append(aresta.vertices[1])
            elif vertice == aresta.vertices[1]:
                lista_vizinhos.append(aresta.vertices[0])

        return lista_vizinhos

    def haAresta(self, verticeA, verticeB):
        #Retorna um bool se existe uma aresta entre dois vértices
        if self.getAresta(verticeA, verticeB) == None:
            return False
        else:
            return True

    def getAresta(self, verticeA, verticeB):
        #Retorna a aresta entre o vérticeA e vérticeB e se não existir retonar None
        for aresta in self.arestas:
            if verticeA == aresta.vertices[0] and verticeB == aresta.vertices[1]:
                return aresta
            if verticeA == aresta.vertices[1] and verticeB == aresta.vertices[0]:
                return aresta
                    
        return None

    def peso(self, verticeA, verticeB):
        #Retorna o peso de uma aresta entre vértices A e B, retorna infinto se não exsitir essa aresta
        aresta = self.getAresta(verticeA, verticeB)
        
        if aresta == None:
            return float('int')
        else:
            return aresta.peso


    def ler(self, arquivo):
        #Carrega um grafo a partir de um input especificado
        arq = open(arquivo, 'r')
        linhas = arq.readlines()

        flag_vertices = False
        flag_arestas = False

        for linha in linhas:
                        
            if '*vertices' in linha:
                lista_linha = linha.split(' ')
                flag_vertices = True

            elif '*edges' in linha:
                lista_linha = linha.split(' ')
                flag_vertices = False
                flag_arestas = True

            elif flag_vertices:
                lista_linha = linha.split(' ')
                vertice = Vertice(lista_linha[0], lista_linha[1])
                self.adicionarVertice(vertice)

            elif flag_arestas:
                lista_linha = linha.split(' ')
                aresta = Aresta([int(lista_linha[0]), int(lista_linha[1])], lista_linha[2])
                self.adicionarAresta(aresta)

    def print(self):
        print("\nPrint do Grafo ------------")
        print("Vértices: --------")
        for vertice in self.vertices:
            print(f"Index: {vertice.index} / Vértice {vertice.rotulo}")
        print("Arestas: ---------")
        for aresta in self.arestas:
            print(f"Aresta: {aresta.vertices} / Peso: {aresta.peso}")

class Vertice:
    def __init__(self, index, rotulo):
        self.index = int(index)
        self.rotulo = rotulo

class Aresta:
    def __init__(self, vertices, peso):
        #o atributo vértices de arestas é uma tupla de vértices (rótulo)
        self.vertices = vertices
        self.peso = int(peso)
