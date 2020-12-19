import os
import sqlite3
from sqlite3 import Error


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
    for filename in files:
        abs_path = path + '/' + filename
        file = open(abs_path, 'r')
        print(file.read())
        file.close()


def create_haiku(conn):
    sql = "INSERT INTO HAIKU(name, authors, content) VALUES  (\"test\",\"test\",\"test\");"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()


def main():
    # database = r"C:/sqlite/db/haikuDB.db"
    path = 'C:/Users/natha/Documents/Personal Projects/quotes/Haikus'
    # create database connection
    # conn = sqlite3.connect(database)
    read_files(path)
    # create_haiku(conn)


main()
