import mysql.connector

class Backend:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="bishal",
            password="Bishal@123",
            database="wiki",
            auth_plugin="mysql_native_password"
        )
        self.cur = self.conn.cursor()
        if self.conn.is_connected():
            print("Connected")

    def add(self, query, values):
        self.cur.execute(query, values)
        self.conn.commit()

    def update(self, query, values):
        self.cur.execute(query, values)
        self.conn.commit()

    def delete(self, query, values):
        self.cur.execute(query, values)
        self.conn.commit()
