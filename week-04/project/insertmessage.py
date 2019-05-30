import psycopg2

def add_to_message(rawdata):
    insert_list = []
    for record in rawdata:
        msg_id = record['ts']
        text = record['text']
        user_id = record['user']
        channel = 'thanks'
        record_list = [msg_id, user_id, text, channel]
        insert_list.append(record_list)
    
    connection = psycopg2.connect(
        host = 'localhost',
        database = 'second_project',
        user = 'postgres',
        password = 'wengleo'
    )
    cursor = connection.cursor()
    insert_code = 'INSERT INTO messages (id, user_id, message, channel) VALUES (%s, %s, %s, %s)'
    for recordlist in insert_list:
        cursor.execute(insert_code, recordlist)
        connection.commit()
    
    cursor.close()
    connection.close()

