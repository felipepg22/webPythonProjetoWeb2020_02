from abc import abstractmethod, ABC, ABCMeta
from enum import Enum
import hashlib, logging, datetime
from flask import session



class Funcoes(metaclass=ABCMeta):#Cria classe abstrata



    #método abstrato
    @abstractmethod
    def criptografaSenha(senha):
        return hashlib.sha3_256(senha.encode('utf-8')).hexdigest()

    @abstractmethod
    def criaLOG(mensagem, tipo):
        logging.basicConfig(filename='abcBolinhas.log', format='%(levelname)s| %(name)s | %(asctime)s | %(message)s ', datefmt='%d/%m/%Y %I:%M:%S %p', level=logging.INFO)
        
        try:
            if tipo == 'info':            
                logging.info(f'{mensagem} Usuario: {session["usuario"]}')
            elif tipo == 'warning':
                logging.warning(f'{mensagem} Usuario: {session["usuario"]}')
            elif tipo =='erro':
                logging.error(f'{mensagem} Usuario: {session["usuario"]}')
        except Exception as e:
            print(str(e))