'''
Created on Feb 26, 2017

@author: ubuntu
'''

import sqlite3


conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT * FROM stuffToPlot WHERE value = 3')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT * FROM stuffToPlot WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

    c.execute('SELECT value, datestamp FROM stuffToPlot WHERE unix > 1452554972')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row[0])
    
read_from_db()
c.close
conn.close()