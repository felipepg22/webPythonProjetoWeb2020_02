from BancoBD import Banco


class Produtos():
    def __init__(self, id_produto=0, descricao="", valor=0, imagem="" ):
        self.id_produto = id_produto
        self.descricao = descricao
        self.valor = valor
        self.imagem = imagem

    def insert(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('INSERT INTO tb_produtos(descricao, valor, imagem) VALUES(%s, %s, %s)', (self.descricao, self.valor, self.imagem))

            banco.conexao.commit()
            c.close()
            return 'Produto adicionado com sucesso!'

        except Exception as e:
            raise Exception('Erro ao cadastrar produto', str(e))

 