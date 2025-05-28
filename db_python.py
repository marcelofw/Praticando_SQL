from platform import python_version
# print(python_version())
import sqlite3
# print(sqlite3.sqlite_version)

import pandas as pd

con = sqlite3.connect("cap12_dsa.db")   # conectar no banco de dados
cursor = con.cursor()                   # entrar no banco com o cursor para percorrer os dados no banco de dados
sql_query = """SELECT name FROM sqlite_master WHERE type = 'table';"""
cursor.execute(sql_query)
print(cursor.fetchall())



























