import sqlite3


def base_entries(name):
    con = sqlite3.connect('specchoise.db')
    cur = con.cursor()
    content = cur.execute('SELECT * FROM {}'.format(name))
    entries = content.fetchall()
    con.close()
    return entries


def prof_entries(name):
    con = sqlite3.connect('specchoise.db')
    cur = con.cursor()
    content = cur.execute("SELECT * FROM  professions_list WHERE link='{}';".format(name))
    entries = content.fetchall()
    con.close()
    return entries


def test_entries():
    con = sqlite3.connect('specchoise.db')
    cur = con.cursor()
    content = cur.execute("SELECT question FROM test;")
    entries = content.fetchall()
    con.close()
    return entries



def test_zno():
    con = sqlite3.connect('specchoise.db')
    cur = con.cursor()
    content = cur.execute('SELECT * FROM zno_test')
    entries = content.fetchall()
    d = dict()
    for spec in entries:
        temp_set = {spec[2],spec[3],spec[4],spec[5]}
        temp_set.difference_update("-")
        d.update({spec[1]: list(temp_set)})
    con.close()
    return d

