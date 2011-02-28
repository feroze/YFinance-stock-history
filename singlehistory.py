#!/usr/bin/env python

import csv
import sqlite3
import os
import urllib2
import httplib

conn= sqlite3.connect('history.db')
c=conn.cursor()

inp=str(raw_input())

c.execute('''DROP TABLE IF EXISTS '''+inp)

c.execute('''CREATE TABLE ''' +inp+ ''' (
    date TEXT,
    open TEXT,
    high TEXT,
    low TEXT,
    close TEXT,
    volume TEXT)
''')

insertSQL='''INSERT INTO '''+inp+''' VALUES (?,?,?,?,?,?)'''

response = urllib2.urlopen("http://ichart.finance.yahoo.com/table.csv?s="+inp+".NS&a=07&b=12&c=2002&d=01&e=6&f=2011&g=d&ignore=.csv")

csvfile=response.read()
#print csvfile
fout=open('temp.csv','w')
fout.write(csvfile)
fout.close()
reader=csv.reader(open('temp.csv','rb'))
os.remove('temp.csv')
rownum=0
#print reader
for row in reader:
    if rownum==0:
        #rownum+=1
        pass
    else:
        print row
        t=(row[0],row[1],row[2],row[3],row[4],row[5])
        c.execute(insertSQL, t)
    rownum+=1
    
conn.commit()
c.close()    
    



