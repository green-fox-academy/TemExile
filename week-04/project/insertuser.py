import psycopg2

def add_to_users(rawdata):
    insert_list = []
    user_set = set()
    for record in rawdata:
        user_id = record['user']
        user_set.add(user_id)
        if 'reactions' in record:
            for reaction in record['reactions']:
                for user in reaction['users']:
                    user_set.add(user)
    insert_list = list(user_set)
    connection = psycopg2.connect(
        host = 'localhost',
        database = 'second_project',
        user = 'postgres',
        password = 'wengleo'
    )
    cursor = connection.cursor()
    insert_code = 'INSERT INTO users (user_id) VALUES (%s)'
    for recordlist in insert_list:
        cursor.execute(insert_code, (recordlist,))
        connection.commit()
    
    cursor.close()
    connection.close()