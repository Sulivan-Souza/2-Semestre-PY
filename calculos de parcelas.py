def calculaParcela(totalDivida, qtdParcelas):
    if qtdParcelas > 0:
        if totalDivida > 0:
            resultado = totalDivida / qtdParcelas
            return resultado
        else:
            resultado = -998
            return resultado
    else:
        resultado = -999
        return resultado

totalDivida = float(input("Digite o total da divida: "))
qtdParcelas = int(input("Digite a quantidade de parcelas: "))

resultado = calculaParcela(totalDivida, qtdParcelas)

if resultado == -999:
    print("Quantidade de parcelas deve ser maior que zero.")
elif resultado == -998:
    print("Total da divida deve ser maior que zero.")
else:
    print("O valor da parcela é: %.2f" % resultado)
