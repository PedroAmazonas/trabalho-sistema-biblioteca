from faker import Faker
import datetime
from abc import ABC, abstractmethod
from excecoes import ErroPessoa,ErroSalario,ErroNome,ErroIdade,ErroCPF
faker=Faker('pt_BR')
#Classe das pessoas
class Pessoa(ABC):
    @abstractmethod
    def __str__(self):
        pass
      
class Cliente(Pessoa):
    def __init__(self,nome=None,idade=None,cpf=None):
        hoje = datetime.date.today()
        self.__nome=faker.name()
        data_de_nascimento=faker.date_of_birth(minimum_age=4,maximum_age=123)
        self.__idade=hoje.year - data_de_nascimento.year - ((hoje.month, hoje.day) < (data_de_nascimento.month, data_de_nascimento.day))
        self.__cpf=faker.cpf()
    @property
    def nome(self):
        '''Getter do nome'''
        return self.__nome
    nome.setter
    def alterar_nome(self,novo_nome):
        '''Setter do nome'''
        try:
            self.__nome=novo_nome
        except:
            raise ErroNome(novo_nome)
    @property
    def idade(self):
        '''Getter da idade'''
        return self.__idade
    idade.setter
    def alterar_idade(self,nova_idade):
        '''Setter da idade'''
        try:
            nova_idade=int(nova_idade)
        except:
            raise ErroIdade(nova_idade)
        if nova_idade<0:
            raise ErroIdade(nova_idade)
        else:
            self.__idade=nova_idade
    @property
    def cpf(self):
        '''Getter do cpf'''
        return self.__cpf
    cpf.setter
    def alterar_cpf(self,novo_cpf):
        '''Setter do cpf'''
        try:    
            self.__cpf=novo_cpf
        except:
            raise ErroCPF(novo_cpf)

    def __str__(self):
        text=f"Nome:{self.nome}|Idade: {self.idade}|CPF:{self.cpf}"
        return text

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
        try:
            self.__nome=novo_nome
        except:
            raise ErroNome(novo_nome)
    @property
    def idade(self):
        '''Getter da idade'''
        return self.__idade
    idade.setter
    def alterar_idade(self,nova_idade):
        '''Setter da idade'''
        try:
            nova_idade=int(nova_idade)
        except:
            raise ErroIdade(nova_idade)
        if nova_idade<0:
            raise ErroIdade(nova_idade)
        else:
            self.__idade=nova_idade
    @property
    def cpf(self):
        '''Getter do cpf'''
        return self.__cpf
    cpf.setter
    def alterar_cpf(self,novo_cpf):
        '''Setter do cpf'''
        try:    
            self.__cpf=novo_cpf
        except:
            raise ErroCPF(novo_cpf)
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
