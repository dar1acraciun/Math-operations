def insert_operation(connection,
                     cursor,
                     endpoint, input_data, result, user_id):
    """
    Inserts a new operation into the OPERATIONS table.

    :param endpoint: The type of operation (e.g., 'add', 'subtract').
    :param input_data: The input data for the operation in JSON format.
    :param result: The result of the operation.
    """
    query = """
    INSERT INTO OPERATIONS (endpoint, input_data, result,user_id)
    VALUES (%s, %s, %s,%s)
    """
    cursor.execute(query, (endpoint, input_data, result, user_id))
    connection.commit()

def get_user_history(user_id, limit=20):
    from model import db_connection
    db = db_connection.get_connection()
    cursor = db.cursor()
    cursor.execute(
        "SELECT endpoint, result, created_at FROM OPERATIONS WHERE user_id = %s ORDER BY created_at DESC LIMIT %s",
        (user_id, limit)
    )
    rows = cursor.fetchall()
    history = []
    for row in rows:
        history.append({
            'operation': row[0],
            'result': row[1],
            'time': row[2].strftime('%Y-%m-%d %H:%M') if row[2] else ''
        })
    return history
