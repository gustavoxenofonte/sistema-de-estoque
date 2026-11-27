from domain import Produto
from repositories import criarBancoDeDados
import sqlite3

class CadastroProduto:
    def __init__(self, produto: Produto):
        self.produto = produto
        self.id, self.nome, self.preco = self.produto.retorna_atributos()

    def cadastrar_produto(self):
        # lembrar de ver o nome do banco
        conexao = sqlite3.connect('src/database/banco.db')
        cursor = sqlite3.Cursor(conexao)
        cursor.execute(f'''INSERT INTO produtos (nome, preco) VALUES (
                        "{self.nome}", "{self.preco}"
                        )''')
        conexao.commit()





