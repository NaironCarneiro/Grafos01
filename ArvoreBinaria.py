class No:
    # Contrutor
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def getValor(self):
        return  self.valor

    def getEsquerda(self):
        return self.esquerda

    def getDireita(self):
        return self.direita

    def setEsquerda(self, esquerda):
        self.esquerda = esquerda

    def setDireita(self, direita):
        self.direita = direita

class ArvoreBinaria:

    def __init__(self):
        self.raiz = None

    def getRaiz(self):
        return  self.raiz

    def inserir(self, valor):
        no = No(valor)
        if self.raiz == None:
            self.raiz = no
        else:
            # No para comparação
            no_atual = self.raiz
            no_pai = None
            while True:
                if no_atual != None:
                    no_pai = no_atual
                    if no.getValor() < no_atual.getValor():
                        no_atual = no_atual.getEsquerda()
                    else:
                        no_atual = no_atual.getDireita()
                else:
                    if (no.getValor() < no_pai.getValor()):
                        no_pai.setEsquerda(no)
                    else:
                        no_pai.setDireita(no)
                    break

    def mostrarValoresEmOrdem(self, no_atual):
        if no_atual != None:
            self.mostrarValoresEmOrdem(no_atual.getEsquerda())
            print(no_atual.getValor(), end = ' ')
            self.mostrarValoresEmOrdem(no_atual.getDireita())

    def mostrarValoresPreOrdem(self, no_atual):
        if no_atual != None:
            print(no_atual.getValor(), end=' ')
            self.mostrarValoresEmOrdem(no_atual.getEsquerda())
            self.mostrarValoresEmOrdem(no_atual.getDireita())

    def mostrarValoresPosOrdem(self, no_atual):
        if no_atual != None:
            self.mostrarValoresEmOrdem(no_atual.getEsquerda())
            self.mostrarValoresEmOrdem(no_atual.getDireita())
            print(no_atual.getValor(), end=' ')

arvore = ArvoreBinaria()

arvore.inserir(5)
arvore.inserir(2)
arvore.inserir(6)
arvore.inserir(4)
arvore.inserir(3)
arvore.inserir(1)
arvore.inserir(7)

print('Em ordem')
arvore.mostrarValoresEmOrdem(arvore.getRaiz())
print('')
print('Pre ordem')
arvore.mostrarValoresPreOrdem(arvore.getRaiz())
print('')
print('Pos ordem')
arvore.mostrarValoresPosOrdem(arvore.getRaiz())