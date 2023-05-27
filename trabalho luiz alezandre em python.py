import os

class Pessoa:
    num = 1

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.num = Pessoa.num
        Pessoa.num += 1

def validarNome(nome):
    return nome.isalpha()

def validarIdade(idade):
    return idade.isdigit() and int(idade) > 0

def validarSalario(salario):
    try:
        float(salario)
        return True
    except ValueError:
        return False

def adicionarPessoa():
    os.system("cls" if os.name == "nt" else "clear")
    print("-- ADICIONAR PESSOA --\n\n")
    print("Digite as informações da pessoa:")
    nome = input("Digite o nome: ")
    if not validarNome(nome):
        print("Nome inválido. Digite apenas caracteres alfabéticos.")
        input("\nDigite uma tecla para continuar")
        return
    idade = input("Digite a idade: ")
    if not validarIdade(idade):
        print("Idade inválida. Digite apenas números positivos.")
        input("\nDigite uma tecla para continuar")
        return
    salario = input("Digite o salário: ")
    if not validarSalario(salario):
        print("Salário inválido. Digite um valor numérico válido.")
        input("\nDigite uma tecla para continuar")
        return
    pessoa = Pessoa(nome, int(idade), float(salario))
    pessoas.append(pessoa)
    os.system("cls" if os.name == "nt" else "clear")
    print("\nPessoa adicionada com sucesso!\n")
    input("\nDigite uma tecla para continuar")

def listarRegistros():
    os.system("cls" if os.name == "nt" else "clear")
    print("-- LISTAR REGISTROS --\n\n")
    if len(pessoas) == 0:
        print("Nenhum registro encontrado")
        input("\nDigite uma tecla para retornar")
    else:
        print("| %-10s |%-30s | %10s | %10s |" % ("Num", "Nome", "Idade", "Salario"))
        for pessoa in pessoas:
            print(
                "| %-10i |%-30s | %10i | %10.2f |"
                % (pessoa.num, pessoa.nome, pessoa.idade, pessoa.salario)
            )
        input("\nDigite uma tecla para continuar")

def alterarRegistros():
    os.system("cls" if os.name == "nt" else "clear")
    print("-- ALTERAR REGISTRO --\n\n")
    if len(pessoas) == 0:
        print("Nenhum registro encontrado")
        input("\nDigite uma tecla para retornar")
    else:
        print("Digite o nome da pessoa que deseja alterar:")
        nome = input()
        encontrada = False
        for pessoa in pessoas:
            if pessoa.nome.lower() == nome.lower():
                encontrada = True
                print(
                    "| %-10s |%-30s | %10s | %10s |" % ("Num", "Nome", "Idade", "Salario")
                )
                print(
                    "| %-10i |%-30s | %10i | %10.2f |"
                    % (pessoa.num, pessoa.nome, pessoa.idade, pessoa.salario)
                )
                print("\nDigite as novas informações da pessoa:")
                novo_nome = input("Digite o novo nome: ")
                if not validarNome(novo_nome):
                    print("Nome inválido. Digite apenas caracteres alfabéticos.")
                    input("\nDigite uma tecla para continuar")
                    return
                nova_idade = input("Digite a nova idade: ")
                if not validarIdade(nova_idade):
                    print("Idade inválida. Digite apenas números positivos.")
                    input("\nDigite uma tecla para continuar")
                    return
                novo_salario = input("Digite o novo salário: ")
                if not validarSalario(novo_salario):
                    print("Salário inválido. Digite um valor numérico válido.")
                    input("\nDigite uma tecla para continuar")
                    return
                pessoa.nome = novo_nome
                pessoa.idade = int(nova_idade)
                pessoa.salario = float(novo_salario)
                os.system("cls" if os.name == "nt" else "clear")
                print("\nRegistro alterado com sucesso!\n")
                input("\nDigite uma tecla para continuar")
                break
        if not encontrada:
            print("\nPessoa não encontrada")
            input("\nDigite uma tecla para continuar")

def removerRegistros():
    os.system("cls" if os.name == "nt" else "clear")
    print("-- REMOVER REGISTRO --\n\n")
    if len(pessoas) == 0:
        print("Nenhum registro encontrado")
        input("\nDigite uma tecla para retornar")
    else:
        print("Digite o nome da pessoa que deseja remover:")
        nome = input()
        encontrada = False
        for pessoa in pessoas:
            if pessoa.nome.lower() == nome.lower():
                encontrada = True
                print(
                    "| %-10s |%-30s | %10s | %10s |" % ("Num", "Nome", "Idade", "Salario")
                )
                print(
                    "| %-10i |%-30s | %10i | %10.2f |"
                    % (pessoa.num, pessoa.nome, pessoa.idade, pessoa.salario)
                )
                confirmacao = input("\nTem certeza que deseja remover? (s/n) ")
                if confirmacao.lower() == "s":
                    pessoas.remove(pessoa)
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\nRegistro removido com sucesso!\n")
                    input("\nDigite uma tecla para continuar")
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\nRemoção cancelada.\n")
                    input("\nDigite uma tecla para continuar")
                break
        if not encontrada:
            print("\nPessoa não encontrada")
            input("\nDigite uma tecla para continuar")

def salvarEmTexto():
    os.system("cls" if os.name == "nt" else "clear")
    print("-- SALVAR EM TEXTO --\n\n")
    if len(pessoas) == 0:
        print("Nenhum registro encontrado")
        input("\nDigite uma tecla para retornar")
    else:
        nome_arquivo = input("Digite o nome do arquivo de texto para salvar: ")
        if nome_arquivo.strip() == "":
            print("Nome de arquivo inválido. Digite um nome válido.")
            input("\nDigite uma tecla para retornar")
            return
        if not nome_arquivo.lower().endswith('.txt'):
            nome_arquivo += '.txt'

        try:
            with open(nome_arquivo, "w") as arquivo:
                arquivo.write("| %-10s |%-30s | %10s | %10s |\n" % ("Num", "Nome", "Idade", "Salario"))
                for pessoa in pessoas:
                    arquivo.write(
                        "| %-10i |%-30s | %10i | %10.2f |\n"
                        % (pessoa.num, pessoa.nome, pessoa.idade, pessoa.salario)
                    )
            os.system("cls" if os.name == "nt" else "clear")
            print("\nRegistros salvos com sucesso no arquivo: %s\n" % nome_arquivo)
            input("\nDigite uma tecla para continuar")
        except IOError:
            os.system("cls" if os.name == "nt" else "clear")
            print("\nErro ao salvar registros no arquivo. Verifique o nome e a permissão do arquivo.\n")
            input("\nDigite uma tecla para continuar")

pessoas = []

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("-- MENU --\n\n")
    print("Selecione uma opção:")
    print("1 - Adicionar pessoa")
    print("2 - Listar registros")
    print("3 - Alterar registro")
    print("4 - Remover registro")
    print("5 - Salvar em texto")
    print("0 - Sair")
    opcao = input("\nDigite o número da opção desejada: ")
    if opcao == "1":
        adicionarPessoa()
    elif opcao == "2":
        listarRegistros()
    elif opcao == "3":
        alterarRegistros()
    elif opcao == "4":
        removerRegistros()
    elif opcao == "5":
        salvarEmTexto()
    elif opcao == "0":
        os.system("cls" if os.name == "nt" else "clear")
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("\nOpção inválida. Digite um número válido.")
        input("\nDigite uma tecla para continuar")