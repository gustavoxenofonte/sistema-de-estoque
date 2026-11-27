import sqlite3

# A princípio o banco de dados vai vir com tabelas pré-definidas

def criar_banco_de_dados(nome):
    conexao = sqlite3.connect(f'src/database/{nome}.db')
    cursor = sqlite3.Cursor(conexao)

    # Tabela produtos

    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco FLOAT NOT NULL
                    )''')

    conexao.commit()
