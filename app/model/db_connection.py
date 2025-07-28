
import mysql.connector
import time


def get_connection(retries=5, delay=3):
    for attempt in range(retries):
        try:
            conn = mysql.connector.connect(
                host="db",
                user="user",
                password="userpass",
                database="mathdb"
            )
            return conn
        except mysql.connector.Error as err:
            print(
                f"MySQL connection failed: {err}. "
                f"Retrying in {delay} seconds..."
            )
            time.sleep(delay)
    raise Exception("Could not connect to MySQL after several attempts.")
