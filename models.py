from extensions import db
from utils import hash_password, verify_password

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        self.password = hash_password(password)

    def verify_password(self, password):
        return verify_password(self.password, password)