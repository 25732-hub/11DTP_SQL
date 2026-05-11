import sqlite3
print('Hello world!')
db = sqlite3.connect('11DTP.db')
cursor = db.cursor()
sql = 'SELECT * FROM fighters;'
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()