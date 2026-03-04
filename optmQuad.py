from hashtable import Hashtable

def findLargest(lista):
    largest = -1
    counter = 0

    for i in range(0, len(lista)):
        for j in range(0, len(lista)):
            counter += 1
            if(lista[j] > largest):
                largest = lista[j]

    return (largest, counter)

def findLargestHash(hashtable:Hashtable):
    largest = 0
    counter = 0
    for i in range(0, hashtable.tamanho):
        counter += 1
        temp = hashtable.buscar(i)
        if(temp > largest):
            largest = temp

    return (largest, counter)


lista = [1, 2, 3, 4, 56, 6, 7, 8, 9, 10]
result = findLargest(lista)
print(f"Maior numero: {result[0]}")
print(f"Numero de comparações(laços aninhados): {result[1]}")

hashtable = Hashtable(len(lista))
for i in range(0, len(lista)):
    hashtable.inserir(i, i + 10)

resultHash = findLargestHash(hashtable)
print(f"Maior numero: {resultHash[0]}")
print(f"Numero de comparacoes(Hashtable): {resultHash[1]}")
