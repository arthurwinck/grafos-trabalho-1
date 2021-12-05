INF = 9999999999999

def matriz_de_adjacencia(grafo):
    n = grafo.qtdVertices()
    m = grafo.qtdArestas()
    matriz = [[INF for i in range(n)] for j in range(n)]

    for edge in grafo.arestas:
        x = edge.vertices[0]
        y = edge.vertices[1]
        matriz[x-1][y-1] = edge.peso
        matriz[y-1][x-1] = edge.peso

    for i in range(n):  
        matriz[i][i] = 0

    return matriz

def floyd_warshall(grafo):
    matriz_adjancencia = matriz_de_adjacencia(grafo)
    dist = list(map(lambda p: list(map(lambda q: q, p)), matriz_adjancencia))
    n = len(matriz_adjancencia)

    for r in range(n):
        for p in range(n):
            for q in range(n):
                dist[p][q] = min(dist[p][q], dist[p][r] + dist[r][q])
    for i in range(n):
        print("{}:".format(i+1), end="")
        for j in range(n-1):
            print("{},".format(dist[i][j]), end="")
        print(dist[i][n-1])