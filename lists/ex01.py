"""
E uma lista de lstas de numeros inteiros
As listas internas tem o tamanho de 10 elementos
As listas internas contem numeros entre 1 a 10 e eles podem ser duplicados

Exerciocio

Crie uma funcao que encontra os dois primeiros numeros duplicados na lista
interna
        Requisistos:
            A ordem dos numeros duplicados e considerada a partir
            da segunda ocorrencia (o numero duplicado em si).
            Exemplo: [1, 2, 3, ->3<-, 2, 1] 3
            Se nao encontrar duplicados na lista, retorne -1

"""



lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 7],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

nova_lista = []

lista = ['Ola', 'Maconha', 1,2,3, 'xereca']

def remove_numbers_from_list(lista):
    for item in lista:
        if item is not int:
            nova_lista.append(item)
        else:
            return


if __name__ == '__main__':
    remove_numbers_from_list(lista)
    print()