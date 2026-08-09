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

    def particionar(self, k):
        cabeca_menor = None
        cauda_menor = None
        cabeca_maior = None
        cauda_maior = None

        atual = self.p
        while atual is not None:
            prox = atual.prox
            atual.prox = None
            if atual.valor <= k:
                if cabeca_menor is None:
                    cabeca_menor = atual
                else:
                    cauda_menor.prox = atual
                cauda_menor = atual
            else:
                if cabeca_maior is None:
                    cabeca_maior = atual
                else:
                    cauda_maior.prox = atual
                cauda_maior = atual
            atual = prox

        if cauda_menor is not None:
            cauda_menor.prox = cabeca_maior
            self.p = cabeca_menor
        else:
            self.p = cabeca_maior

    def __str__(self):
        valores = []
        atual = self.p
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.prox
        return " -> ".join(valores) if valores else "(lista vazia)"


if __name__ == "__main__":
    lista = ListaEncadeada()
    for v in [9, 2, 5, 6, 1]:
        lista.inserir_fim(v)

    k = 5
    print("Antes:", lista)
    lista.particionar(k)
    print(f"Depois (k={k}):", lista)


# b) Analise o tempo de execucao do seu algoritmo.
#
# O algoritmo percorre a lista uma unica vez, e para cada no realiza
# apenas operacoes de custo constante (comparar com k e religar
# ponteiros em uma das duas sublistas). Logo, o tempo de execucao e
# O(n), onde n e o numero de nos da lista. O espaco extra utilizado e
# O(1), pois os nos existentes sao reaproveitados, sem criacao de
# novos nos.