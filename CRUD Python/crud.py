import pyodbc

dados_conexao = ("Driver={SQL Server};" 
                 "Server=ITALO;" 
                 "Database=PythonCRUD;")
conexao = pyodbc.connect(dados_conexao)

cursor = conexao.cursor()

#CREATE
# comando = """
#     INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
#     VALUES (2, 'Marisa', 'Bicicleta', '16/05/2022', 2100, 1)
# """
#cursor.execute(comando)
#cursor.commit()  # edita o banco de dados


# READ
# comando = f'SELECT * FROM Vendas'
# cursor.execute(comando)
# resultado = cursor.fetchall() # Ler o banco de dados


# UPDATE
# id_venda = 2
# preco = 2600
# comando = f'UPDATE Vendas SET preco = {preco} WHERE id_venda = {id_venda}'
# cursor.execute(comando)
# cursor.commit()


# DELETE
comando = 'DELETE FROM Vendas WHERE id_venda = 2'
cursor.execute(comando)
cursor.commit()

# ENCERRANDO CONEXÃO
cursor.close()
conexao.close()
