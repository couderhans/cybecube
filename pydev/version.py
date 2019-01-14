import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('test.db')
    cur = con.cursor()
    cur.execute('SELECT SQLITE_VERSION()')
    data = cur.fetchone()
    print('sqlite version {}'.format(data))
except lite.Error:
    print('sqlite error {}')
    sys.exit(1)
finally:
    if con:
        con.close()


