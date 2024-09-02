def ordenacao_natural(lista):
    """
    Ordena a lista de forma natural (padrão).
    """
    return sorted(lista)

def ordenacao_customizada(lista, chave):
    """
    Ordena a lista de forma customizada com base na função da chave fornecida.
    """
    return sorted(lista, key=chave)

#Lista de números
lista_numeros = [34, 7, 23, 32, 5, 62]

print("Números original:", lista_numeros)

# Ordenação natural de números
ordenacao_nat_numeros = ordenacao_natural(lista_numeros)
print("Números naturalmente:", ordenacao_nat_numeros)

#Lista de marcas
lista_strings = ["Nike", "Adidas", "Puma", "Fila", "Vans"]

print("\nLista original:", lista_strings)

# Ordenação natural 
ordenacao_nat_strings = ordenacao_natural(lista_strings)
print("Ordenada naturalmente:", ordenacao_nat_strings)

# Ordenação customizada: por comprimento 
ordenacao_custom_strings = ordenacao_customizada(lista_strings, chave=len)
print("Ordenada por comprimento:", ordenacao_custom_strings)

# Ordenação customizada: por ordem alfabética inversa
ordenacao_custom_strings_inversa = ordenacao_customizada(lista_strings, chave=lambda s: s[::-1])
print("Ordem alfabética inversa:", ordenacao_custom_strings_inversa)
