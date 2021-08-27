def initialize_matriz():
    for i in range(vertice):
        newLine = []
        for j in range(vertice):
            newLine.append(0)
        graph.append(newLine)


def print_graph():
    print('MATRIZ ADJACÊNCIA')
    for i in range(vertice):
        for j in range(vertice):
            print(graph[i][j], end=" ")
        print("")


def add_arestas():
    for i in range(vertice):
        for j in range(vertice):
            if (i == 1) | (i == 2):
                if (j != 1) & (j != 2):
                    graph[i-1][j-1] = 1
            elif (i == 3) | (i == 4):
                if (j != 3) & (j != 4):
                    graph[i-1][j-1] = 1
            else:
                if (j != 0) & (j != 5):
                    graph[i-1][j-1] = 1


def lista_Adjacentes(graph):
    print('\nLISTA ADJACÊNCIA')
    for i in range(vertice):
            print('')
            print( 'vétice' ,i + 1, ' : adjacentes -> ', end=' ')
            for j in range(vertice):
                if graph[i][j] == 1:
                    print(j+1, end=' ')

graph = []
vertice = 6
print("Criando grafo...")

initialize_matriz()
add_arestas()

print_graph()
lista_Adjacentes(graph)