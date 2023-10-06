import sqlite3

connection = sqlite3.connect('folio.db')
cursor = connection.cursor()
cursor.execute('''select * from users''')
connection.commit()
connection.close()