#Aluno: Felipe Dias , Gleibson Vinicius 

import os
import csv
from dataclasses import dataclass

os.system("cls||clear")

@dataclass
class Funcionario:
    nome: str
    cpf: int
    cargo: str
    salario: float

    def exibir_dados(self):
        return f"Nome: {self.nome} | CPF: {self.cpf} | Cargo: {self.cargo} | Salário: R${self.salario:.2f}"

lista_funcionarios = []

def adicionar_funcionario():
    nome = input("Digite seu nome: ")
    cpf = int(input("Digite seu CPF: "))
    cargo = input("Digite seu cargo: ")
    salario = float(input("Digite seu salário: "))
    funcionario = Funcionario(nome, cpf, cargo, salario)
    lista_funcionarios.append(funcionario)
    print("Funcionário adicionado com sucesso!\n")

def listar_funcionarios():
    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado.\n")
    else:
        for funcionario in lista_funcionarios:
            print(funcionario.exibir_dados())
        print()

def excluir_dados():
    nome_para_remover = input("Digite o nome do funcionário que deseja remover: ")
    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_para_remover:
            lista_funcionarios.remove(funcionario)
            print(f"Funcionário '{nome_para_remover}' removido com sucesso.")
            return
    print("Funcionário não encontrado.")

def salvar_dados_txt(nome_arquivo="funcionarios_senai.txt"):
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for f in lista_funcionarios:
            linha = f"{f.nome},{f.cpf},{f.cargo},{f.salario}\n"
            arquivo.write(linha)

def salvar_dados_csv(nome_arquivo="funcionarios_senai.csv"):
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["nome", "cpf", "cargo", "salario"])
        for f in lista_funcionarios:
            escritor.writerow([f.nome, f.cpf, f.cargo, f.salario])

def carregar_dados_txt(nome_arquivo="funcionarios_senai.txt"):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.split(",")
                if len(partes) == 4:
                    nome = partes[0]
                    cpf = int(partes[1])
                    cargo = partes[2]
                    salario = float(partes[3])
                    funcionario = Funcionario(nome, cpf, cargo, salario)
                    lista_funcionarios.append(funcionario)

def carregar_dados_csv(nome_arquivo="funcionarios_senai.csv"):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, mode="r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                if "nome" in linha and "cpf" in linha and "cargo" in linha and "salario" in linha:
                    nome = linha["nome"]
                    cpf = int(linha["cpf"])
                    cargo = linha["cargo"]
                    salario = float(linha["salario"])
                    funcionario = Funcionario(nome, cpf, cargo, salario)
                    lista_funcionarios.append(funcionario)

def exibir_menu():
    continuar = True
    while continuar:
        print("=== MENU FUNCIONÁRIOS ===")
        print("1 - Adicionar Funcionário")
        print("2 - Listar Funcionários")
        print("3 - Excluir Funcionário")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            excluir_dados()
        elif opcao == "4":
            salvar_dados_txt()
            salvar_dados_csv()
            print("Sistema encerrado. Dados salvos.")
            continuar = False
        else:
            print("Opção inválida.\n")

carregar_dados_csv()
carregar_dados_txt()
exibir_menu()
