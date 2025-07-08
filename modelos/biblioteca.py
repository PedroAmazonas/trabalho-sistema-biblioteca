import livro
from faker import Faker
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
    def __init__(self,nome=None,endereco=None):
        self.nome=nome or faker.word()
        self.endereco=endereco or faker.address()
    def __str__(self):
        text=f'Nome da biblioteca:{self.nome}|endereço:{self.endereco}'
        return text
b=Biblioteca()
print(b)