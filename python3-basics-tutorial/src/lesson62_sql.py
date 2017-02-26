'''
Created on Feb 26, 2017

@author: ubuntu
'''

import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]
    print(50*'#')
    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 2')
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]
    print(50*'#')
    c.execute('DELETE FROM stuffToPlot WHERE value = 99')
    conn.commit()
    print(50*'#')
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]
    
    
del_and_update()
c.close
conn.close()