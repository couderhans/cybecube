import sqlite3 as lite

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


def open_database():
    return lite.connect('C:\\Users\\couder\\Projects\\pydev\\test.db')


def close_database(con):
    if con:
        con.close()


def create_table_repositories():
    try:
        con = open_database()
        with con:
            cur = con.cursor()
            cur.execute(
                "CREATE TABLE repositories(repo_id integer primary key autoincrement, "
                "user text, "
                "name text, "
                "clone_url text)")
            data = cur.fetchone()
        print('sqlite version {}'.format(data))
    except lite.Error as e:
        print('sqlite error {}'.format(e.args[0]))
    finally:
        close_database(con)


def insert_into_repositories(repo):
    try:
        con = open_database()
        with con:
            cur = con.cursor()
            cur.execute('INSERT INTO repositories(user,name,clone_url) VALUES (?,?,?)', repo)
            data = cur.fetchone()
        print('sqlite version {}'.format(data))
    except lite.Error as e:
        print('sqlite error {}'.format(e.args[0]))
    finally:
        close_database(con)


def delete_table(name):
    try:
        con = open_database()
        with con:
            cur = con.cursor()
            cur.execute('DROP TABLE {}'.format(name))
        print('table {} deleted'.format(name))
    except lite.Error as e:
        print('sqlite error {}'.format(e.args[0]))
    finally:
        close_database(con)
