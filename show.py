from flask import Flask
from flask import jsonify
import sqlite3


con = sqlite3.connect("horoskop14.db")

with con:
    c = con.cursor()

    c.execute("SELECT json FROM horoskop")

    rows = c.fetchall()


app = Flask(__name__)


@app.route('/')
def show():
    return jsonify(rows)

if __name__ == '__main__':
    app.run()
