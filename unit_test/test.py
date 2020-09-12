import unittest
from backend.main import *

class TestLogin(unittest.TestCase):
    def __init__(self):
        self.backend = Backend()

    def addUser(self):
        query = "insert into users (username,email,image,password) values (%s,%s,%s,%s)"
        values = ("zimba12", "zimba@gmail.com", "", "zimboy12")
        self.backend.add(query, values)

    def delete(self):
        query = "delete from users where username=%s"
        values = ("user1",)
        self.backend.delete(query, values)

t = TestLogin()
t.addUser()
t.delete()