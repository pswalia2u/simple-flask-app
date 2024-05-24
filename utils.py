from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

def create_jwt_payload(user):
    payload = {'user_id': user.id}
    return payload

def hash_password(password):
    return generate_password_hash(password)

def verify_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

def generate_token(user):
    payload = create_jwt_payload(user)
    return create_access_token(identity=payload)