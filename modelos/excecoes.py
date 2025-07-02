class ErroPessoa(Exception):
    '''Classe para os erros da codigo do pessoa.py'''
    pass
class ErroSalario(ErroPessoa):
    def __init__(self,salario):
        self.salario=salario
        super().__init__(f'O valor:{salario},não é válido.')
class ErroNome(ErroPessoa):
    def __init__(self,nome):
        self.nome=nome
        super().__init__(f'O valor:{nome},não é válido.')