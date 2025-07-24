def insert_operation(connection,cursor,endpoint, input_data, result):
    """
    Inserts a new operation into the OPERATIONS table.
    
    :param endpoint: The type of operation (e.g., 'add', 'subtract').
    :param input_data: The input data for the operation in JSON format.
    :param result: The result of the operation.
    """
    query = """
    INSERT INTO OPERATIONS (endpoint, input_data, result)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (endpoint, input_data, result))
    connection.commit()