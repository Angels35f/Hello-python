#com uma clave pode ter acesso a um valor (key) a key deve ser 
# hashable que é mutável
#Como declarar um dicionario
meu_dicionario = {
    'Eduardo': [1.4, 4.5, 5.6], 
    'Carla': [6.7, 7.8, 8.9],
    'Gabriel': [9.0, 10.1, 11.2]
}
print(meu_dicionario)
#dict é uma função que cria um dicionário
meu_dicionario_2 = dict(
    Eduardo = [1.4, 4.5, 5.6], 
    Carla = [6.7, 7.8, 8.9],
    Gabriel = [9.0, 10.1, 11.2])
print(meu_dicionario_2)
#dict_vacio
meu_dicionario_vacio = dict()
meu_dicionario_vacio['Eduardo'] = [1.4, 4.5, 5.6]
meu_dicionario_vacio['Carla'] = [6.7, 7.8, 8.9]
meu_dicionario_vacio['Gabriel'] = [9.0, 10.1, 11.2]
print(meu_dicionario_vacio)

#mostra de como os dicionários são mutáveis
meu_dicionario_vacio['Maria'] = [1.4, 4.5, 5.6]
print(meu_dicionario_vacio)
meu_dicionario_vacio['Maria'] = [6.7, 7.8, 8.9]
del meu_dicionario_vacio['Maria']
print(meu_dicionario_vacio)
#Diferetes vistas keys, values e both 
print(meu_dicionario_vacio.keys())
print(meu_dicionario_vacio.values())
print(meu_dicionario_vacio.items())