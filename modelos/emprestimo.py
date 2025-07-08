from pessoa import *
from livro import *
import datetime

class Emprestimo:
    global historico_de_emprestimos
    historico_de_emprestimos = {}

    def __init__(self, livro: Livro, cliente: Cliente, data_emprestimo=None, prazo_devolucao=None):
        self.livro = livro
        self.cliente = cliente
        self.data_emprestimo = data_emprestimo
        self.prazo_devolucao = prazo_devolucao

    def emprestar(self):
        if self.livro.disponibilidade:
            self.livro.alterar_disponibilidade(False)
            self.data_emprestimo = datetime.date.today()
            self.prazo_devolucao = self.data_emprestimo + datetime.timedelta(days=7)
            historico_de_emprestimos[self.cliente] = (self.livro,self.data_emprestimo,self.prazo_devolucao)
            return (
                f"Livro: {self.livro.titulo} emprestado para {self.cliente.nome} | "
                f"Data de empréstimo: {self.data_emprestimo.strftime('%d/%m/%Y')} | "
                f"Data de devolução: {self.prazo_devolucao.strftime('%d/%m/%Y')}"
            )
        else:
            raise ErroDisponibilidade

    def devolver(self):
        self.data_devolucao = datetime.date.today()
        if self.data_devolucao > self.prazo_devolucao:
            dias_atraso = (self.data_devolucao - self.prazo_devolucao).days
            multa = dias_atraso * 0.10  # R$0,10 por dia
            print(f"Você atrasou a devolução. Multa: R${multa:.2f}")
            self.livro.alterar_disponibilidade(True)
        else:
            print("Livro devolvido no prazo.")
        self.livro.alterar_disponibilidade(True)
e=Emprestimo(l,c)
print(e.emprestar())

e2=Emprestimo(l2,c2)
e2.emprestar()
e2.devolver()
print(historico_de_emprestimos)  
