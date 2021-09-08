import heapq

n = 6           #numero de vertices
m = 8           #numero de arestas

H = []

for i in range(m):
    vertice1,vertice2,custo1To2 = input().split()           #ler aresta de vertice1 até vertice2 e seu  custo custo1To2
    vertice1 = int(vertice1)
    vertice2 = int(vertice2)
    custo1To2 = int(custo1To2)
    heapq.heappush(H,(custo1To2,vertice1,vertice2))     #coloca aresta no heap

Conjunto = [[] * n for i in range(n)]                      #criar conjuntos

for i in range(n):
        Conjunto[i].append(i)                              #cada conjunto1[i] é inicializado com [i]

Array = []
for i in range(n):
    Array.append(i)                                     #Array[i] é o conjunto  ao qual o vertice i pertence

cont = 0
custo = 0

while cont < n-1:                                           #basta n-1 arestas
    custo1To2, vertice1, vertice2 = heapq.heappop(H)    #remover  a próxima  aresta do heap
    if Array[vertice1] != Array[vertice2]:                  #as arestas unem arvores diferentes, eu adiciono uma nova aresta
        custo = custo + custo1To2
        p = Array[vertice1]
        q = Array[vertice2]
        if q < p:
            p, q = q, p
        for j in Conjunto[q]:
            Array[j] = p
        Conjunto[p].extend(Conjunto[q])                   #união de conjuntos Conjunto[p] com Conjunto[q]
        Conjunto[q] = []                                   #esvaziar Conjunto[q]
        cont = cont + 1
        print(Conjunto)
        print(Array)
print(custo)

'''
0 1 4
1 2 8
2 3 7
2 5 5
3 4 9
0 4 14
5 3 2
0 5 1
'''
