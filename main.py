import sys
import os
from time import sleep
sys.path.append(os.path.abspath('modelos'))
from modelos.biblioteca import Biblioteca,Colecao
def menu():
    print("\n CLI DA BIBLIOTECA ")
    print("1. Registrar cliente")
    print("2. Registrar funcionário")
    print("3. Registrar livro")
    print("4. Registrar empréstimo")
    print("5. Registrar devolução")
    print("6. Listar clientes")
    print("7. Listar livro")
    print("8. Listar emprestimos e devoluções")
    print("9. Listar funcionários")
    print("10. Registrar coleção")
    print("11. Listar coleções")
    print("0. Sair")
def main():
    b =Biblioteca("Biblioteca",'Rua 1')
    c=Colecao()
    while True:
        menu()
        op = input("Escolha uma opção: ")
        if op == "1":
            nome = input("Nome do cliente: ")
            idade = input("Idade: ")
            cpf = input("CPF: ")
            b.registrar_cliente(nome, idade, cpf)
        elif op == "2":
            nome = input("Nome do funcionário: ")
            idade = input("Idade: ")
            cpf = input("CPF: ")
            salario = input("Salário: ")
            b.registrar_funcionario(nome, idade, cpf, salario)
        elif op == "3":
            titulo = input("Título do livro: ")
            ano = input("Ano de publicação: ")
            isnb = input("ISBN: ")
            b.registrar_livro(titulo, ano, isnb)
        elif op == "4":
            cpf = input("CPF ou nome do cliente: ")
            titulo = input("Título ou ISBN do livro: ")
            print(b.registrar_emprestimo(cpf, titulo))
        elif op == "5":
            cpf = input("CPF ou nome do cliente: ")
            titulo = input("Título ou ISBN do livro: ")
            print(b.registrar_devolucao(cpf, titulo))
        elif op == "6":
            print(b.listar_clientes())
            sleep(3)
        elif op == "7":
            print(b.listar_livros())
            sleep(3)
        elif op == "8":     
            print(b.listar_emprestimos())
            sleep(3)
        elif op == "9":
            print(b.listar_funcionarios())
            sleep(3)
        elif op == "10":
            nome = input("Nome da coleção: ")
            descricao = input("Descrição: ")
            livros = input("Livros (separados por vírgula): ").split(",")
            print(c.registrar_colecao(nome, descricao, [livro.strip() for livro in livros]))
            sleep(3)
        elif op == "11":
            print("Coleções")
            print(c.listar_colecoes())
            sleep(3)
        elif op == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()