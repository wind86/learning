'''
Created on Feb 26, 2017

@author: ubuntu
'''

import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1452549218,'2016-01-10 13:53:39','Python',5)")

    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()