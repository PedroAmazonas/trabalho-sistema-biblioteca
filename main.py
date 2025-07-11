import sys
import os
sys.path.append(os.path.abspath('modelos'))
from modelos import biblioteca
def menu():
    print("\n--- MENU DA BIBLIOTECA ---")
    print("1. Registrar cliente")
    print("2. Registrar funcionário")
    print("3. Registrar livro")
    print("4. Registrar empréstimo")
    print("5. Registrar devolução")
    print("6. Pesquisar cliente")
    print("7. Pesquisar livro")
    print("8. Pesquisar histórico")
    print("9. Pesquisar funcionário")
    print("10. Registrar coleção")
    print("11. Pesquisar coleção")
    print("0. Sair")
def main():
    b =biblioteca.Biblioteca("Biblioteca",'Rua 1')
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
            id = input("Nome ou CPF: ")
            print(b.pesquisar_cliente(id))
        elif op == "7":
            id = input("Título ou ISBN: ")
            print(b.pesquisar_livro(id))
        elif op == "8":
            id = input("CPF, nome, título ou ISBN: ")
            print(b.pesquisar_historico(id))
        elif op == "9":
            id = input("Nome ou CPF do funcionário: ")
            print(b.pesquisar_funcionario(id))
        elif op == "10":
            nome = input("Nome da coleção: ")
            descricao = input("Descrição: ")
            livros = input("Livros (separados por vírgula): ").split(",")
            print(b.registrar_colecao(nome, descricao, [livro.strip() for livro in livros]))
        elif op == "11":
            nome = input("Nome da coleção: ")
            print(b.pesquisar_colecao(nome))
        elif op == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")
if __name__ == "__main__":
    main()