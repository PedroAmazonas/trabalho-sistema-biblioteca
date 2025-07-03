class ErroPessoa(Exception):
    '''Classe para os erros do codigo do pessoa.py'''
    pass
class ErroSalario(ErroPessoa):
    def __init__(self,salario):
        self.salario=salario
        super().__init__(f'O valor:{salario},não é válido.')
class ErroNome(ErroPessoa):
    def __init__(self,nome):
        self.nome=nome
        super().__init__(f'O valor:{nome},não é válido.')

class ErroLivro(Exception):
    '''Classe para os erros do codigo do pessoa.py'''
    pass
class ErroTitulo(ErroLivro):
    def __init__(self,titulo):
        self.titulo=titulo
        super().__init__(f'O título:{titulo},não é válido.')

class ErroIsnb(ErroLivro):
    def __init__(self,isnb):
        self.isnb=isnb
        super().__init__(f'O título:{isnb},não é válido.')
class ErroAno_de_publicacao(ErroLivro):
    def __init__(self,ano_de_publicacao):
        self.ano_de_publicacao=ano_de_publicacao
        super().__init__(f'O ano_de_publicacao:{ano_de_publicacao},não é válido.')
class ErroDisponibilidade(ErroLivro):
    def __init__(self,disponibilidade):
        self.disponibilidade=disponibilidade
        super().__init__(f'A disponibilidade:{disponibilidade},não é válido.')