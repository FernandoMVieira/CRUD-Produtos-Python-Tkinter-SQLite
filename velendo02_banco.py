
import sqlite3 as sql


def dataBase():
    con = sql.connect('main.db')
    with con:
        cur = con.cursor()
        query = (
            "CREATE TABLE IF NOT EXISTS tarefa(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, brand TEXT, "
            "category TEXT, provider TEXT, price TEXT, regist_date TEXT)")
        cur.execute(query)



def inserir(i):
    con = sql.connect('main.db')
    with con:
        cur = con.cursor()
        query = "INSERT INTO tarefa (name, brand, category, provider, price, regist_date) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)


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


def deletar(i):
    item = i
    con = sql.connect('main.db')
    cur = con.cursor()
    cur.execute(f'DELETE FROM tarefa WHERE id = {item}')
    con.commit()
    cur.close()


def atualizar(i):
    con = sql.connect('main.db')
    with con:
        cur = con.cursor()
        query = "UPDATE tarefa SET name=?, brand=?, category=?, provider=?, price=?, regist_date=? WHERE id=?"
        cur.execute(query, i)


