import sqlite3
import urllib
import json


def collect_json_data(url, db_name):
    #url = 'http://www.lunin.net/24ur/page.php'
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    con = sqlite3.connect(db_name)

    with con:
        c = con.cursor()

        a = data["MoonPage"]

        c.execute('''CREATE TABLE IF NOT EXISTS horoskop(date text, json varchar); ''')
        c.execute(''' INSERT INTO horoskop VALUES(?, ?); ''', (a["date"], str(a)))

        c.execute("SELECT json FROM horoskop")
        rows = c.fetchall()
        print rows

    con.commit()
    con.close()


collect_json_data('http://www.lunin.net/24ur/page.php', "horoskop14.db")
