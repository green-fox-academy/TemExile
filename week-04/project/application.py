from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template('first_page.html')

@app.route('/message')
def message_page():
    connection = psycopg2.connect(
    host = 'localhost',
    database = 'second_project',
    user = 'postgres',
    password = 'wengleo')
    cursor = connection.cursor()
    cursor.execute('SELECT avg(messages) \
                    FROM (SELECT user_id, count(id) as messages \
                            FROM messages\
                            GROUP BY user_id) as table1')
    averge_messages_sent = cursor.fetchone()
    averge_messages_sent = round(float(averge_messages_sent[0]),2)
    
    cursor.close()
    connection.close()
    return render_template('message.html', avg = averge_messages_sent)



if __name__ == '__main__':
    app.run(debug=True)

