#mostra como uma variavel é inmutável, ou seja, n pode mudar, sendo que, o tag acaba sendo o mesmo
lista_estudiantes = ['maria', 'edward','josé']
lista_estudiantes_nuevo = lista_estudiantes
lista_estudiantes_nuevo.append ('pepe')
print(lista_estudiantes_nuevo)
print(lista_estudiantes)

#Tupla
def retornar_estudante():
    return 'Angel', 22, 7.5
nome_estudante, idade_estudante, promedio_estudante =   retornar_estudante()
print(nome_estudante)
print(idade_estudante)
print(promedio_estudante)
