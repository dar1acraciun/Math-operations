
from model import db_connection
from model import user_model


class RegisterController:

    def __init__(self):
        self.db = db_connection.get_connection()
        self.cursor = self.db.cursor()

    def register(self, nume, prenume, email, password, conf_password):
        if password != conf_password:
            return {"error": "Passwords do not match"}
        if not user_model.is_email_unique(self.cursor, email):
            return {"error": "Email already exists"}
        user = user_model.create_user(
            self.db, self.cursor, nume, prenume, email, password
        )
        if user:
            return {"success": "User registered successfully"}
        return {"error": "User registration failed"}
