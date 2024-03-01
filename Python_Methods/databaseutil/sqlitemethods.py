import  sqlite3
class SQLiteMethod:

    def sqliteActions(self):
        #self.sqliteConnection() # create connection
        #self.tableCreation() # table creation
        #self.insert() # data insertion
        #self.fetch()
        #self.update()
        #self.delete()
        self.dropTable()
        self.fetch()

    def sqliteConnection(self):
        print("\nSQLite3 database connection..")
        connection = sqlite3.connect("gfg.db") # connecting to the database
        cursor = connection.cursor() # cursor
        print("Connected to the database") # print statement will execute if there are no errors
        connection.close()

    def tableCreation(self):
        print("\nTable Creation")
        connection = sqlite3.connect("gfg.db") # connecting to the database
        crsr = connection.cursor() # cursor
        # SQL command to create a table in the database
        sql_command = """CREATE TABLE emp ( staff_number INTEGER PRIMARY KEY, fname VARCHAR(20), lname VARCHAR(30), gender CHAR(1), joining DATE);"""

        crsr.execute(sql_command) # execute the statement
        print("Table Created Successfully")
        connection.close() # close the connection

    def insert(self):
        connection = sqlite3.connect("gfg.db") # connecting to the database
        crsr = connection.cursor() # cursor

        # SQL command to insert the data in the table
        sql_command = """INSERT INTO emp VALUES (22, "Rishabh","Bansal", "M", "2014-03-28");"""
        crsr.execute(sql_command)

        sql_command = """INSERT INTO emp VALUES (11, "Bill", "Gates","M", "1980-10-28");""" # another SQL command to insert the data in the table
        crsr.execute(sql_command)

        #Inserting data input by the user
        pk = [2, 3, 4, 5, 6]  # primary key
        f_name = ['Nikhil', 'Nisha', 'Abhinav', 'Raju', 'Anshul']  # Enter 5 students first names
        l_name = ['Aggarwal', 'Rawat', 'Tomar', 'Kumar', 'Aggarwal'] # Enter 5 students last names
        gender = ['M', 'F', 'M', 'M', 'F'] # Enter their gender respectively
        date = ['2019-08-24', '2020-01-01', '2018-05-14', '2015-02-02', '2018-05-14'] # Enter their jpining data respectively

        for i in range(5):
            crsr.execute(f'INSERT INTO emp VALUES ({pk[i]},"{f_name[i]}","{l_name[i]}","{gender[i]}","{date[i]}")')# This is the q-mark style:


        connection.commit() # If we skip this, nothing will be saved in the database.# To save the changes in the files. Never skip this.
        connection.close() # close the connection

    def fetch(self):
        connection = sqlite3.connect("gfg.db") # connect withe the myTable database
        crsr = connection.cursor() # cursor object
        crsr.execute("SELECT * FROM emp") # execute the command to fetch all the data from the table emp

        ans = crsr.fetchall() # store all the fetched data in the ans variable
        # Since we have already selected all the data entries
        # using the "SELECT *" SQL command and stored them in
        # the ans variable, all we need to do now is to print
        # out the ans variable
        for i in ans:
            print(i)

    def update(self):
        connection = sqlite3.connect('gfg.db') # Connecting to sqlite
        cursor = connection.cursor() # Creating a cursor object using he cursor() method
        cursor.execute('''UPDATE emp SET lname = "Jyoti" WHERE fname="Rishabh";''')# Updating

        connection.commit() # Commit your changes in the database
        connection.close()

    def delete(self):
        conn = sqlite3.connect('gfg.db')
        cursor = conn.cursor() # Creating a cursor object using
        cursor.execute('''DELETE FROM emp WHERE fname="Rishabh";''') # Updating

        conn.commit() # Commit your changes in the database
        conn.close() # Closing the connection

    def dropTable(self):
        conn = sqlite3.connect('gfg.db')
        cursor = conn.cursor() # Creating a cursor object using the cursor() method
        cursor.execute('''DROP TABLE emp;''')# Updating
        conn.close() # Closing the connection

