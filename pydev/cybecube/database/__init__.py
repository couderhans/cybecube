import sqlite3 as lite


def open_database():
    return lite.connect('C:\\Users\\couder\\Projects\\pydev\\test.db')


def close_database(con):
    if con:
        con.close()
