def insertion_sort(lista):
    count = 0
    new_lista = lista
    count += 1
    for i in range(1, len(new_lista)):
        count += 2
        chave = new_lista[i]
        count += 1
        j = i - 1
        count += 1
    
        while(j >= 0) and (new_lista[j] > chave):
            count += 4
            new_lista[j + 1] = new_lista[j]
            count += 2
            j -= 1
            count += 1

        new_lista[j + 1] = chave
        count += 1
    count += 1
    print(f"Numero de passos, comparações e deslocamentos: {count}")
    return new_lista 

lista = [3, 2, 1, 40, 0, 37]
new_lista = insertion_sort(lista)
print(new_lista)
lista = [100, 80, 60, 40, 20]
new_lista = insertion_sort(lista)
print(new_lista)
