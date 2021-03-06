import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e + "tring to create database")    
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e + "trying to create table")
    
def create_database():       
    database = "database.db"
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        
                                            first_name text NOT NULL,
                                            last_name text NOT NULL
                                            
                                        ); """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_users_table)
    
    else:
        print("Error")



