from flask import Flask, jsonify, render_template, request, redirect, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

from models import User
from utils import hash_password, verify_password
from extensions import db, jwt

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
jwt.init_app(app)

# Routes
@app.route('/login_form', methods=['GET'])
def login_form():
    return app.send_static_file('login.html')  # Assuming login.html exists

@app.route('/register_form', methods=['GET'])
def register_form():
    return render_template('register.html')  # Render registration form

# Login route
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    # Check if user exists
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"message": "User not found"}), 404

    # Verify password
    if not user.verify_password(password):
        return jsonify({"message": "Invalid password"}), 401

    # Generate access token on successful login
    access_token = create_access_token(identity={'user_id': user.id})

    # Create response, set token as cookie, and redirect to /protected
    response = make_response(redirect('/protected'))
    response.set_cookie('access_token', access_token, httponly=True)
    return response

# User registration route (moved from register route)
@app.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    # Check if username exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400  # Bad request

    # Create new user
    user = User(username=username)
    user.set_password(password)  # Use set_password method

    # Add user to database and commit changes
    db.session.add(user)
    db.session.commit()

    # Reload user to get its id
    user = User.query.filter_by(username=username).first()

    # Generate access token on successful registration
    access_token = create_access_token(identity={'user_id': user.id})

    # Create response, set token as cookie, and redirect to /protected
    response = make_response(redirect('/protected'))
    response.set_cookie('access_token', access_token, httponly=True)
    return response

# Protected route example
@app.route('/protected')
@jwt_required()
def protected_page():
    current_user = get_jwt_identity()
    return f"Welcome to the protected page, user ID: {current_user['user_id']}"

with app.app_context():
    print("Creating database tables...")
    db.create_all()
    print("Database tables created")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
