from model import db_connection
from model import operation_model
import logging
import json

def power(base, exponent):
    try:
        base = float(base)
        exponent = float(exponent)
        import math
        result = math.pow(base, exponent)
        if not math.isfinite(result):
            return None, 'Rezultatul este prea mare sau invalid!'
        formatted = f"{base}^{exponent} = {result if result % 1 else int(result):,}"
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        input_data_json = json.dumps({'base': base, 'exponent': exponent})

        operation_model.insert_operation(conn, cursor, 'power', input_data_json, formatted)
        cursor.close()
        conn.close()
        return formatted, None
    except Exception:
        logging.exception("Error in power calculation")
        return None, 'Eroare la calculul puterii!'
 
def fibonacci(n):
    try:
        n = int(n)
        if n < 0:
            return None, None, 'Număr invalid!'
        if n > 1000:
            return None, None, 'Numărul este prea mare! (max 1000)'
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        sequence = []
        x, y = 0, 1
        for i in range(min(n+1, 20)):
            sequence.append(x)
            x, y = y, x + y
        formatted = f"Fibonacci({n}) = {a:,}"
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        input_data_json = json.dumps({'n': n})
        operation_model.insert_operation(conn, cursor, 'fibonacci', input_data_json, formatted)
        cursor.close()
        conn.close()
        return formatted, sequence, None
    except Exception:
        logging.exception("Error in fibonacci calculation")
        return None, None, 'Eroare la calculul Fibonacci!'

def factorial(n):
    try:
        n = int(n)
        if n < 0:
            return None, 'Număr invalid!'
        import math
        result = math.factorial(n)
        formatted = f"{n}! = {result:,}"
        conn = db_connection.get_connection()
        cursor = conn.cursor()
        input_data_json = json.dumps({'n': n})
        operation_model.insert_operation(conn, cursor, 'factorial', input_data_json, formatted)
        cursor.close()
        conn.close()
        return formatted, None
    except Exception:
        logging.exception("Error in factorial calculation")
        return None, 'Eroare la calculul factorialului!'