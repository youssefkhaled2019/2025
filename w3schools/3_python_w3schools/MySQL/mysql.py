# MySQL Database : https://www.mysql.com/downloads/
# Install MySQL Driver : pip install mysql.connector
        # pip install mysql-connector-python
        # pip install mysqlclient
        # pip install pymysql
# ================================================

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword",
#   #  database="mydatabase", # If the database does not exist, you will get an error.
# ) 
# print(mydb)
# ================================================


# mycursor = mydb.cursor()
# ================================================

# Check if Database Exists
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x) 


# Creating a Database
# mycursor.execute("CREATE DATABASE mydatabase")


# ================================================

# Check if Table Exists
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x) 

# Creating a Table
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


# Create primary key when creating the table:
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))") 


# If the table already exists, use the ALTER TABLE keyword
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 

# ================================================
# Insert Into Table

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

# val = ("John", "Highway 21")

# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")



# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)
# print("1 record inserted, ID:", mycursor.lastrowid) 
# ================================================
# Update Table
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected") 


# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected") 
# ================================================
# Delete 

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)

# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)


# Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# ================================================
# Select 

# mycursor.execute("SELECT * FROM customers")
# mycursor.execute("SELECT name, address FROM customers")



# myresult = mycursor.fetchall()
# myresult = mycursor.fetchone() # method will return the first row of the result:

# for x in myresult:
#   print(x)
# ================================================
# WHERE
# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# mycursor.execute(sql)

# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)

# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)
# ================================================
# ORDER BY
# sql = "SELECT * FROM customers ORDER BY name"
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# ================================================

# DROP TABLE
# sql = "DROP TABLE customers"
# mycursor.execute(sql) 

# or Drop Only if Exist
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql) 

# ================================================
# Limit the Result
# mycursor.execute("SELECT * FROM customers LIMIT 5")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x) 

# If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:
# Start from position 3, and return 5 records:
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x) 
# ================================================
# Join Two or More Tables

# INNER JOIN
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x) 

# LEFT JOIN
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   LEFT JOIN products ON users.fav = products.id"

# RIGHT JOIN
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   RIGHT JOIN products ON users.fav = products.id"
# ================================================
