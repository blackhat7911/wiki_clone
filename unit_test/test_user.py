import unittest
from model.user_model import *

class Test_User(unittest.TestCase):
    def setUp(self):
        self.user = User("", "", "", "")

    def test_set_name(self):
        self.user.set_name("Bishal")
        self.assertEqual("Bishal", self.user.get_name())

    def test_get_name(self):
        self.assertEqual("Bishal", self.user.get_name())

if __name__ == '__main__':
    unittest.main()