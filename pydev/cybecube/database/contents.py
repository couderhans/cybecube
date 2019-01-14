import sqlite3 as lite


def open_database():
    return lite.connect('C:\\Users\\couder\\Projects\\pydev\\test.db')


def close_database(con):
    if con:
        con.close()

def create_table_contents():
    try:
        con = open_database()
        with con:
            cur = con.cursor()
            cur.execute('CREATE TABLE contents(content_id integer primary key autoincrement,'
                        ' repo_id integer not null, '
                        '   foreign key repo_id references '
                        ' name text, '
                        ' clone_url text)')
            data = cur.fetchone()
        print('sqlite version {}'.format(data))
    except lite.Error as e:
        print('sqlite error {}'.format(e.args[0]))
    finally:
        close_database(con)
