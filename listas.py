Lista_numeros = [1, 2, 3]
#listas podem ser heterogêneas
Lista_numeros[2] = "três"
print(Lista_numeros)
#apped adiciona um elemento ao final da lista
Lista_numeros.append(4)
Lista_numeros.append(4)
Lista_numeros.append(4)
print(Lista_numeros)
#remove remove um elemento da lista
Lista_numeros.remove(4)
print(Lista_numeros)
#coutn conta quantas vezes um elemento aparece na lista
print(Lista_numeros.count(4))
#extend adiciona uma lista a outra
lista_extendida = [5, 6, 7]

Lista_numeros.extend(lista_extendida)
print(Lista_numeros)   
#index retorna o índice de um elemento
print(Lista_numeros.index(5))
#insert insere um elemento em uma posição específica
print(Lista_numeros)
Lista_numeros.insert(0, 5000)
print(Lista_numeros)
#pop remove um elemento de uma posição específica
print(Lista_numeros)
print(Lista_numeros.pop(0))
print(Lista_numeros)
#remove remove um elemento específico
print(Lista_numeros)
Lista_numeros.remove(5)
print(Lista_numeros)   
#reverse inverte a lista
print(Lista_numeros)
Lista_numeros.reverse()
print(Lista_numeros)     
#clear limpa a lista
Lista_numeros.clear()
print(Lista_numeros)
#sort ordena a lista
lista_desordeada = [5, 3, 1, 4, 2]	
print(lista_desordeada)
lista_desordeada.sort()
print(lista_desordeada)
