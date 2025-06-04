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
# print(cursor.fetchall())

# query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
#             FROM tb_vendas_dsa
#             WHERE Valor_Unitario > 199 & AVG(Unidades_Vendidas) > 10
#             GROUP BY Nome_Produto"""
# cursor.execute(query5)          # erro: misuse of aggregate AVG()

query5 = """SELECT Nome_Produto, AVG(Unidades_Vendidas)
            FROM tb_vendas_dsa
            WHERE Valor_Unitario > 199
            GROUP BY Nome_Produto
            HAVING AVG(Unidades_Vendidas) > 10"""
cursor.execute(query5)
# print(cursor.fetchall())

cursor.close()      #boa prática = somente usar o cursor quando está trabalhando no db e fechar em seguida
con.close()


# Usando pandas com SQL

con = sqlite3.connect("cap12_dsa.db")
cursor = con.cursor()

query = "SELECT * FROM tb_vendas_dsa"
cursor.execute(query)
dados = cursor.fetchall()
# print(dados)
# print(type(dados))

df = pd.DataFrame(dados, columns = ["ID_Pedido", "ID_Cliente", "Nome_Produto", "Valor_Unitario", "Unidades_Vendidas", "Custo"])
print(df.head())

cursor.close()
con.close()

media_unidades_vendidas = df["Unidades_Vendidas"].mean()
# print(type(media_unidades_vendidas))
# print(media_unidades_vendidas)









