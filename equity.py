#!/usr/bin/env python

import csv
import sqlite3
import os
conn= sqlite3.connect('company.db')
c=conn.cursor()

c.execute('''DROP TABLE IF EXISTS equity''')

c.execute('''CREATE TABLE equity (
    symbol TEXT,
    name TEXT,
    date TEXT,
    face INTEGER)
''')

insertSQL='''INSERT INTO equity VALUES (?,?,?,?)'''
if(os.path.isfile('EQUITY_L.csv')):
    print "file exists"

reader=csv.reader(open('EQUITY_L.csv','rb'))
rownum=0
print reader
for row in reader:
    if rownum==0:
        #rownum+=1
        pass
    else:
        t=(row[0],row[1],row[3],int(row[7]))
        c.execute(insertSQL, t)
    rownum+=1
    
conn.commit()
c.close()    
    
