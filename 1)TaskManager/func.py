import sqlite3

from secr import to_sim,to_let,dictionary


#connection.commit()


def login(name,passw):
    table="test"
    connection = sqlite3.connect('folio.db')
    cursor = connection.cursor()
    if "@"in name and (".ru" in name or ".com"in name or ".org" in name):
        cursor.execute(f'''select id,username from {table} where email='{to_sim(name,dictionary)}' and pass='{to_sim(passw,dictionary)}';''')
    else:
         cursor.execute(f'''select id,username from {table} where username='{to_sim(name,dictionary)}' and pass='{to_sim(passw,dictionary)}';''')
    res=cursor.fetchall()
    
    connection.close()
    if res!=[]:
        nick=res[0][1]
        id_u=res[0][0]
        
        return (True,to_let(id_u,dictionary),to_let(nick,dictionary))
    else:
        return(False,"0","0")

def sign_up_back(name,email,passw):
    table="test"
    connection = sqlite3.connect('folio.db')
    cursor = connection.cursor()
    cursor.execute(f'''select * from {table} where email='{email}' or username='{name}';''')
    if (cursor.fetchall()==[]):
        cursor.execute(f'''insert into {table} ([username],[email],[pass]) values ('{name}','{email}','{to_sim(passw,dictionary)}')''')
        connection.commit()
        connection.close()
        return "ok"
    else:
        cursor.execute(f"select * from {table} where email='{email}'")
        if (cursor.fetchall()!=[]):
            connection.close()
            return "email уже зарагастрирован"
        cursor.execute(f"select * from {table} where username='{name}'")
        if (cursor.fetchall()!=[]):
            connection.close()
            return "такой ник уже существует"
        connection.close()
        return("что-то пошло не так")
    
    


'''
a,n,p=login ("hellmin","123457")
print(f"проверка: {a};\n\r id={n}; name={p}")'''

#print(sign_up_back("qqq","aa@aa.aa","qwerty"))