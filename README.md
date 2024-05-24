# Flask Authentication Project

This is a simple Flask project demonstrating user login and registration functionality with JWT authentication.

## Features

- User registration
- User login
- Password hashing and verification
- JWT token generation
- Protected routes

## Requirements

- Python 3.x
- Flask
- Flask-JWT-Extended
- SQLAlchemy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/flask-auth-project.git
    cd flask-auth-project
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    flask shell
    >>> from app1 import db
    >>> db.create_all()
    >>> exit()
    ```

5. Run the application:
    ```sh
    FLASK_APP=app1.py flask run
    ```

## Configuration

Configuration settings are stored in `config.py`. Update this file with your database settings and any other configuration settings as needed.

## Usage

### User Registration

Endpoint: `/register`

Method: `POST`

Request Body:
```json
{
    "username": "your_username",
    "password": "your_password"
}
