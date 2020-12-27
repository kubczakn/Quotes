import os
import sqlite3
import classifier
import quotes

from sqlite3 import Error


# Haiku object
class Haiku:
    def __init__(self, kind, content):
        self.kind = kind
        self.content = content


# Search to determine Haiku type
def search(content, data):
    return classifier.get_result(classifier.analyse_text(content, data))


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
    training_data = classifier.get_training_data()
    for filename in files:
        abs_path = path + '/' + filename
        name = filename.replace('.txt', '')
        file = open(abs_path, 'r')
        content = ''
        for line in file.readlines()[2:5]:
            content += line
            content += '\n'
        file.close()
        file = open(abs_path, 'r')
        kind = search(content, training_data)
        texts[name] = Haiku(kind, file.read())
        file.close()

    return texts


def create_haikus(conn, files):
    cur = conn.cursor()
    cur.execute("DELETE FROM haikuApp_haiku")
    i = 1
    for filename in files:
        cur.execute("INSERT INTO haikuApp_haiku VALUES (?, ?, ?, ?)",
                    (i, filename, files[filename].content, files[filename].kind))
        conn.commit()
        i += 1
    cur.close()


def classify_haiku(haiku):
    start = haiku.find("Haiku:") + len("Haiku:")
    end = haiku.find("Authors:")
    content = haiku[start:end]
    training_data = classifier.get_training_data()
    return search(content, training_data)


def create_haiku(conn, name, haiku):
    cur = conn.cursor()
    cur.execute("INSERT INTO haikuApp_haiku VALUES (NULL,  ?, ?, ?)",
                (name, haiku, classify_haiku(haiku)))
    conn.commit()
    cur.close()


def main():
    database = os.path.abspath("app/db.sqlite3")

    # create database connection
    conn = sqlite3.connect(database)
    name, content = quotes.find_quotes()
    create_haiku(conn, name, content)


main()
