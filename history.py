#!/usr/bin/env python

import csv
import sqlite3
import os
import urllib2
import httplib

def gethist(sym):
    inp=str(sym[0])
    print inp
    conn= sqlite3.connect('history.db')
    c=conn.cursor()
    
    
    c.execute('''DROP TABLE IF EXISTS _'''+inp)
    
    c.execute('''CREATE TABLE _''' +inp+ ''' (
        date TEXT,
        open TEXT,
        high TEXT,
        low TEXT,
        close TEXT,
        volume TEXT)
    ''')
    
    insertSQL='''INSERT INTO _'''+inp+''' VALUES (?,?,?,?,?,?)'''
    response = None
    try:
        response = urllib2.urlopen("http://ichart.finance.yahoo.com/table.csv?s="+inp+".NS&a=07&b=12&c=2002&d=01&e=6&f=2011&g=d&ignore=.csv")
    except Exception:
        return
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
    


donn= sqlite3.connect('company.db')
d=donn.cursor()

d.execute('SELECT symbol FROM equity WHERE face=1')

for tow in d:
    print tow
    gethist(tow)