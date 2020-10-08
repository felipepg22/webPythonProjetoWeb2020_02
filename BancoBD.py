import pymysql

class Banco():    
    def __init__(self):
        host = "127.0.0.1"
        user = "Felipe"
        password = "fepaga221292"
        db = "db_abc_bolinhas"
        self.conexao = pymysql.connect(host, user, password, db)