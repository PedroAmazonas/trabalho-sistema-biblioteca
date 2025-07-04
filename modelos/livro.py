from faker import Faker
import datetime
from excecoes import ErroLivro,ErroTitulo,ErroIsnb,ErroAno_de_publicacao,ErroDisponibilidade
faker=Faker('pt_BR')
class Livro():
    def __init__(self,titulo=None,ano_de_publicacao=None,isnb=None,disponibilidade=None):
        self.__titulo = titulo or faker.word()
        self.__isnb = isnb or faker.isbn13()
        self.__ano_de_publicacao = ano_de_publicacao or faker.year()
        self.__disponibilidade = disponibilidade    
    @property
    def titulo(self):
        '''Getter do titulo'''
        return self.__titulo
    titulo.setter
    def alterar_titulo(self,novo_titulo):
        '''Setter do titulo'''
        try:
            if novo_titulo==None:
                raise ErroTitulo
            else:    
                self.__titulo=novo_titulo
        except:
            raise ErroTitulo
    @property
    def ano_de_publicacao(self):
        '''Getter do ano_de_publicacao'''
        return self.__ano_de_publicacao
    ano_de_publicacao.setter
    def alterar_ano_de_publicacao(self,novo_ano_de_publicacao):
        '''Setter do salario'''
        try:
            novo_ano_de_publicacao=int(novo_ano_de_publicacao)
        except:
            raise ErroAno_de_publicacao(novo_ano_de_publicacao)
        if novo_ano_de_publicacao<1700:
            raise ErroAno_de_publicacao(novo_ano_de_publicacao)
        else:
            self.__ano_de_publicacao=novo_ano_de_publicacao  
    @property
    def isnb(self):
        '''Getter do isnb'''
        return self.__isnb
    isnb.setter
    def alterar_isnb(self,novo_isnb):
        '''Setter do isnb'''
        try:
            if novo_isnb==None:
                raise ErroIsnb
            else:    
                self.__isnb=novo_isnb
        except:
            raise ErroIsnb 
    @property
    def disponibilidade(self):
        '''Getter do disponibilidade'''
        return self.__disponibilidade
    disponibilidade.setter
    def alterar_disponibilidade(self,nova_disponibilidade):
        '''Setter do isnb'''
        try:
            if nova_disponibilidade==None:
                raise ErroDisponibilidade
            else:    
                self.__disponibilidade=nova_disponibilidade
        except:
            raise ErroDisponibilidade

l=Livro(disponibilidade=True)
l2=Livro(disponibilidade=True)