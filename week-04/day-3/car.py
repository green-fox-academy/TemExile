import psycopg2
import json

with open('cars.json', 'r') as infile:
    a = json.load(infile)

connection = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'wengleo'
)

cursor = connection.cursor()
add_query = 'INSERT INTO car (id, brand, model, year, condition, price, count) VALUES (%s, %s, %s, %s, %s, %s, %s)'
for i in range(len(a)):
    cursor.execute(add_query, list(a[i].values()))
    connection.commit()

### Modify the data
remove_car = 'DELETE FROM car WHERE count = 0'
cursor.execute(remove_car)
connection.commit()

decrease_price = 'UPDATE car SET price = price * 0.8 WHERE condition = %s'
cursor.execute(decrease_price, ('wreck',))
connection.commit()

get_age = 'SELECT sum((date_part(%s, CURRENT_DATE) - year)*count)/sum(count) FROM car'
cursor.execute(get_age, ('year',))
print(cursor.fetchall())

cursor.close()
connection.close()