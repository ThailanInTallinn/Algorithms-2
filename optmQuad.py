def findLargest(lista):
    largest = -1
    counter = 0

    for i in range(0, len(lista)):
        for j in range(0, len(lista)):
            counter += 1
            if(lista[j] > largest):
                largest = lista[j]

    return (largest, counter)

class Hashtable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _funcao_hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave, valor):
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]

        for i, (chave_ex, _) in enumerate(bucket):
            if(chave_ex == chave):
                bucket[i] = (chave, valor)
                return 
            
        bucket.append((chave, valor))



    def buscar(self, chave):
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]

        for chave_ex, valor in bucket:
            if(chave_ex == chave):
                return valor

        return None

    def remover(self, chave):
        index = self._funcao_hash(chave)
        bucket = self.tabela[index]

        for i, (chave_ex, valor) in enumerate(bucket):
            if chave_ex == chave:
                del bucket[i]

        return None

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
