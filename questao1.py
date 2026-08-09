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

    def mover_maior_para_fim(self):
        if self.p is None or self.p.prox is None:
            return

        prev_max = None
        max_no = self.p

        prev = self.p
        atual = self.p.prox

        while atual is not None:
            if atual.valor > max_no.valor:
                max_no = atual
                prev_max = prev
            prev = atual
            atual = atual.prox

        ultimo = prev

        if max_no is ultimo:
            return

        if prev_max is None:
            self.p = max_no.prox
        else:
            prev_max.prox = max_no.prox

        max_no.prox = None
        ultimo.prox = max_no

    def __str__(self):
        valores = []
        atual = self.p
        while atual is not None:
            valores.append(str(atual.valor))
            atual = atual.prox
        return " -> ".join(valores) if valores else "(lista vazia)"


if __name__ == "__main__":
    lista = ListaEncadeada()
    for v in [5, 8, 13, 2, 10]:
        lista.inserir_fim(v)

    print("Antes:", lista)
    lista.mover_maior_para_fim()
    print("Depois:", lista)

# b) Analise o tempo de execucao do seu algoritmo.
#
# O algoritmo faz uma unica passada pela lista para encontrar o maior
# valor, seu predecessor e o ultimo no, custando O(n), onde n e o
# numero de nos da lista. A remocao e reinsercao do no sao O(1), pois
# envolvem apenas religar ponteiros. Logo, o tempo total e O(n).
# O espaco extra utilizado e O(1), ja que nenhuma estrutura auxiliar
# proporcional a n e criada.