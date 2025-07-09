import livro,pessoa,emprestimo,excecoes
from faker import Faker
import json,os
faker=Faker('pt_BR')
class Colecao:
    def __init__(self,nome,livros,descricao):
        self.nome=nome
        self.livros=livros
        self.descricao=descricao
    def inserir_livro(self,livro):
        self.livros.append(livro)
        return f'Sucesso na inserção do livro {livro} na coleção {self.nome}'
    def remover_livro(self,livro):
        self.livros.remove(livro)
        return f'Sucesso na remoção do livro {livro} na coleção {self.nome}'
    def __str__(self):
        text=f'Nome:{self.nome}|Livros:{self.livros}|Descrição:{self.descricao}'
class Colecao_Autor(Colecao):
    def __init__(self, nome, livros, descricao,autor):
        self.autor=autor
        super().__init__(nome, livros, descricao)
    def __str__(self):
        text=f'Nome:{self.nome}|Livros:{self.livros}|Autor:{self.autor}|Descrição:{self.descricao}'
class Biblioteca():
    def __init__(self, nome=None, endereco=None):
        self.nome = nome or faker.word()
        self.endereco = endereco or faker.address()
    def __str__(self):
        return f'Nome da biblioteca: {self.nome} | endereço: {self.endereco}'
    def _caminho_dados(self):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'json', 'dados.json')
    def verificar_funcionario(self, identificador):
        caminho_json = self._caminho_dados()
        if not os.path.exists(caminho_json):
            return False
        with open(caminho_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return False
        if isinstance(dados, dict):
            dados = [dados]
        for func in dados:
            if func['nome'] == identificador or str(func['cpf']) == str(identificador):
                print(f'Funcionário encontrado: {func}')
                return True
        print(f'Funcionário com nome ou CPF "{identificador}" não encontrado.')
        return False
    def registar_funcionario(self, nome, idade, cpf, salario):
        if self.verificar_funcionario(cpf):
            print("Registro não realizado: funcionário já existe.")
            return
        funcionario = pessoa.Funcionario(nome, idade, cpf, salario)
        funcionario_dict = {
            "nome": funcionario.nome,
            "idade": funcionario.idade,
            "cpf": funcionario.cpf,
            "salario": funcionario.salario
        }
        caminho_json = self._caminho_dados()
        if os.path.exists(caminho_json):
            with open(caminho_json, 'r', encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                    if isinstance(dados, dict):
                        dados = [dados]
                except json.JSONDecodeError:
                    dados = []
        else:
            dados = []
        dados.append(funcionario_dict)
        with open(caminho_json, "w", encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        print("Registro realizado com sucesso.")
    def excluir_funcionario(self, identificador):
        caminho_json = self._caminho_dados()
        if not os.path.exists(caminho_json):
            return 'Arquivo de dados não encontrado.'
        with open(caminho_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return 'Arquivo JSON vazio ou corrompido.'
        if isinstance(dados, dict):
            dados = [dados]
        original_len = len(dados)
        dados = [func for func in dados if func['nome'] != identificador and str(func['cpf']) != str(identificador)]
        if len(dados) == original_len:
            return f'Funcionário com nome ou CPF "{identificador}" não encontrado.'
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados if len(dados) > 1 else dados[0], f, ensure_ascii=False, indent=4)
        return f'Funcionário com identificador "{identificador}" removido com sucesso.'

b=Biblioteca()
print(b)
b.registar_funcionario('s',1234,1243,4314)
b.registar_funcionario('dfdasf',23,312,31)
b.excluir_funcionario("896.054.137-01")