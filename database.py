import os
import sqlite3
import wikipedia
import random
from sqlite3 import Error


# Haiku object
class Haiku:
    def __init__(self, kind, content):
        self.kind = kind
        self.content = content


# Search to determine Haiku type
def search(name):
    article = wikipedia.search(name)[0]

    try:
        summary = wikipedia.summary(article)
    except wikipedia.DisambiguationError as e:
        summary = wikipedia.summary(e.options[0])
    except wikipedia.PageError:
        return 'Film'

    if summary.find('film') != -1:
        return 'Film'
    if summary.find('novel') != -1:
        return 'Book'
    else:
        return 'Person'


def create_connection(db_file):
    # Create database connection

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def read_files(path):
    files = os.listdir(path)
    texts = {}
    for filename in files:
        abs_path = path + '/' + filename
        name = filename.replace('.txt', '')
        file = open(abs_path, 'r')
        kind = search(name)
        texts[name] = Haiku(kind, file.read())
        file.close()

    return texts


def create_haiku(conn, files):
    cur = conn.cursor()
    for filename in files:
        cur.execute("INSERT INTO HAIKU VALUES (?, ?, ?)", (filename, files[filename].content, files[filename].kind))
        conn.commit()

    cur.close()


def main():
    database = r"C:/sqlite/db/haikuDB.db"
    path = 'C:/Users/natha/Documents/Personal Projects/quotes/Haikus'

    # create database connection
    conn = sqlite3.connect(database)
    create_haiku(conn, read_files(path))


main()
