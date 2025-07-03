from faker import Faker
import datetime
from abc import ABC, abstractmethod
from excecoes import ErroPessoa,ErroSalario,ErroNome
faker=Faker('pt_BR')
class Pessoa(ABC):
    @abstractmethod
    def __str__(self):
        pass
      
class Cliente(Pessoa):
    def __init__(self,nome=None,idade=None,cpf=None,livros_emprestados=[]):
        hoje = datetime.date.today()
        self.__nome=faker.name()
        data_de_nascimento=faker.date_of_birth(minimum_age=4,maximum_age=123)
        self.__idade=hoje.year - data_de_nascimento.year - ((hoje.month, hoje.day) < (data_de_nascimento.month, data_de_nascimento.day))
        self.__cpf=faker.cpf()
        self.__livros_emprestados=livros_emprestados
    @property
    def nome(self):
        '''Getter do nome'''
        return self.__nome
    nome.setter
    def alterar_nome(self,novo_nome):
        '''Setter do nome'''
        try:
            if novo_nome==None:
                raise ErroNome
            else:    
                self.__nome=novo_nome
        except:
            raise ErroNome
        
    @property
    def idade(self):
        '''Getter da idade'''
        return self.__idade
    @property
    def cpf(self):
        '''Getter do cpf'''
        return self.__cpf
    cpf.setter
    def alterar_cpf(self,novo_cpf):
        '''Setter do cpf'''
        self.__nome=novo_cpf
    @property
    def livros_emprestados(self):
        '''Getter dos livros_emprestados'''
        return self.__livros_emprestados
    '''livros_emprestados.setter
        def alterar_livros_emprestados(self,):
        Setter dos livros_emprestados
        self.__livros_emprestados='''
    def __str__(self):
        text=f"Nome:{self.nome}|Idade: {self.idade}|CPF:{self.cpf}|livros_emprestados:{self.livros_emprestados}"
        return text
p=Cliente()
print(p)

class Funcionario(Pessoa):
    def __init__(self,nome=None,idade=None,cpf=None,salario=None):
        hoje = datetime.date.today()
        self.__nome=faker.name()
        data_de_nascimento=faker.date_of_birth(minimum_age=4,maximum_age=123)
        self.__idade=hoje.year - data_de_nascimento.year - ((hoje.month, hoje.day) < (data_de_nascimento.month, data_de_nascimento.day))
        self.__cpf=faker.cpf()
        self.__salario=salario
    @property
    def nome(self):
        '''Getter do nome'''
        return self.__nome
    nome.setter
    def alterar_nome(self,novo_nome):
        '''Setter do nome'''
        self.__nome=novo_nome
    @property
    def idade(self):
        '''Getter da idade'''
        return self.__idade
    @property
    def cpf(self):
        '''Getter do cpf'''
        return self.__cpf
    cpf.setter
    def alterar_nome(self,novo_cpf):
        '''Setter do cpf'''
        self.__nome=novo_cpf
    @property
    def salario(self):
        '''Getter do salario'''
        return self.__salario
    salario.setter
    def alterar_salario(self,novo_salario):
        '''Setter do salario'''
        try:
            novo_salario=int(novo_salario)
        except:
            raise ErroSalario(novo_salario)
        if novo_salario<0:
            raise ErroSalario(novo_salario)
        else:
            self.__salario=novo_salario
    def __str__(self):
        text=f"Nome:{self.nome}|Idade: {self.idade}|CPF:{self.cpf}|Salario:R${self.salario}"
        return text
f=Funcionario(salario=1545)
print(f)