import heapq

vertices = 6          #numero de vertices
arestas = 9          #numero de arestas

vizinho_saida = [[] * vertices for i in range(vertices)]    # linhas de adjacencias
custo = []                                                  # matriz de custos (pesos)

for i in range(vertices):
    linha = []
    for j in range(vertices):
        if i == j:
            linha.append(0)
        else:
            linha.append(-1)
    custo.append(linha)

infinity = 1
for j in range(arestas):
    a, b, custoab = input().split()  # ler aresta de a até b e seu  custoab custo
    a = int(a)
    b = int(b)
    custoab = int(custoab)
    vizinho_saida[a].append(b)          # b é vizinho  de saida de a
    custo[a][b] = custoab
    infinity = infinity + custoab       # o infinity será a soma de todos os pesos, mais um


marca_vertice = vertices * [0]
L = vertices * [infinity]
L[0] = 0                                # 0 será a raiz do algortimo
H = [(0,0)]                             # cada posição do heap guarda (L(w),w)
for x in range(1,vertices):
    heapq.heappush(H,(L[x],x))          #inicia todos os valores do heap com infinito, as que não são a raiz  ( L[x] -> custo
pai = vertices * [-1]                   # x -> vertice

while H != []:
    custo_min, v = heapq.heappop(H)     # tirar o heap da raiz
    marca_vertice[v] = 1                # quando eu remover eu marco a vertice
    for x in vizinho_saida[v]:          #percorrer os vizinhos de v
        if marca_vertice[x] == 0:
            if L[v] + custo[v][x] < L[x]:     # encontrar a posição de x no heap, se for menor eu atualizo
                for i in range(len(H)):
                    if H[i] == (L[x],x):
                        pos = i
                        break
                L[x] = L[v] + custo[v][x]       # atualizar o valor de L[x]
                H[pos] = (L[x],x)
                heapq._siftdown(H,0,pos)         #atualiza o heap
                pai[x] = v
print(L)
print(pai)

'''
0 1 4
0 2 2
1 3 5
2 1 1
2 3 8
2 4 10
3 4 2
3 5 6
4 5 2 

'''
