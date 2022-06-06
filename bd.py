# importando sqlite3
import sqlite3 as sql

# criando e conectando com o banco de dados name, brand, category, provider, price, regist_date

# Criar tabela
def dataBase():
    con = sql.connect('main.db')   
    with con:
        cur = con.cursor()
        query = ( "CREATE TABLE IF NOT EXISTS tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, brand TEXT, category TEXT, provider TEXT, price TEXT, regist_date TEXT)")
        cur.execute(query)

# Populando Banco
""" with con:
    cur = con.cursor()
    cur.execute("INSERT INTO tarefa (name, brand, category, provider, price, regist_date) VALUES('Mouse Gamer', 'Razer', 'Periférico', 'Razer Inc', '200,00', '13/05/22')")
    cur.execute("INSERT INTO tarefa (name, brand, category, provider, price, regist_date) VALUES('Mouse Gamer', 'Razer', 'Periférico', 'Razer Inc', '200,00', '13/05/22')")
    cur.execute("INSERT INTO tarefa (name, brand, category, provider, price, regist_date) VALUES('Mouse Gamer', 'Razer', 'Periférico', 'Razer Inc', '200,00', '13/05/22')")
    cur.execute("INSERT INTO tarefa (name, brand, category, provider, price, regist_date) VALUES('Mouse Gamer', 'Razer', 'Periférico', 'Razer Inc', '200,00', '13/05/22')") """

# Inserir tarefas
def inserir(i):
    con = sql.connect('main.db')
    with con:
        cur = con.cursor()
        query = "INSERT INTO tarefa (name, brand, category, provider, price, regist_date) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# Selecionar tarefas
def selecionar():
    con = sql.connect('main.db')
    lista_tarefas = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM tarefa")
        rows = cur.fetchall()
        for row in rows:
            lista_tarefas.append(row)
    return lista_tarefas

# Deletar tarefas
def deletar(i):
    con = sql.connect('main.db')
    with con:
        cur = con.cursor()
        query = "DELETE FROM tarefa WHERE id=?"
        cur.execute(query, i)

# Atualizar tarefas
def atualizar(i):
    con = sql.connect('main.db')
    with con:
        cur = con.cursor()
        query = "UPDATE tarefa SET name=?, brand=?, category=?, provider=?, price=?, regist_date=? WHERE id=?"
        cur.execute(query, i)