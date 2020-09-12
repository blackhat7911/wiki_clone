import unittest
from backend.main import *

class TestDB(unittest.TestCase):
    def setUp(self):
        self.backend = Backend()

    def test_add(self):
        query = "insert into posts (title,information,image,username) values (%s, %s, %s, %s)"
        values = ("Apple", "Apple is a fruit, A for apple bla bla bla", "", "test")
        expect = True
        actual = self.backend.add(query, values)
        self.assertEqual(expect, actual)

if __name__ == '__main__':
    unittest.main()
