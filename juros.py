divida = float(input("Qual o valor da dívida? "))
print("")


print("Quantidade de parcelas: 1")
print("Taxa de juros sobre o valor inicial da dívida: 0%")
print("A dívida atualizada é de R$: ", divida)
print("Valor de cada parcela R$: ", divida)
print("")


qnt_parcelas = 0
for qnt_parcelas in range(3, 13, 3):
    print("Quantidade de parcelas: ",qnt_parcelas)

    if qnt_parcelas == 3:
        juros = 10
        valor_com_juros = divida*(juros / 100) + divida

        print("Taxa de juros sobre o valor inicial da dívida: ", juros, "%")
        print("A dívida atualizada é de R$: ", valor_com_juros)
        print("Valor de cada parcela R$:{:.2f}".format(valor_com_juros/qnt_parcelas))
        print("")

    elif qnt_parcelas == 6:
        juros = 15
        valor_com_juros = divida*(juros / 100) + divida

        print("Taxa de juros sobre o valor inicial da dívida: ", juros, "%")
        print("A dívida atualizada é de R$: ", valor_com_juros)
        print("Valor de cada parcela R$:{:.2f}".format(valor_com_juros/qnt_parcelas))
        print("")

    elif qnt_parcelas == 9:
        juros = 20
        valor_com_juros = divida*(juros / 100) + divida

        print("Taxa de juros sobre o valor inicial da dívida: ", juros, "%")
        print("A dívida atualizada é de R$: ", valor_com_juros)
        print("Valor de cada parcela R$:{:.2f}".format(valor_com_juros/qnt_parcelas))
        print("")

    elif qnt_parcelas == 12:
        juros = 25
        valor_com_juros = divida*(juros / 100) + divida

        print("Taxa de juros sobre o valor inicial da dívida: ", juros, "%")
        print("A dívida atualizada é de R$: ", valor_com_juros)
        print("Valor de cada parcela R$:{:.2f}".format(valor_com_juros/qnt_parcelas))
        print("")
