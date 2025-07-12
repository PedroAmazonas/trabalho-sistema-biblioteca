import livro,pessoa,emprestimo,excecoes
from faker import Faker
import json,os
import datetime

faker=Faker('pt_BR')
class Colecao:
    def __init__(self,nome=None,descricao=None,livros=None):
        self.nome=nome
        self.livros=livros
        self.descricao=descricao
    def inserir_livro(self,livro):
        try:
            self.livros.append(livro)
            return f'Sucesso na inserção do livro {livro} na coleção {self.nome}'
        except:
            raise excecoes.ErroInserir()
    def remover_livro(self,livro):
        try:
            self.livros.append(livro)
            return f'Sucesso na remoçao do livro {livro} na coleção {self.nome}'
        except:
            raise excecoes.ErroRemover()
    def _caminho_colecoes(self):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'json', 'colecoes.json')
    def registrar_colecao(self, nome, descricao, livros=None):
        livros = livros or []
        caminho = self._caminho_colecoes()
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        nova_colecao = {
            "nome": nome,
            "descricao": descricao,
            "livros": livros  # lista de títulos ou ISNBs
        }
        dados = []
        if os.path.exists(caminho):
            with open(caminho, 'r', encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = []
        # Verifica duplicidade por nome
        for c in dados:
            if c["nome"] == nome:
                return f"Coleção '{nome}' já registrada."
        dados.append(nova_colecao)
        with open(caminho, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2)
        return f"Coleção '{nome}' registrada com sucesso."
    def excluir_colecao(self, identificador):
        caminho_json = self._caminho_colecoes()
        if not os.path.exists(caminho_json):
            return 'Arquivo de colecoes não encontrado.'
        with open(caminho_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return 'Arquivo JSON de colecoes  vazio ou corrompido.'
        if isinstance(dados, dict):
            dados = [dados]
        original_len = len(dados)
        dados = [c for c in dados if c["nome"] != identificador]
        if len(dados) == original_len:
            return f'colecao  "{identificador}" não encontrado.'
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2)
        return f'colecoes  "{identificador}" excluído com sucesso.'
    def listar_colecoes(self):
        caminho = self._caminho_colecoes()
        if not os.path.exists(caminho):
            return "Nenhuma coleção registrada."

        with open(caminho, 'r', encoding='utf-8') as f:
            try:
                colecoes = json.load(f)
            except json.JSONDecodeError:
                return "Erro ao ler coleções."
        if not colecoes:
            return "Nenhuma coleção encontrada."
        texto = ""
        for c in colecoes:
            livros = ', '.join(c.get("livros", []))
            texto += f"\n Nome: {c.get('nome')}\n Descrição: {c.get('descricao')}\n Livros: {livros}\n"
        return texto.strip()
    def __str__(self):
        text=f'Nome:{self.nome}|Livros:{self.livros}|Descrição:{self.descricao}'


class Biblioteca():
    def __init__(self, nome=None, endereco=None):
        self.nome = nome or faker.word()
        self.endereco = endereco or faker.address()
    def __str__(self):
        return f'Nome da biblioteca: {self.nome} | endereço: {self.endereco}'

#Registro e armazenamento dos funcionarios
    def _caminho_funcionarios(self):
            return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'json', 'funcionarios.json')
    def registrar_funcionario(self, nome, idade, cpf,salario):
        caminho_json = self._caminho_funcionarios()
        os.makedirs(os.path.dirname(caminho_json), exist_ok=True)
        if self.verificar_funcionario(cpf):
            print("Registro não realizado: funcionario já existe.")
            return
        funcionario = pessoa.Funcionario(nome,idade,cpf,salario)
        funcionario.alterar_nome(nome)
        funcionario.alterar_idade(idade)
        funcionario.alterar_cpf(cpf)
        funcionario.alterar_salario(salario)
        funcionario_dict = {
            "nome": funcionario.nome,
            "idade": funcionario.idade,
            "cpf": funcionario.cpf
        }
        dados = []
        if os.path.exists(caminho_json):
            with open(caminho_json, 'r', encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                    if isinstance(dados, dict):
                        dados = [dados]
                except json.JSONDecodeError:
                    dados = []
        dados.append(funcionario_dict)
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2)
        print("funcionario registrado com sucesso.")
    def verificar_funcionario(self, identificador):
        caminho_json = self._caminho_funcionarios()
        if not os.path.exists(caminho_json):
            return False
        with open(caminho_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return False
        if isinstance(dados, dict):
            dados = [dados]
        for c in dados:
            if c["nome"] == identificador or str(c["cpf"]) == str(identificador):
                return True
        return False
    def excluir_funcionario(self, identificador):
        caminho_json = self._caminho_funcionarios()
        if not os.path.exists(caminho_json):
            return 'Arquivo de funcionarios não encontrado.'
        with open(caminho_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return 'Arquivo JSON de funcionarios vazio ou corrompido.'
        if isinstance(dados, dict):
            dados = [dados]
        original_len = len(dados)
        dados = [c for c in dados if c["nome"] != identificador and str(c["cpf"]) != str(identificador)]
        if len(dados) == original_len:
            return f'funcionario "{identificador}" não encontrado.'
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2)
        return f'funcionario "{identificador}" excluído com sucesso.'
    def listar_funcionarios(self):
        caminho = self._caminho_funcionarios()
        if not os.path.exists(caminho):
            return "Nenhum funcionarios registrado."
        with open(caminho, 'r', encoding='utf-8') as f:
            try:
                funcionarios = json.load(f)
            except json.JSONDecodeError:
                return "Erro ao ler funcionarios."
        if not funcionarios:
            return "Nenhum funcionario encontrada."
        texto = ""
        for f in funcionarios:
            texto += f"\nNome: {f.get('nome')}\n CPF: {f.get('cpf')}\n Salario: {f.get('salario')}\n"
        return texto.strip()

#Registro e armazenamento dos clientes
    def _caminho_clientes(self):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'json', 'clientes.json')
    def registrar_cliente(self, nome, idade, cpf):
        caminho_json = self._caminho_clientes()
        os.makedirs(os.path.dirname(caminho_json), exist_ok=True)
        if self.verificar_cliente(cpf):
            print("Registro não realizado: cliente já existe.")
            return
        cliente = pessoa.Cliente(nome=nome, idade=idade, cpf=cpf)
        cliente.alterar_nome(nome)
        cliente.alterar_idade(idade)
        cliente.alterar_cpf(cpf)
        cliente_dict = {
            "nome": cliente.nome,
            "idade": cliente.idade,
            "cpf": cliente.cpf
        }
        dados = []
        if os.path.exists(caminho_json):
            with open(caminho_json, 'r', encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                    if isinstance(dados, dict):
                        dados = [dados]
                except json.JSONDecodeError:
                    dados = []
        dados.append(cliente_dict)
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2)
        print("Cliente registrado com sucesso.")
    def verificar_cliente(self, identificador):
        caminho_json = self._caminho_clientes()
        if not os.path.exists(caminho_json):
            return False
        with open(caminho_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return False
        if isinstance(dados, dict):
            dados = [dados]
        for c in dados:
            if c["nome"] == identificador or str(c["cpf"]) == str(identificador):
                return True
        return False
    def excluir_cliente(self, identificador):
        caminho_json = self._caminho_clientes()
        if not os.path.exists(caminho_json):
            return 'Arquivo de clientes não encontrado.'
        with open(caminho_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return 'Arquivo JSON de clientes vazio ou corrompido.'
        if isinstance(dados, dict):
            dados = [dados]
        original_len = len(dados)
        dados = [c for c in dados if c["nome"] != identificador and str(c["cpf"]) != str(identificador)]
        if len(dados) == original_len:
            return f'Cliente "{identificador}" não encontrado.'
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2)
        return f'Cliente "{identificador}" excluído com sucesso.'
    def listar_clientes(self):
        caminho = self._caminho_clientes()
        if not os.path.exists(caminho):
            return "Nenhum cliente registrado."
        with open(caminho, 'r', encoding='utf-8') as f:
            try:
                clientes = json.load(f)
            except json.JSONDecodeError:
                return "Erro ao ler clientes."
        if not clientes:
            return "Nenhum funcionario cliente."
        texto = ""
        for c in clientes:   
            texto += f"\n Nome:{c.get('nome')}\n CPF:{c.get('cpf')}\n Idade:{c.get('idade')}\n"
        return texto.strip()
#Registro e armazenamento dos livros
    def _caminho_livros(self):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'json', 'livros.json')
    def registrar_livro(self, titulo, ano_de_publicacao, isnb, disponibilidade=True):
        caminho_json = self._caminho_livros()
        os.makedirs(os.path.dirname(caminho_json), exist_ok=True)
        if self.verificar_livro(isnb):
            print("Registro não realizado: livro já existe.")
            return
        livro_obj = livro.Livro(titulo=titulo, ano_de_publicacao=ano_de_publicacao, isnb=isnb, disponibilidade=disponibilidade)
        livro_obj.alterar_titulo(titulo)
        livro_obj.alterar_ano_de_publicacao(ano_de_publicacao)
        livro_obj.alterar_isnb(isnb)
        livro_obj.alterar_disponibilidade(True)
        livro_dict = {
            "titulo": livro_obj.titulo,
            "ano_de_publicacao": livro_obj.ano_de_publicacao,
            "isnb": livro_obj.isnb,
            "disponibilidade": livro_obj.disponibilidade
        }
        dados = []
        if os.path.exists(caminho_json):
            with open(caminho_json, 'r', encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                    if isinstance(dados, dict):
                        dados = [dados]
                except json.JSONDecodeError:
                    dados = []
        dados.append(livro_dict)
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2)
        print("Livro registrado com sucesso.")
    def verificar_livro(self, isnb):
        caminho_json = self._caminho_livros()
        if not os.path.exists(caminho_json):
            return False
        with open(caminho_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return False
        if isinstance(dados, dict):
            dados = [dados]
        for l in dados:
            if str(l["isnb"]) == str(isnb):
                return True
        return False
    def excluir_livro(self, isnb):
        caminho_json = self._caminho_livros()
        if not os.path.exists(caminho_json):
            return 'Arquivo de livros não encontrado.'
        with open(caminho_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return 'Arquivo JSON de livros vazio ou corrompido.'
        if isinstance(dados, dict):
            dados = [dados]
        original_len = len(dados)
        dados = [l for l in dados if str(l["isnb"]) != str(isnb)]
        if len(dados) == original_len:
            return f'Livro com ISBN "{isnb}" não encontrado.'
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2)
        return f'Livro com ISBN "{isnb}" removido com sucesso.'
    def _caminho_emprestimos(self):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'json', 'emprestimos.json')
    def excluir_cliente(self, identificador):
        caminho_json = self._caminho_clientes()
        if not os.path.exists(caminho_json):
            return 'Arquivo de clientes não encontrado.'
        with open(caminho_json, 'r', encoding='utf-8') as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                return 'Arquivo JSON de clientes vazio ou corrompido.'
        if isinstance(dados, dict):
            dados = [dados]
        original_len = len(dados)
        dados = [c for c in dados if c["nome"] != identificador and str(c["cpf"]) != str(identificador)]
        if len(dados) == original_len:
            return f'Cliente "{identificador}" não encontrado.'
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2)
        return f'Cliente "{identificador}" excluído com sucesso.'
    def listar_livros(self):
        caminho = self._caminho_livros()
        if not os.path.exists(caminho):
            return "Nenhum livro registrado."
        with open(caminho, 'r', encoding='utf-8') as f:
            try:
                livros = json.load(f)
            except json.JSONDecodeError:
                return "Erro ao ler livros."
        if not livros:
            return "Nenhum livro encontrada."
        texto = ""
        for l in livros:   
            texto += f"\n Titulo:{l.get('titulo')}\n Disponibilidade:{l.get('disponibilidade')}\n ISNB:{l.get('isnb')}\n"
        return texto.strip()
