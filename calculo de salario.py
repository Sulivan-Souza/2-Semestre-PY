nome = input("Digite o nome do Funcionario: ")
if len(nome) > 80:
    print("Nome invalido")
else:
    sal_bruto = float(input("Digite o valor do Salario Bruto: "))

    if sal_bruto > 0:
        if sal_bruto > 0 and sal_bruto <= 1302.00:
            INSS = (7.5 * sal_bruto) / 100
            porcentagem = 7.5
        elif sal_bruto > 1302.00 and sal_bruto <= 2571.29:
            INSS = (9 * sal_bruto) / 100
            porcentagem = 9
        elif sal_bruto > 2571.29 and sal_bruto <= 3856.94:
            INSS = (12 * sal_bruto) / 100
            porcentagem = 12
        elif sal_bruto > 3856.94 and sal_bruto <= 7507.49:
            INSS = (14 * sal_bruto) / 100
            porcentagem = 14
        else:
            print("Valor invalido")
            quit()

        sal_liquido = sal_bruto - INSS

        print("\nFuncionario: ", nome)
        print("Salario Bruto e de: R$ %.2f" % sal_bruto)
        print("Valor da porcentagem de desconto e: %.2f%%" % porcentagem)
        print("INSS a ser descontado e de: R$ %.2f" % INSS)
        print("Salario Liquido e de: R$ %.2f" % sal_liquido)
