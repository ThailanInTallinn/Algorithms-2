from hashtable import Hashtable


def findDup(lista):
    hashtable = Hashtable(len(lista))
    seen = lista[0]
    i = 0
    for i in range(1, len(lista)):
        hashtable.inserir(i, lista[i])
        if(lista[i] == seen):
            break
    seen = lista[i]
    return (seen, hashtable)

lista = ["oi", "tchau", "ola", "oi", "adeus"]
listaB = ["Flu", "Flu", "Vasco", "Flamengo", "Botafogo"]
result = findDup(lista)
print(result[0])
print(f"Hashtable gerado: {result[1].tabela}")
result = findDup(listaB)
print(result[1].tabela)
