import os
import unittest
import show
import tempfile


class ShowTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, show.app.config['DATABASE'] = tempfile.mkstemp()
        show.app.testing = True
        self.app = show.app.test_client()

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'horoskop' in rv.data

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(show.app.config['DATABASE'])




