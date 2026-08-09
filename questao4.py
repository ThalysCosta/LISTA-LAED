class P:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None


class ListaEncadeada:
    def __init__(self):
        self.p = None

    def inserir_fim(self, valor):
        novo = P(valor)
        if self.p is None:
            self.p = novo
            return
        atual = self.p
        while atual.prox is not None:
            atual = atual.prox
        atual.prox = novo

    def duplicar_impares(self):
        atual = self.p
        while atual is not None:
            if atual.valor % 2 != 0:
                copia = P(atual.valor)
                copia.prox = atual.prox
                atual.prox = copia
                atual = copia.prox
            else:
                atual = atual.prox

    def __str__(self):
        valores = []
        atual = self.p
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.prox
        return " -> ".join(valores) if valores else "(lista vazia)"


if __name__ == "__main__":
    lista = ListaEncadeada()
    for v in [2, 7, 6, 3]:
        lista.inserir_fim(v)

    print("Antes:", lista)