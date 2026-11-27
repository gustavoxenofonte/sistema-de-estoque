class Produto:
    def __init__(self, id: int, nome: str, preco: float):
        self.id = id
        self.nome = nome
        self.preco = preco

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, novo_id):
        if isinstance(novo_id, int) and novo_id >= 0:
            self.__id = novo_id
        elif not isinstance (novo_id, int):
            raise TypeError
        elif novo_id < 0:
            raise ValueError
        else:
            raise Exception

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self.__nome = novo_nome
        else:
            raise TypeError

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        if isinstance(novo_preco, float) and novo_preco > 0:
            self.__preco = novo_preco
        elif isinstance(novo_preco, int) and novo_preco > 0:
            novo_preco = float(novo_preco)
            self.__preco = novo_preco
        elif isinstance(novo_preco, int) or isinstance(novo_preco, float) and novo_preco < 0:
            raise ValueError
        else:
            raise TypeError

    

produto = Produto(id = 0, nome="Arroz", preco=20)
produto.preco = 99299292929292929.123
print(produto.preco)
    