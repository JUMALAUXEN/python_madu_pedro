def ordenacao_por_insercao(lista):
    """
    Ordena a lista usando o algoritmo de ordenação por inserção.
    """
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

def ordenar_lista(lista, metodo='natural'):
    """
    Ordena a lista usando o método especificado ('natural' ou 'insercao').
    """
    if metodo == 'natural':
        return sorted(lista)
    elif metodo == 'insercao':
        return ordenacao_por_insercao(lista[:])
    else:
        raise ValueError("Método de ordenação desconhecido. Use 'natural' ou 'insercao'.")

#Lista de números
lista_numeros = [25, 4, 36, 32, 6, 95, 48]

print("Números original:", lista_numeros)

# Ordenação total usando o método natural
ordenacao_nat_numeros = ordenar_lista(lista_numeros, metodo='natural')
print("Números ordenada naturalmente:", ordenacao_nat_numeros)

# Ordenação total usando o método de inserção
ordenacao_ins_numeros = ordenar_lista(lista_numeros, metodo='insercao')
print("Números ordenada por inserção:", ordenacao_ins_numeros)
