import mysql.connector
import mysql_functions


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

print(mydb)
print("-------")

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE IF EXISTS asdf")

mysql_functions.show_databases(mycursor)
print("-------")

mycursor.execute("CREATE DATABASE IF NOT EXISTS asdf")

mysql_functions.show_databases(mycursor)
print("-------")


mycursor.execute("USE asdf")

mycursor.execute("DROP TABLE IF EXISTS customers")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
print("-------")

mycursor.execute(
    "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Marko", "Savska bb")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount)
print("-------")

val = [
    ("Petar", "Novosadska 21"),
    ("Ana", "Zeleznicka 5")
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount)
print("-------")

val = ("Janko", "Kosovska 15")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.lastrowid)
print("-------")


mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
print("-------")

mycursor.execute("SELECT name FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
print("-------")

sql = "SELECT * FROM customers WHERE address='Savska bb'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("-------")

sql = "SELECT * FROM customers WHERE address LIKE '%ska%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("-------")

sql = "SELECT * FROM customers WHERE address=%s"
adr = ("Savska bb",)
mycursor.execute(sql, adr)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("-------")

sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("-------")

sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
print("-------")

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Savska bb",)
mycursor.execute(sql, adr)
mydb.commit()

print(mycursor.rowcount)
print("-------")


sql = "UPDATE customers SET address = 'Niska 14' WHERE address='Kosovska 15'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount)
print("-------")


sql = "UPDATE customers SET address = %s WHERE address=%s"
val = ("Kosovska 15", "Niska 14")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount)
print("-------")
