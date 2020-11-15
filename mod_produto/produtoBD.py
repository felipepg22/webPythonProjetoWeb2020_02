import json

from BancoBD import Banco
from funcoes import Funcoes, LOG

class Produtos():
    def __init__(self, id_produto=0, descricao="", valor=0, imagem="" ):
        self.id_produto = id_produto
        self.descricao = descricao
        self.valor = valor
        self.imagem = imagem

    def selectAll(self):
        banco = None
        c = None
        try:
            banco = Banco()

            c= banco.conexao.cursor()

            c.execute('SELECT id_produto, descricao, valor, CONVERT(imagem USING utf8) FROM tb_produtos')

            result = c.fetchall()

            c.close()

            return result

        except Exception as e:
            raise Exception('Erro ao buscar produtos', str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def selectONE(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "select id_produto, descricao, CONVERT(valor, CHAR), CONVERT(imagem USING utf8) from tb_produtos where id_produto = %s"
            _sql_data = (self.id_produto,)
            c.execute(_sql,_sql_data)
            for linha in c:
                self.id_produto = linha[0]
                self.descricao = linha[1]
                self.valor = linha[2]
                self.imagem = linha[3]
                return "Busca feita com sucesso!"
        except Exception as e:
            raise Exception("Ocorreu um erro na busca do produto", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()


    def insert(self):
        banco = None
        c = None
        try:
            banco = Banco()            
            c = banco.conexao.cursor()
            _sql = "insert into tb_produtos(descricao, valor, imagem) values (%s,%s,%s)"
            _sql_data = (self.descricao, self.valor, self.imagem,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()

            Funcoes.criaLOG(f'INSERT Produto {c.lastrowid}', LOG.info)
            return "Produto cadastrado com sucesso!"

            
        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
            raise Exception('Erro ao tentar cadastrar produto!', str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def update(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "update tb_produtos set descricao=%s,valor=%s,imagem=%s where id_produto = %s"
            _sql_data = (self.descricao, self.valor, self.imagem, self.id_produto,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()
            Funcoes.criaLOG(f'UPDATE PRODUTO {self.id_produto}', 'info')
            return "Produto atualizado com sucesso!"
        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
            raise Exception("Erro ao editar produto!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def delete(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = "delete from tb_produtos where id_produto = %s"
            _sql_data = (self.id_produto,)
            c.execute(_sql,_sql_data)
            banco.conexao.commit()

            Funcoes.criaLOG(f'DELETE Produto {self.id_produto}', LOG.info)
            return "Produto excluído com sucesso!"
        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
            raise Exception("Erro ao tentar excluir produto!", str(e))
        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)