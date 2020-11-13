from BancoBD import Banco
import pymysql

from funcoes import Funcoes, LOG

class Pedidos():
    def __init__(self, id_pedido=0, data_hora="", id_cliente=0, observacao=""):
        self.id_pedido = id_pedido
        self.data_hora = data_hora
        self.id_cliente = id_cliente
        self.observacao = observacao

    def selectAll(self):
        banco = None
        c = None
        try:
            banco = Banco()

            c = banco.conexao.cursor(pymysql.cursors.DictCursor)#Traz como resultado um array associativo

            c.execute('SELECT tbp.id_pedido as ID, tbc.nome as Nome,tbc.telefone as Telefone,tbc.endereco as Endereco,tbc.numero as Numero,tbc.cep as CEP,tbc.bairro as Bairro,tbc.cidade as Cidade,tbp.observacao as Observacao,tbp.data_hora as Data_hora FROM tb_clientes tbc INNER JOIN tb_pedidos tbp ON tbc.id_cliente = tbp.id_cliente')

            result = c.fetchall()

            return result

        except Exception as e:
            raise Exception('Erro ao buscar pedidos', str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()
    def selectOne(self):
        banco = None
        c = None
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = 'SELECT id_pedido, data_hora, id_cliente, observacao FROM tb_pedidos WHERE id_pedido = %s'
            _sql_data = (self.id_pedido)

            c.execute(_sql, _sql_data)

            for linha in c:
                self.id_pedido = linha[0]
                self.data_hora = linha[1]
                self.id_cliente = linha[2]
                self.observacao = linha[3]

            return 'Pedido buscado com sucesso!'

            return result

        except Exception as e:
            raise Exception('Erro ao buscar pedido!', str(e))

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
            _sql = 'INSERT INTO tb_pedidos (data_hora, id_cliente, observacao) VALUES(%s, %s, %s)'
            _sql_data = (self.data_hora, self.id_cliente, self.observacao)
            c.execute(_sql, _sql_data)

            banco.conexao.commit()
            Funcoes.criaLOG(f'INSERT pedido {c.lastrowid}', LOG.info)

            return 'Pedido cadastrado com sucesso!'

        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
            raise Exception('Erro ao cadastrar pedido', str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()
            
        

class PedidosProdutos():
    def __init__(self, id_pedido=0, id_produto=0, quantidade=0, valor=0, observacao=""):
        self.id_pedido=id_pedido
        self.id_produto=id_produto
        self.quantidade=quantidade
        self.valor=valor
        self.observacao = observacao

    def selectProdutosByPedido(self):
        banco = None
        c = None
        try:
            banco = Banco()

            c = banco.conexao.cursor(pymysql.cursors.DictCursor)
            _sql = 'SELECT tp.descricao as Descricao,tpp.id_pedido as ID_PEDIDO, tpp.quantidade as Quantidade, CONVERT(tpp.valor, CHAR) as Valor, tpp.observacao as Observacao, tpp.id_produto as ID_PRODUTO FROM tb_produtos tp INNER JOIN tb_pedido_produtos tpp ON tp.id_produto = tpp.id_produto WHERE tpp.id_pedido = %s'
            _sql_data = (self.id_pedido)
            c.execute(_sql, _sql_data)

            result = c.fetchall()

            return result
        
        except Exception as e:
            raise Exception('Erro ao buscar produtos do pedido', str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def insertProdutosPedido(self):
        banco = None
        c = None
        try:
            banco = Banco()

            c = banco.conexao.cursor()
            _sql = 'INSERT INTO tb_pedido_produtos (id_pedido, id_produto, quantidade, valor, observacao) VALUES(%s, %s, %s, %s, %s)'
            _sql_data = (self.id_pedido, self.id_produto, self.quantidade, self.valor, self.observacao)
            c.execute(_sql, _sql_data)

            banco.conexao.commit()
            Funcoes.criaLOG(f'INSERT produto {self.id_produto} pedido {self.id_produto}', LOG.info)

            return 'Produto cadastrado na comanda'

        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
            raise Exception('Erro ao cadastrar produto na comanda', str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def updateQuantidadeProduto(self):
        banco = None
        c = None
        try:
            banco = Banco()
            c = banco.conexao.cursor()
            _sql = 'UPDATE tb_pedido_produtos SET quantidade = %s WHERE id_pedido = %s AND id_produto = %s'
            _sql_data = (self.quantidade, self.id_pedido, self.id_produto)
            c.execute(_sql, _sql_data)
            banco.conexao.commit()
            
            Funcoes.criaLOG(f'UPDATE quantidade produto {self.id_produto} pedido {self.id_pedido}', LOG.info)

            return 'Produto atualizado com sucesso!'
        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
            raise Exception('Erro ao atualizar produto', str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()

    def deleteProdutoPedido(self):
        banco = None
        c = None
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            _sql = 'DELETE FROM tb_pedido_produtos WHERE id_pedido = %s AND id_produto = %s'
            _sql_data = (self.id_pedido, self.id_produto)

            c.execute(_sql, _sql_data)

            banco.conexao.commit()

            Funcoes.criaLOG(f'DELETE produto {self.id_produto} pedido {self.id_pedido}', LOG.info)

            return 'Produto deletado do pedido'
        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
            raise Exception('Erro ao deletar produto do pedido', str(e))

        finally:
            if c:
                c.close()
            if banco:
                banco.conexao.close()