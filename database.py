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


def create_haiku(conn):
    sql = "INSERT INTO HAIKU(name, authors, content) VALUES  (\"test\",\"test\",\"test\");"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()


def main():
    database = r"C:/sqlite/db/haikuDB.db"

    # create database connection
    conn = sqlite3.connect(database)

    create_haiku(conn)


main()
