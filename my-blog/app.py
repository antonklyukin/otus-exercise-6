from flask import Flask
import psycopg2


def get_users():

    conn = psycopg2.connect(
        host="pg_db", database="my-blog", user="my-blog", password="my-pass"
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM users")

    users = cur.fetchall()

    return users


app = Flask(__name__)


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