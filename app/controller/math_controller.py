from model import db_connection
from model import operation_model
from utils.auth_utils import get_user_id_from_token
import logging
import json
from utils.cache_utils import cache


class MathController:

    def __init__(self):
        self.db = db_connection.get_connection()
        self.cursor = self.db.cursor()

    @cache.cached(timeout=60, query_string=True)
    def power(self, base, exponent):
        logging.info("Se execută calculul power (NU din cache)")
        try:
            base = float(base)
            exponent = float(exponent)
            import math
            result = math.pow(base, exponent)
            if not math.isfinite(result):
                return None, 'Rezultatul este prea mare sau invalid!'
            formatted = (
                f"{base}^{exponent} = "
                f"{result if result % 1 else int(result):,}"
            )
            input_data_json = json.dumps({'base': base, 'exponent': exponent})
            user_id = get_user_id_from_token()
            operation_model.insert_operation(
                self.db,
                self.cursor,
                'power',
                input_data_json,
                formatted,
                user_id
            )
            return formatted, None
        except Exception:
            logging.exception("Error in power calculation")
            return None, 'Eroare la calculul puterii!'

    @cache.cached(timeout=60, query_string=True)
    def fibonacci(self, n):
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
            for i in range(min(n + 1, 20)):
                sequence.append(x)
                x, y = y, x + y
            formatted = f"Fibonacci({n}) = {a:,}"
            input_data_json = json.dumps({'n': n})
            user_id = get_user_id_from_token()
            operation_model.insert_operation(
                self.db,
                self.cursor,
                'fibonacci',
                input_data_json,
                formatted,
                user_id
            )
            return formatted, sequence, None
        except Exception:
            logging.exception("Error in fibonacci calculation")
            return None, None, 'Eroare la calculul Fibonacci!'

    @cache.cached(timeout=60, query_string=True)
    def factorial(self, n):
        try:
            n = int(n)
            if n < 0:
                return None, 'Număr invalid!'
            import math
            result = math.factorial(n)
            formatted = f"{n}! = {result:,}"
            input_data_json = json.dumps({'n': n})
            user_id = get_user_id_from_token()
            operation_model.insert_operation(
                self.db,
                self.cursor,
                'factorial',
                input_data_json,
                formatted,
                user_id
            )
            return formatted, None
        except Exception:
            logging.exception("Error in factorial calculation")
            return None, 'Eroare la calculul factorialului!'

    def get_history(self):
        try:
            user_id = get_user_id_from_token()
            history = operation_model.get_user_history(user_id)
            return history
        except Exception:
            logging.exception("Error retrieving history")
            return None, 'Eroare la recuperarea istoricului!'
