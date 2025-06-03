from platform import python_version
# print(python_version())
import sqlite3
# print(sqlite3.sqlite_version)

import pandas as pd

con = sqlite3.connect("cap12_dsa.db")   # conectar no banco de dados
cursor = con.cursor()                   # entrar no banco com o cursor para percorrer os dados no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""
cursor.execute(sql_query)
# print(cursor.fetchall())

query1 = 'SELECT * FROM tb_vendas_dsa'
cursor.execute(query1)
nomes_colunas = [description[0] for description in cursor.description]
# print(nomes_colunas)
dados = cursor.fetchall()
# print(dados)

query2 = 'SELECT AVG(Unidades_Vendidas) FROM tb_vendas_dsa'
cursor.execute(query2)
# print(cursor.fetchall())

query3 = 'SELECT Nome_Produto, AVG(Unidades_Vendidas) FROM tb_vendas_dsa GROUP BY Nome_Produto'
cursor.execute(query3)
# print(cursor.fetchall())

query4 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto"""
cursor.execute(query4)
print(cursor.fetchall())


































