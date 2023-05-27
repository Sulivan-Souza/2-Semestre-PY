import os

def calc_fahrenheit(celsius):
    fahrenheit = 0.0
    if celsius >= -32 and celsius <= 480:
        fahrenheit = (celsius * 1.8) + 32
    else:
        fahrenheit = -998
    return fahrenheit

def calc_celsius(fahrenheit):
    celsius = 0.0
    if fahrenheit >= -32 and fahrenheit <= 480:
        celsius = (fahrenheit - 32) / 1.8
    else:
        celsius = -999
    return celsius

opcao = 1
while opcao != 0:
    os.system("cls" if os.name == "nt" else "clear")
    print("  |-----------------------------------------------------------|")
    print("  |                                                           |")
    print("  |        #####   Conversao de Temperatura   #####           |")
    print("  |                                                           |")
    print("  |                 Celsius para Fahrenheit  =  Opcao  -  1   |")
    print("  |                                                           |")
    print("  |                 Fahrenheit para Celsius  =  Opcao  -  2   |")
    print("  |                                                           |")
    print("  |                 Sair                     =  Opcao   - 0   |")
    print("  |                                                           |")
    print("  |-----------------------------------------------------------|")
    print("\n Escolha uma opcao para continuar, ou Digite '0' para Sair: ")
    opcao = int(input())
    
    if opcao == 1:
        os.system("cls" if os.name == "nt" else "clear")
        print("Celsius para Fahrenheit\n")
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = calc_fahrenheit(celsius)
        if fahrenheit == -998:
            print("\nValor invalido!")
        else:
            print("\nA temperatura em Fahrenheit e: %.2f" % fahrenheit)
        input("\nDigite uma tecla para continuar")
    
    elif opcao == 2:
        os.system("cls" if os.name == "nt" else "clear")
        print("Fahrenheit para Celsius\n")
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = calc_celsius(fahrenheit)
        if celsius == -999:
            print("\nValor invalido!")
        else:
            print("\nA temperatura em Celsius e: %.2f" % celsius)
        input("\nDigite uma tecla para continuar")
    
    elif opcao == 0:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nSaindo do programa...")
        input("\ndigite uma tecla para continuar")
    
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nOpcao invalida!")
        input("\ndigite uma tecla para continuar")
