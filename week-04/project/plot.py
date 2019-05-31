import matplotlib.pyplot as plt
import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    database = 'second_project',
    user = 'postgres',
    password = 'wengleo'
)
cursor = connection.cursor()
cursor.execute('SELECT user_id, count(id) as messages \
                FROM messages \
                GROUP BY user_id ORDER BY count(id) DESC')
messages_sent = cursor.fetchall()
user = []
message = []
for r in messages_sent:
    user.append(r[0])
    message.append(r[1])
n, bins, patches = plt.hist(x = message, bins = 5, 
                            facecolor='blue', alpha = 0.5)
plt.xlabel('Message sent')
plt.ylabel('Frequence(%)')
plt.title(r'The Distribution of Message Sent Amount, $\mu = 9.13$')
plt.show()

cursor.close()
connection.close()