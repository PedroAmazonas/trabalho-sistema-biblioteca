from pessoa import *
from livro import *
import datetime

class Emprestimo():
    global historico_de_emprestimos
    historico_de_emprestimos={}
    def __init__(self,livro:Livro,cliente:Cliente,data_emprestimo=None,data_devolucao=None):
        self.livro=livro
        self.cliente=cliente
        self.data_emprestimo=data_emprestimo
        self.data_devolucao=data_devolucao
    def emprestar(self):
        if self.livro.disponibilidade==True:
            self.livro.alterar_disponibilidade(False)
            self.data_emprestimo=datetime.date.today()
            self.data_devolucao=self.data_emprestimo+datetime.timedelta(days=7)
            historico_de_emprestimos[self.cliente]=self.livro
            return f'Livro:{self.livro} emprestado para {self.cliente}|data de emprestimo:{self.data_emprestimo.strftime("%d/%m/%Y")}|data de devolucao {self.data_devolucao.strftime("%d/%m/%Y")}'
        else:
            print("Indisponivel")
e=Emprestimo(l,c)
e.emprestar()   
e.emprestar()
e2=Emprestimo(l2,c2)
e2.emprestar()
print(historico_de_emprestimos)  
