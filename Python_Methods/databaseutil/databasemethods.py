"""Cursor Object:->It is an object that is used to make the connection for executing SQL queries.
It acts as middleware between SQLite database connection and SQL query. """

from  databaseutil import  sqlitemethods

class DatabaseMethod:
    def databaseActions(self):
        choice = int(input("1.SQLite :"))
        if choice == 1:
            sqlitemethods.SQLiteMethod().sqliteActions()

