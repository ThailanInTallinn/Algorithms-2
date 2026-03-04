from hashtable import Hashtable

def commonElements(listA, listB):
    largest_list = (listA if len(listA) > len(listB) else listB, listB if len(listA) > len(listB) else listA)
    new_list:list[int] = []
    hashtable = Hashtable(len(largest_list[0]))    
    counter = 0
    
    for i in range(0, hashtable.tamanho):
        hashtable.inserir(largest_list[0][i], largest_list[0][i])

    for i in range(0, len(largest_list[1])):
        found:int = hashtable.buscar(largest_list[1][i])     
        counter += 1
        if(found):
            new_list.append(found)
    
    print(f"Passos para localizar cada item da lista menor também presente na lista maior: {counter}")
    return new_list

lista1 = [1, 2, 3]
lista2 = [i + 1 for i in range(0, 100)]
result = commonElements(lista1, lista2)
print(result)
