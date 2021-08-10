def initialize_matriz():
    for i in range(vertice):
        newLine = []
        for j in range(vertice):
            newLine.append(0)
        graph.append(newLine)

def print_graph():
    for i in range(vertice):
        for j in range(vertice):
            print(graph[i][j], end=" ")
        print("")

def add_arestas():
    print("Me diga quais posições quer adicionar")
    l = int(input("linha:"))
    c = int(input("coluna:"))
    graph[l - 1][c - 1] = 1
    print_graph()
    print("Aresta adicionada com sucesso!!")

grausVertices = []
def grau_graph(dec):
    cont = 0
    for i in range(vertice):
        for j in range(vertice):
            if graph[i][j] == 1:
                cont = cont + 1
        if dec:
            print("a vertice ", i + 1, "é de grau", cont)
        grausVertices.append(cont)
        cont = 0

def grau_minimum():
    minValor = min(grausVertices)
    print("O Grau mínimo do grafo é: ", minValor)

def grau_maximum():
    maxValor = max(grausVertices)
    print("O Grau máximo do grafo é: ", maxValor)

graph = []
vertice = int(input("Digite a quantidade de vértices para o seu grafo: "))
print("Criando grafo...")
initialize_matriz()
print_graph()

menu = True
while menu:
    print("""
    1.Adicionar Arestas
    2.Mostrar Grafo
    3.Grau de cada vértice
    4.Grau Mínimo
    5.Grau Máximo
    0.Sair
    """)
    menu = input("Escolha uma opção:")

    if menu == "1":
        add_arestas()
    elif menu == "2":
        print("\nGrafo com os dados")
        print_graph()
    elif menu == "3":
        grau_graph(True)
    elif menu == "4":
        grau_graph(False)
        grau_minimum()
    elif menu == "5":
        grau_graph(False)
        grau_maximum()
    elif menu == "0":
        exit()
    elif menu !="":
        print("\n Opção Invalida. Tente Novamente")








