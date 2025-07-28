def get_user_by_email(cursor, email):
    cursor.execute("SELECT * FROM USERS WHERE email = %s", (email,))
    return cursor.fetchone() or None


def check_password(user, password):
    from werkzeug.security import check_password_hash
    return check_password_hash(user[3], password)


def create_user(connection, cursor, first_name, last_name, email, password):
    from werkzeug.security import generate_password_hash
    hashed_password = generate_password_hash(password)
    cursor.execute(
        "INSERT INTO USERS (first_name, last_name, email, password) "
        "VALUES (%s, %s, %s, %s)",
        (first_name, last_name, email, hashed_password)
    )
    connection.commit()
    return cursor.lastrowid


def is_email_unique(cursor, email):
    cursor.execute("SELECT * FROM USERS WHERE email = %s", (email,))
    return cursor.fetchone() is None