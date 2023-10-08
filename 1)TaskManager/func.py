import sqlite3

from secr import *


#connection.commit()


def login(name,passw):
    table="test"
    connection = sqlite3.connect('folio.db')
    cursor = connection.cursor()
    if "@"in name and (".ru" in name or ".com"in name or ".org" in name):
        cursor.execute(f'''select id,username from {table} where email='{name}' and pass='{passw}';''')
    else:
         cursor.execute(f'''select id,username from {table} where username='{name}' and pass='{passw}';''')
    res=cursor.fetchall()
    print(type(res[0]))
    connection.close()
    if res!=[]:
        nick=res[0][1]
        id_u=res[0][0]
        
        return (True,id_u,nick)
    else:
        return(False,"0","0")

a,n,p=login ("hellmin","123456")
print(f"проверка: {a}\n\r id= {n}; name= {p}")