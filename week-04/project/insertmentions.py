import psycopg2

def add_to_mention(rawdata):
    insert_list = []
    for record in rawdata:
        msg_id = record['ts']
        user_id = record['user']
        record_list = [msg_id, user_id]
        insert_list.append(record_list)
    
    connection = psycopg2.connect(
        host = 'localhost',
        database = 'second_project',
        user = 'postgres',
        password = 'wengleo'
    )
    cursor = connection.cursor()
    insert_code = 'INSERT INTO mentions (message_id, user_id) VALUES (%s, %s)'
    for recordlist in insert_list:
        cursor.execute(insert_code, recordlist)
        connection.commit()
    
    cursor.close()
    connection.close()
