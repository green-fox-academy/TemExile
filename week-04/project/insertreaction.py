import psycopg2

def add_to_reactions(rawdata):
    insert_list = []
    for msg in rawdata:
        msg_id = msg['ts']
        if 'reactions' in msg:
            for reaction in msg['reactions']:
                name = reaction['name']
                for user in reaction['users']:
                    user_id = user
                    record_list = [user_id, msg_id, name]
                    insert_list.append(record_list)
    
    connection = psycopg2.connect(
        host = 'localhost',
        database = 'second_project',
        user = 'postgres',
        password = 'wengleo'
    )
    cursor = connection.cursor()
    insert_code = 'INSERT INTO reactions (user_id, message_id, reaction) VALUES (%s, %s, %s)'
    for recordlist in insert_list:
        cursor.execute(insert_code, recordlist)
        connection.commit()
    
    cursor.close()
    connection.close()