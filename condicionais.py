# if condicional
# edad = 17
# if edad >= 18:
#     print("Você é maior de idade")
# else:
#     print("Você é menor de idade")

# como fazer para pedir a idade e que possa ser escrita
edad = int(input("Digite sua idade: "))
if edad >= 0 and edad <= 12:
    print("Você é uma criança")
elif edad >= 13 and edad <= 17:
    print("Você é um adolescente")
elif edad >= 18 and edad <= 59:
    print("Você é um Adulto")
else:
    print("Você é um idoso")
