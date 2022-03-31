Entrada = [2, 7, 11, 15]
print("Esses são os números disponíveis:", Entrada)
ValorEscolhido = int(input(
    "Digite o resultado da soma de dois números da lista acima, que o código retornará o indíce da posição da soma: "))
for x in range(len(Entrada)):
    index1 = Entrada[x-1]
    index2 = Entrada[x]
    index3 = Entrada[x-2]
    index4 = Entrada[x-3]

    if (Entrada[x-1]+(Entrada[x]) == ValorEscolhido):
        print(ValorEscolhido, "é a soma de", index1, "+", index2)
        break

    elif (Entrada[x-2]+(Entrada[x]) == ValorEscolhido):
        print(ValorEscolhido, "é a soma de", index3, "+", index2)
        break
    elif (Entrada[x-3]+(Entrada[x]) == ValorEscolhido):
        print(ValorEscolhido, "é a soma de", index4, "+", index2)
        break
