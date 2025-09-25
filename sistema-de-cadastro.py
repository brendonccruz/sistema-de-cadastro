'''
    Exercício 5: Sistema de Cadastro de Funcionários

    Objetivo: Criar, gerenciar e listar objetos de uma classe usando laços.

    a) Crie uma classe Funcionario com os atributos nome, cargo e salario.
    b) Adicione um método aumentar_salario(self, percentual) que aumenta o salário do funcionário de acordo com um percentual.
    c) Crie uma lista vazia chamada equipe.
    d) Implemente um menu interativo usando um laço while com as seguintes opções:
        [1] Adicionar um novo funcionário (pedir nome, cargo e salário e criar um
        objeto Funcionario para adicionar à lista equipe).
        [2] Listar todos os funcionários (use um laço for para percorrer a
        lista equipe e imprimir os dados de cada um).
        [3] Aumentar o salário de um funcionário (pedir o nome do funcionário e o percentual,
        encontrar o funcionário na lista e chamar o método aumentar_salario).
        [Sair] Para sair do programa.
'''

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
    def aumentar_salario (self, percentual):
        self.salario += self.salario * (percentual/100)
        print(f"Seu novo salário com um aumento de {percentual}% é de R$ {self.salario:.2f}")

equipe = []

def cadastrar_funcionario():
        nome_nf = input("Qual o nome do novo funcionário? ")
        cargo_nf = input(f"Qual o cargo exercido por {nome_nf}? ")
        salario_nf = float(input(f"Informe o salário de {nome_nf}. R$"))

        novofuncionario = Funcionario(nome_nf, cargo_nf, salario_nf)
        equipe.append(novofuncionario)

def menu():
    while True:
        print("[1] Adicionar um novo funcionário")
        print("[2] Listar todos os funcionários")
        print("[3] Aumentar o salário de um funcionário")
        print("[Sair] Para sair do programa.")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_funcionario()
            repetir = input("Deseja cadastrar mais um funcionário? Digite 1 para sim, ou 2 para não: ")
            while repetir != "2":
                cadastrar_funcionario()
                repetir = input("Deseja cadastrar mais um funcionário? Digite 1 para sim, ou 2 para não: ")
                if repetir == "2":
                    break
        if opcao == "2":
            if not equipe:
                print("Nenhum funcionário foi cadastrado.")
            else:
                for funcionario in equipe:
                    print(f"Nome do Funcionário: {funcionario.nome}, Cargo: {funcionario.cargo}, Salário: R${funcionario.salario}")
        if opcao == "3":
            pesquisar = input("Qual funcionário deseja aplicar o aumento de salário? ")

            encontrado = False

            for funcionario in equipe:
                if pesquisar == funcionario.nome:
                    try:
                        print("Funcionário Encontrado.")
                        print(f"Nome do Funcionário: {funcionario.nome}, Cargo: {funcionario.cargo}, Salário: {funcionario.salario}")
                        percentual = int(input("Digite o percentual desse aumento: "))
                        funcionario.aumentar_salario(percentual)
                        print(f"Salário de {funcionario.nome} aumentado com sucesso!")
                        break
                    except ValueError:
                        print("Percentual inválido. Tente novamente.")
                        break
                if not encontrado:
                    print("Funcionário não encontrado.")
        if opcao == "3":
            print("Obrigado por utilizar o programa.")

menu()