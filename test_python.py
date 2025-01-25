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
print("O nome é:", nome_estudante)
print("A idade é", idade_estudante)
print("O promedio é:", promedio_estudante)

#Onelineswapping
variable_1 = 1.0
variable_2 = 2.0
#Para mudar o valor entre elas, pode ser usada uma tupla
variable_1, variable_2 = variable_2, variable_1
print(variable_1, variable_2)