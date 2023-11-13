from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event

app = Flask(__name__)

# PostgreSQL database URI
db_uri = 'postgresql://han:123@127.0.0.1:5432/testdb'

# Configure the Flask app to use the database
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy object
db = SQLAlchemy(app)

# Sample model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

# Route to create a sample user
@app.route('/create_user')
def create_user():
    new_user = User(username='JohnDoe', email='john@example.com')
    db.session.add(new_user)
    db.session.commit()
    return 'User created!'

if __name__ == '__main__':
    app.run(debug=True)
