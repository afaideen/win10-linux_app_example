from datetime import timedelta

from flask import Flask, request
from flask_login import LoginManager, UserMixin
from itsdangerous import URLSafeTimedSerializer

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=90)

login_manager = LoginManager()
login_manager.init_app(app)

serializer = URLSafeTimedSerializer(app.secret_key)

# Simulated User model
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

# @login_manager.token_loader
def load_token(token):
    duration = app.config['REMEMBER_COOKIE_DURATION'].total_seconds()
    user_id = serializer.loads(token, max_age=duration)
    return User(user_id)

# Generate token for the user
def generate_token(user_id):
    return serializer.dumps(user_id)

@app.route('/get_token/<int:user_id>')
def get_token(user_id):

    # token = serializer.dumps(user_id)
    token = generate_token(user_id)
    return token


@app.route('/protected')
def protected():
    # token = request.headers.get('key')  # Extract token from header
    token = request.args.get("key")
    if token:
        loaded_user = load_token(token)
        if loaded_user:
            return f"Access granted to user {loaded_user.id}"
    return "Unauthorized"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
