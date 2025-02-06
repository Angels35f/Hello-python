#declaracion
meu_set = set()
meu_set.add(1)
meu_set.add(2)
meu_set.add(3)
meu_set.add(4)
meu_set.add(4)  
print(meu_set)
#um set não aceita elementos duplicados, pelo que sempre vai apagar 
# o último elemento
lista_numeros = [1, 1, 2, 3, 4, 4, 5, 1, 7]
meu_set_numeros = set(lista_numeros)
print(meu_set_numeros)

pertenece = 3 in meu_set_numeros
print(pertenece)

frutas = {"banana", "maçã", "laranja", "uva", "abacaxi"}
#é criada uma hash table com os elementos da lista.
#frozenset é uma lista imutável
meu_fronzenset = frozenset(frutas)
#meu_fronzenset.add("melancia") não é possível adicionar elementos
print(meu_fronzenset)