#Registro e armazenamento de emprestimos
    def registrar_emprestimo(self, identificador_cliente, identificador_livro):
        # Buscar cliente
        cliente = None
        with open(self._caminho_clientes(), 'r', encoding='utf-8') as f:
            try:
                clientes = json.load(f)
            except json.JSONDecodeError:
                clientes = []
        for c in clientes:
            if c["nome"] == identificador_cliente or str(c["cpf"]) == str(identificador_cliente):
                cliente = c
                break
        if not cliente:
            return f"Cliente '{identificador_cliente}' não encontrado."
        # Buscar livro
        livro = None
        with open(self._caminho_livros(), 'r', encoding='utf-8') as f:
            try:
                livros = json.load(f)
            except json.JSONDecodeError:
                livros = []
        for l in livros:
            if l["titulo"] == identificador_livro or str(l["isnb"]) == str(identificador_livro):
                livro = l
                break
        if not livro:
            return f"Livro '{identificador_livro}' não encontrado."
        if not livro["disponibilidade"]:
            return f"Livro '{livro['titulo']}' está indisponível."
        # Atualizar disponibilidade do livro
        livro["disponibilidade"] = False
        with open(self._caminho_livros(), 'w', encoding='utf-8') as f:
            json.dump(livros, f, indent=2)
        # Registrar empréstimo
        hoje = datetime.date.today()
        devolucao = hoje + datetime.timedelta(days=7)
        registro = {
            'Tipo':'Emprestimo',
            "cliente": cliente["nome"],
            "cpf": cliente["cpf"],
            "livro": livro["titulo"],
            "isnb": livro["isnb"],
            "data_emprestimo": hoje.strftime('%Y-%m-%d'),
            "prazo_devolucao": devolucao.strftime('%Y-%m-%d')
        }
        caminho_json = self._caminho_emprestimos()
        os.makedirs(os.path.dirname(caminho_json), exist_ok=True)
        dados = []
        if os.path.exists(caminho_json):
            with open(caminho_json, 'r', encoding='utf-8') as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = []
        dados.append(registro)
        with open(caminho_json, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2)
        return f"Empréstimo de '{livro['titulo']}' para {cliente['nome']} registrado com sucesso."
    def registrar_devolucao(self, identificador_cliente, identificador_livro):
        # Buscar cliente
        cliente = None
        with open(self._caminho_clientes(), 'r', encoding='utf-8') as f:
            try:
                clientes = json.load(f)
            except json.JSONDecodeError:
                clientes = []
        for c in clientes:
            if c["nome"] == identificador_cliente or str(c["cpf"]) == str(identificador_cliente):
                cliente = c
                break
        if not cliente:
            return f"Cliente '{identificador_cliente}' não encontrado."
        # Buscar livro
        livro = None
        with open(self._caminho_livros(), 'r', encoding='utf-8') as f:
            try:
                livros = json.load(f)
            except json.JSONDecodeError:
                livros = []
        for l in livros:
            if l["titulo"] == identificador_livro or str(l["isnb"]) == str(identificador_livro):
                livro = l
                break
        if not livro:
            return f"Livro '{identificador_livro}' não encontrado."
        if livro["disponibilidade"]:
            return f"Livro '{livro['titulo']}' já está disponível. Nenhuma devolução esperada."
        # Carregar e verificar empréstimos
        caminho_emprestimos = self._caminho_emprestimos()
        if not os.path.exists(caminho_emprestimos):
            return "Nenhum empréstimo registrado."
        with open(caminho_emprestimos, 'r', encoding='utf-8') as f:
            try:
                emprestimos = json.load(f)
            except json.JSONDecodeError:
                return "Arquivo de empréstimos corrompido."
        emprestimo = None
        for e in emprestimos:
            if (e["cliente"] == cliente["nome"] or str(e["cpf"]) == str(cliente["cpf"])) and \
            (e["livro"] == livro["titulo"] or str(e["isnb"]) == str(livro["isnb"])) and e["Tipo"] == "Emprestimo":
                emprestimo = e
                break
        if not emprestimo:
            return "Empréstimo correspondente não encontrado."
        # Calcular multa por atraso
        data_hoje = datetime.date.today()
        prazo = datetime.datetime.strptime(emprestimo["prazo_devolucao"], '%Y-%m-%d').date()
        multa = 0.0
        if data_hoje > prazo:
            dias = (data_hoje - prazo).days
            multa = dias * 0.10
        # Atualizar disponibilidade do livro
        for l in livros:
            if l["titulo"] == livro["titulo"] or l["isnb"] == livro["isnb"]:
                l["disponibilidade"] = True
                break
        with open(self._caminho_livros(), 'w', encoding='utf-8') as f:
            json.dump(livros, f, indent=2)
        # Registrar devolução
        registro = {
            'Tipo': 'Devolucao',
            "cliente": cliente["nome"],
            "cpf": cliente["cpf"],
            "livro": livro["titulo"],
            "isnb": livro["isnb"],
            "data_devolucao": data_hoje.strftime('%Y-%m-%d'),
            "prazo_devolucao": prazo.strftime('%Y-%m-%d'),
            "multa": round(multa, 2)
        }
        emprestimos.append(registro)
        with open(caminho_emprestimos, 'w', encoding='utf-8') as f:
            json.dump(emprestimos, f, indent=2)
        if multa > 0:
            return f"Devolução registrada com multa de R${multa:.2f}"
        return "Devolução registrada sem multa."
    def listar_emprestimos(self):
        caminho = self._caminho_emprestimos()
        if not os.path.exists(caminho):
            return "Nenhum emprestimo registrado."
        with open(caminho, 'r', encoding='utf-8') as f:
            try:
                emprestimos = json.load(f)
            except json.JSONDecodeError:
                return "Erro ao ler emprestimos."
        if not emprestimos:
            return "Nenhum emprestimo encontrado."
        texto = ""
        for e in emprestimos:   
            texto += f"\n Cliente:{e.get('cliente')}\n Livro:{e.get('livro')}\n Tipo:{e.get('Tipo')}\n"
        return texto.strip()