# a) Sim. Ao final das três etapas, a lista fica totalmente ordenada.

# Na primeira etapa, os primeiros 2n/3 elementos são colocados em ordem.
# Depois, ordenamos os últimos 2n/3 elementos da lista. Como essas duas
# partes possuem uma região em comum de tamanho n/3, elementos que ainda
# estavam fora de posição podem ser deslocados para locais mais adequados.

# Em seguida, ordenamos novamente os primeiros 2n/3 elementos. Essa última
# passagem elimina possíveis inversões que tenham surgido na parte inicial
# durante a segunda etapa.

# Como as regiões ordenadas se sobrepõem, os elementos acabam sendo
# ajustados gradualmente até que toda a lista esteja em ordem crescente.


# b) O algoritmo da bolha possui custo O(m²) para ordenar uma lista com
# m elementos.

# Em cada uma das três etapas, a bolha é aplicada a uma sublista com
# tamanho 2n/3.

# Assim:

# T(n) = O((2n/3)²) + O((2n/3)²) + O((2n/3)²)

# T(n) = 3 · O(4n²/9)

# T(n) = O(12n²/9)

# T(n) = O(4n²/3)

# Ignorando constantes multiplicativas:

# T(n) = O(n²)

# Portanto, o tempo de execução desse procedimento é O(n²).