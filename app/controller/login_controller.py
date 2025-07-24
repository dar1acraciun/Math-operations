from model import db_connection
from model import user_model

import logging

class LoginController:
    def __init__(self):
        self.db = db_connection.get_connection()
        self.cursor = self.db.cursor()

    def login(self, email, password):
        logging.info(f"Login attempt for {email}")
        user = user_model.get_user_by_email(self.cursor, email)
        if user and user_model.check_password(user, password):
            logging.info(f"Login SUCCESS for {email}")
            return {"status": "success", "message": "Login successful"}
        else:
            logging.warning(f"Login FAILED for {email}")
            return {"status": "error", "message": "Invalid email or password"}

    def close_connection(self):
        self.cursor.close()
        self.db.close()

