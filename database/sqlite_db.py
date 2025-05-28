import sqlite3
from typing import Tuple


def init_db():
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS passwords(
        id INTEGER PRIMARY KEY,
        title TEXT,
        password TEXT
    )
    '''
    try:
        with sqlite3.connect('sqlite.db') as conn:
            cursor = conn.cursor()
            cursor.execute(create_table_sql)
    except Exception as ex:
        print(f'Dogodila se greska init_db {ex}')


def insert_pwd(password: Tuple[int, str, str]):
    insert_pwd_sql = '''
    INSERT INTO passwords (title, password)
    VALUES(?, ?)
    '''
    password = ()

    try:
        with sqlite3.connect('sqlite.db') as conn:
            cursor = conn.cursor()
            cursor.execute(insert_pwd_sql, password)
            conn.commit()
    except Exception as ex:
        print(f'Dogodila se greska insert_pwd {ex}')


def get_all_pwd():
    get_all_pwd_sql = '''
    SELECT * FROM passwords
    '''
    passwords = []

    try:
        with sqlite3.connect('sqlite.db') as conn:
            cursor = conn.cursor()
            cursor.execute(get_all_pwd_sql)
            passwords = cursor.fetchall()
    except Exception as ex:
        print(f'Dogodila se greska get_all_pwd {ex}')

    return passwords


def get_pwd(id: int):
    get_pwd_sql = '''
    SELECT * FROM passwords WHERE id = ?
    '''
    password = ()

    try:
        with sqlite3.connect('sqlite.db') as conn:
            cursor = conn.cursor()
            cursor.execute(get_pwd_sql, (id, ))
            password = cursor.fetchone()
    except Exception as ex:
        print(f'Dogodila se greska get_pwd {ex}')

    return password