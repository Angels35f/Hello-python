#Jeito inicial de fazer
# meu_dicionario_vacio = dict()
# meu_dicionario_vacio['Eduardo'] = [1.4, 4.5, 5.6]
# meu_dicionario_vacio['Carla'] = [6.7, 7.8, 8.9]
# meu_dicionario_vacio['Gabriel'] = [9.0, 10.1, 11.2]
# #O médio de todos os alunos
# for medio in meu_dicionario_vacio:
#     print(medio, sum(meu_dicionario_vacio[medio]) / 3)
# #Mostra os alunos que tem média maior ou igual a 7 com o uso de for e if.
# for passou in meu_dicionario_vacio:
#     if sum(meu_dicionario_vacio[passou]) / 3 >= 7:
#         print({passou}, "Tem mais de 7 de media e passou

#Jeito mais eficiente e mais limpo
#definir uma função para calcular a média com o parametro notas
def calcular_media(notas):
    return sum(notas) / len(notas)
#definir uma função para imprimir as médias com o parametro dicionario
def imprimir_medias(dicionario):
    for aluno, notas in dicionario.items():
        media = calcular_media(notas)
        print(f"{aluno}: {media:.2f}")
#definir uma função para imprimir os aprovados com o parametro dicionario e media_minima
def imprimir_aprovados(dicionario, media_minima=7):
    for aluno, notas in dicionario.items():
        media = calcular_media(notas)
        if media >= media_minima:
            print(f"{aluno} tem média {media:.2f} e passou")
#dicionario com os alunos e suas notas
meu_dicionario_vazio = {
    'Eduardo': [1.4, 4.5, 5.6],
    'Carla': [6.7, 7.8, 8.9],
    'Gabriel': [9.0, 10.1, 11.2]
}
#imprimir as médias
print("Médias de todos os alunos:")
imprimir_medias(meu_dicionario_vazio)
#imprimir os aprovados
print("\nAlunos aprovados:")
imprimir_aprovados(meu_dicionario_vazio)