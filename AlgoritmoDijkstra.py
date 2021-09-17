import math

class HeapMinimo:

    def __init__(self):
        self.nos = 0        # inicia com 0's nós
        self.heap = []      # o heap inicia vazia

    def inserir_no(self, u, indice):    # o u -> é o peso da aresta   // o indice -> o vertice que ta relacionado com aquele peso
        self.heap.append([u, indice])     # adiciono o u e o indice
        self.nos += 1
        son = self.nos                  #o filho recebe o ultimo nó
        while True:
            if son == 1:                # se o filho já tiver na raiz, para
                break
            pos_pai = son // 2           # divide por 2 e pega só a parte inteira da divisão, para saber a posição do pai ( // )
            if self.heap[pos_pai-1][0] <= self.heap[son-1][0]:      #se o pai for menor ele para
                break
            else:
                self.heap[pos_pai-1], self.heap[son-1] = self.heap[son-1], self.heap[pos_pai-1]   #senão, troca a posição
                son = pos_pai

    def remove_no(self):
        x = self.heap[0]
        self.heap[0] = self.heap[self.nos - 1]
        self.heap.pop()
        self.nos -= 1
        pos_pai = 1
        while True:
            son = 2 * pos_pai
            if son > self.nos:
                break
            if son + 1 <= self.nos:
                if self.heap[son][0] < self.heap[son-1][0]:
                    son += 1
            if self.heap[pos_pai-1][0] <= self.heap[son-1][0]:
                break
            else:
                self.heap[pos_pai-1], self.heap[son-1] = self.heap[son-1], self.heap[pos_pai-1]
                pos_pai = son
        return x

    def tamanho(self):
        return self.nos

class Graph:

    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso
        self.grafo[v-1][u-1] = peso

    def mostra_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.vertices):
            print(self.grafo[i])

    def dijkstra(self, origem):
        custo_vem_vertice = [[-1, 0] for i in range(self.vertices)]   #o custo inicial sempre é -1 e vem do 0
        custo_vem_vertice[origem - 1] = [0, origem]                   #o custo vem na posição 0 e apartir da origem
        h = HeapMinimo()                          #h agora é o HeapMinimo
        h.inserir_no(0, origem)
        while h.tamanho() > 0:
            distance, v = h.remove_no()
            for i in range(self.vertices):
                if self.grafo[v-1][i] != 0:         # verifico se já possui adjacencias com esse grafo
                    if custo_vem_vertice[i][0] == -1 or custo_vem_vertice[i][0] > distance + self.grafo[v-1][i]: # verifica se o caminho é de menor custo
                        custo_vem_vertice[i] = [distance + self.grafo[v-1][i], v]                                #daí faz a troca
                        h.inserir_no(distance + self.grafo[v-1][i], i+1)  #adiciona a nova distancia e o vertice relacionado
        return custo_vem_vertice

g = Graph(6)

# g.adiciona_aresta(1, 2, 5)
# g.adiciona_aresta(1, 3, 6)
# g.adiciona_aresta(1, 4, 10)
# g.adiciona_aresta(2, 5, 13)
# g.adiciona_aresta(3, 4, 3)
# g.adiciona_aresta(3, 5, 11)
# g.adiciona_aresta(3, 6, 6)
# g.adiciona_aresta(4, 5, 6)
# g.adiciona_aresta(4, 6, 4)
# g.adiciona_aresta(5, 7, 3)
# g.adiciona_aresta(6, 7, 8)

# g.adiciona_aresta(1, 2, 1)
# g.adiciona_aresta(1, 3, 3)
# g.adiciona_aresta(1, 5, 6)
# g.adiciona_aresta(2, 3, 1)
# g.adiciona_aresta(2, 4, 3)
# g.adiciona_aresta(3, 1, 1)
# g.adiciona_aresta(3, 2, 2)
# g.adiciona_aresta(3, 4, 1)
# g.adiciona_aresta(4, 1, 3)
# g.adiciona_aresta(4, 5, 2)
# g.adiciona_aresta(5, 4, 1)

g.adiciona_aresta(0, 1, 4)
g.adiciona_aresta(1, 2, 8)
g.adiciona_aresta(2, 3, 7)
g.adiciona_aresta(2, 5, 5)
g.adiciona_aresta(3, 4, 9)
g.adiciona_aresta(0, 4, 14)
g.adiciona_aresta(5, 3, 2)
g.adiciona_aresta(0, 5, 1)

g.mostra_matriz()

resultado_dijkstra = g.dijkstra(1)
print(resultado_dijkstra)
