from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import psycopg2


# def get_users():

#     conn = psycopg2.connect(
#         host="pg_db", database="my-blog", user="my-blog", password="my-pass"
#     )

#     cur = conn.cursor()

#     cur.execute("SELECT * FROM users")

#     users = cur.fetchall()

#     return users


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://my-blog:my-pass@pg_db:5432/my-blog'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Post %r>' % self.username

@app.route("/")
def index():
    """
    Render a Hello World response.

    :return: Flask response
    """
    users = get_users()

    return str(users)


if __name__ in "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)