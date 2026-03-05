def selection_sort(lista):
    new_lista = lista

    for i in range(len(new_lista)):
        min_index = i
        count = 0

        for j in range(i + 1, len(new_lista)):
            count += 1
            if(new_lista[j] < new_lista[min_index]):
                min_index = j

        temp = new_lista[i]
        new_lista[i] = new_lista[min_index]
        new_lista[min_index] = temp

    return new_lista

lista = [3, 2, 1, 4, 5]
new_lista = selection_sort(lista)
print(new_lista)
lista = [50, 40, 30, 1]
new_lista = selection_sort(lista)
print(new_lista)

