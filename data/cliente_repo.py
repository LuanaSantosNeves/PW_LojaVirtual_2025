from multiprocessing.connection import Client
from data.cliente_model import Client
from data.cliente_sql import *
from data.util import get_conection


def criar_tabela():
    conn = get_conection()
    cursor = conn.cursor()  
    cursor.execute(CRIAR_TABELA)
    conn.commit()
    conn.close()

def inserir_cliente(cliente):
    conn = get_conection()
    cursor = conn.cursor()  
    cursor.execute(INSERIR_CLIENTE, (cliente.nome, cliente.cpf, cliente.email, cliente.teleefone, cliente.senha))
    conn.commit()
    conn.close()

def obter_todos():
    conn = get_conection()
    cursor = conn.cursor()  
    cursor.execute(OBTER_TODOS)
    clientes = cursor.fetchall()
    clientes = [Client(id=row[0], nome=row[1], cpf=row[2], email=row[3], telefone=row[4], senha=row[5]) for row in clientes]
    conn.close()
    return clientes