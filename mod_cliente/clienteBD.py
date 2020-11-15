import json

from BancoBD import Banco
from funcoes import Funcoes, LOG


class Clientes(object):
    def __init__(self, id_cliente=0, nome="", endereco="", numero=0, observacao="", cep="", bairro="", cidade="", estado="SC", telefone="", email="", login="", senha="", grupo="SOLIC"):
        self.id_cliente = id_cliente
        self.nome = nome
        self.endereco = endereco
        self.numero = numero
        self.observacao = observacao
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone
        self.email = email
        self.login = login
        self.senha = senha
        self.grupo = grupo

    def selectAll(self):
        try:
            banco = Banco()
            c = banco.conexao.cursor()

            c.execute("select id_cliente,nome,endereco,numero,observacao,cep,bairro,cidade,estado,telefone,email,login,senha,grupo from tb_clientes")

            result = c.fetchall()

            c.close()

            return result
        except Exception as e:
            return "Ocorreu um erro ao buscar os clientes"

    def selectOne(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute("select id_cliente,nome,endereco,numero,observacao,cep,bairro,cidade,estado,telefone,email,login,senha,grupo from tb_clientes where id_cliente = %s", (self.id_cliente)) 

            for linha in c:
                self.id_cliente = linha[0]
                self.nome = linha[1]
                self.endereco = linha[2]
                self.numero = linha[3]
                self.observacao = linha[4]
                self.cep = linha[5]
                self.bairro = linha[6]
                self.cidade = linha[7]
                self.estado = linha[8]
                self.telefone = linha[9]
                self.email = linha[10]
                self.login = linha[11]
                self.senha = linha[12]
                self.grupo = linha[13]

            c.close()
        
            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro ao buscar o Cliente!"

        
    def insert(self):
        try:
            banco = Banco()
        except:
            return "Erro conexão banco"
        try:

            c = banco.conexao.cursor()
            c.execute("insert into tb_clientes(nome,endereco,numero,observacao,cep,bairro,cidade,estado,telefone,email,login,senha,grupo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.nome, self.endereco, self.numero, self.observacao, self.cep, self.bairro, self.cidade, self.estado, self.telefone, self.email, self.login, self.senha, self.grupo))
            banco.conexao.commit()
            
            c.close()
            Funcoes.criaLOG('INSERT Cliente', LOG.info)
            return "Cliente cadastrado com sucesso!"

        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
            raise Exception('Erro ao tentar cadastrar cliente!', str(e))
        
    def update(self):
        
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute("update tb_clientes set nome=%s , endereco=%s , numero=%s, observacao=%s, cep=%s, bairro=%s, cidade=%s, estado=%s, telefone=%s, email=%s, login=%s, grupo=%s where id_cliente = %s",(self.nome, self.endereco, self.numero, self.observacao, self.cep, self.bairro, self.cidade, self.estado, self.telefone, self.email, self.login, self.grupo, self.id_cliente))

            banco.conexao.commit()

            c.close()
            
            Funcoes.criaLOG('UPDATE Cliente', LOG.info)

            return "Cliente editado com sucesso!"
        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)           
            raise Exception("Erro ao editar cliente!", str(e))
    
    def delete(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute("delete from tb_clientes where id_cliente = %s", (self.id_cliente))

            banco.conexao.commit()

            c.close()

            Funcoes.criaLOG('DELETE Cliente', LOG.info)
            return "Cliente excluído com sucesso!"
        except Exception as e:
            Funcoes.criaLOG(str(e), LOG.error)
            raise Exception("Erro ao tentar excluir", str(e))

    def selectLogin(self):
        try:
            banco = Banco()
            c= banco.conexao.cursor()

            c.execute("select id_cliente,nome,login,grupo from tb_clientes where login= %s and senha = %s", (self.login, self.senha))

            for linha in c:
                self.id_cliente = linha[0]
                self.nome = linha[1]
                self.login = linha[2]
                self.grupo = linha[3]

            c.close()

            return 'Busca feita com sucesso!'

        except Exception as e:
            raise Exception('Erro na busca!', str(e))
             
    def verificaSeLoginExiste(self):
        try:
            banco = Banco()

            c = banco.conexao.cursor()

            c.execute('SELECT id_cliente FROM tb_clientes WHERE login = %s',(self.login))
            result = c.fetchall()
            c.close()

            return result
        except Exception as e:
            raise Exception(str(e))
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)