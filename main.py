import mysql.connector

dbconfg = {
    "host" : "localhost",
    "user" : "root",
    "password" : 'Total909090!',
    "database" : "locadora"
}

# pip install sql-connector-python

# cursor = conn.cursor()


def showFilmes():
    conn = mysql.connector.connect(**dbconfg)
    cursor = conn.cursor()
    cursor.execute("select * from filme")

    lista_de_filmes = cursor.fetchall()
    cursor.close()
    conn.close()


    for filme in lista_de_filmes:
        print(filme)

def insertFilme(titulo,genero,ano,preco):
    conn = mysql.connector.connect(**dbconfg)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO filme(titulo, genero, ano, preco)VALUES('{titulo}','{genero}',{ano},{preco})")
    conn.commit()
    cursor.close()
    conn.close()

def deleteFilme(id):
    conn = mysql.connector.connect(**dbconfg)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM filme WHERE id='{id}';")
    conn.commit()
    cursor.close()
    conn.close()


def updateFilme(titulo,genero,ano,preco,id):

    conn = mysql.connector.connect(**dbconfg)
    cursor = conn.cursor()
    cursor.execute(f"""
    UPDATE filme
        set titulo = "{titulo}", genero = "{genero}", ano = '{ano}', preco = '{preco}'
        where id = '{id}';
""")
    conn.commit()
    cursor.close()
    conn.close()

def consulta_banco(query):
    conn = mysql.connector.connect(**dbconfg)
    cursor = conn.cursor()
    cursor.execute(query)
    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return lista

def bulir_no_banco(query):
    conn = mysql.connector.connect(**dbconfg)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    print("editado com sucesso!")
   


# # Consulta
# todos_os_filmes = consulta_banco("SELECT * FROM filme")
# filmes_pos_2005 = consulta_banco("SELECT * FROM filme WHERE ano>2005")

# # Bulir
# titulo = str(input("Digite o titulo do filme: "))
# genero = str(input("Digite o genero do filme: "))
# ano = int(input("Digite o ano do filme: "))
# preco = float(input("Digite o valor do filme: "))

# consulta = f"INSERT INTO filme(titulo, genero, ano, preco)VALUES('{titulo}','{genero}',{ano},{preco})"
# bulir_no_banco(bulir_no_banco)



# showFilmes()
# # insertFilme("As Branquelas","Comedia",2004,30)
# # showFilmes()
# # deleteFilme(12)
# updateFilme("Saltburn","Thriller/comedia",2023,49.69,10)
# print("")


# showFilmes()

while True:
    menu = int(input( f"""
        1-  Vizualizar todos os filmes
        2-  Adicionar um filme
        3-  Editar um filme
        4-  Deletar um film
        0-  Sair
    """
))
    if menu == 0:
        break

    elif menu == 1:
        todos_os_filmes = consulta_banco("SELECT * FROM filme")
        for filme in todos_os_filmes:
            print(filme)
    
    elif menu == 2:
        titulo = str(input("Digite o titulo do filme: "))
        genero = str(input("Digite o genero do filme: "))
        ano = int(input("Digite o ano do filme: "))
        preco = float(input("Digite o valor do filme: "))
        consulta = f"INSERT INTO filme(titulo, genero, ano, preco)VALUES('{titulo}','{genero}',{ano},{preco})"
        bulir_no_banco(consulta)

    elif menu == 3:
        titulo = str(input("Digite o titulo do filme: "))
        genero = str(input("Digite o genero do filme: "))
        ano = int(input("Digite o ano do filme: "))
        preco = float(input("Digite o valor do filme: "))
        id = int(input("Id do filme que será editado: "))
        query = """
                UPDATE filme
                set titulo = "{titulo}", genero = "{genero}", ano = '{ano}', preco = '{preco}'
                where id = '{id}';
"""
        bulir_no_banco(query=query)

    elif menu==4:
        id = int(input("ID do filme que deseja deletar: "))

        query = f"DELETE FROM filme WHERE id='{id}';"
        bulir_no_banco(query)
 
