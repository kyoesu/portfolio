import sqlite3

from secr import *


#connection.commit()


def login(name,passw):
    table="test"
    connection = sqlite3.connect('folio.db')
    cursor = connection.cursor()
    if "@"in name and (".ru" in name or ".com"in name or ".org" in name):
        cursor.execute(f'''select id,name from {table} where email={name} and pass={passw}''')
    else:
         cursor.execute(f'''select id,name from {table} where name={name} and pass={passw}''')
    res=cursor.fetchall()
    connection.close()
    if res!="":
        nick=""
        id_u=''
        
        return (True,id_u,nick)
    else:
        return(False,"0","0")