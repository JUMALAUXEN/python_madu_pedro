def ordenacao_total(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = chave

def main():
    lista = [5, 3, 9, 1, 10, 5, 12, 10, 8]
    
    print("Lista:", lista)
    
    ordenacao_total(lista)
    
    print("Ordenação total:", lista)

if __name__ == "__main__":
    main()
