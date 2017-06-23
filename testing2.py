import os
import sqlite3
import unittest
import urllib
import json
import collect


class TestJSONDatabase(unittest.TestCase):

    def setUp(self):

        url = 'http://www.lunin.net/24ur/page.php'
        response = urllib.urlopen(url)
        data = json.loads(response.read())

        con = sqlite3.connect("horoskop14.db")

        with con:
            c = con.cursor()

            a = data["MoonPage"]
            c.execute('''CREATE TABLE IF NOT EXISTS horoskop(date text, json varchar); ''')
            c.execute(''' INSERT INTO horoskop VALUES(?, ?); ''', (a["date"], str(a)))

        con.commit()
        con.close()

    def test_database(self):
        result = collect.collect_json_data('http://www.lunin.net/24ur/page.php', "horoskop14.db")
        self.assertIsNone(result)

    def tearDown(self):

        os.remove("horoskop14.db")