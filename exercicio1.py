# desenvolver um script que peça a idade e altura do usuario
# Se a pessoa é maior de idade pode participar
# Mas a pessoa deve medir mais de 1.70m para participar
# se a pessoa não mede 1.70m ela poderá participar se tiver mais de 25 anos
# e se a altura é maior que 1.65m

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
    # if idade >= 18 and altura >= 1.70:
    #    print("Você pode participar")
    # elif idade >= 25 and altura >= 1.65:
    #     print("Você pode participar")
    # else:
    #     print("Você não pode participar")
if idade >=18:
    if altura >= 1.70 or (idade >= 25 and altura >= 1.65):
        print("Você pode participar do time")
    else:
        print("Você não cumpre os requisitos para participar do time")
else:
    print("Só maiores de idade podem participar do time")    
