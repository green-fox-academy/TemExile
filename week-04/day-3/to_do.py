import sys
import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'wengleo'
)

cursor = connection.cursor()
list_query = 'SELECT * FROM todotask'
add_query = 'INSERT INTO todotask (task) VALUES (%s)'
remove_query = 'DELETE FROM todotask WHERE listnumber = %s'


if sys.argv[1] == '-l':
    cursor.execute(list_query)
    ab = cursor.fetchall()
    if len(ab) == 0:
        print(f'There is no task')
    else:
        for i in range(len(ab)):
            print(f'{i+1} - {ab[i][0]}')
elif sys.argv[1] == '-a':
    cursor.execute(add_query, (sys.argv[2],))
    connection.commit()
elif sys.argv[1] == '-c':
    cursor.execute(list_query)
    ab = cursor.fetchall()
    if int(sys.argv[2]) > len(ab):
        print(f'No such task')
    else:
        print(f'{sys.argv[2]} - {ab[int(sys.argv[2])-1][0]}')
elif sys.argv[1] == '-r':
    cursor.execute(list_query)
    ab = cursor.fetchall()
    if int(sys.argv[2]) > len(ab):
        print(f'No such task')
    else:
        rid = ab[int(sys.argv[2])-1][1]
        cursor.execute(remove_query, (rid,))
        connection.commit()

