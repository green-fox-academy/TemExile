import psycopg2

connection = psycopg2.connect(
    host = '',
    database = '',
    user = '',
    password = ''
)

name = ''
classname = ''
select_query = 'SELECT * FROM students'
select_query2 = 'INSERT INTO students (name, class) VALUES(%s, %s)'
select_query3 = 'SELECT * FROM students WHERE name LIKE  %s'

connection.commit()

cursor = connection.cursor()
cursor.execute(select_query)
cursor.execute(select_query2, (name, classname))
cursor.execute(select_query2, {'name': name, 'classname' = classname})
cursor.execute(select_query3, (%ddd%, ))

print(cursor.fetchall())
print(cursor.mogrigy(select_query2, (name, classname)))
print(cursor.rowcount)

cursor.close()
connection.close()