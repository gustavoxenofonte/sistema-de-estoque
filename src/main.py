from domain import *
from repositories import *

p1 = Produto("Feijão", 11.50)
criar_banco_de_dados("banco")
cadastro = CadastroProduto(p1)
cadastro.cadastrar_produto()
