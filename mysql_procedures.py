import mysql.connector

current_connection = None
current_cursor = None

def connection(host, user, password):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        global current_connection
        current_connection = mydb
        global current_cursor
        current_cursor=current_connection.cursor()
        return mydb
    except mysql.connector.Error as err:
        print(err)
        raise


def use_database(database_name):
    current_cursor.execute("USE {}".format(database_name))

connection("localhost", "root", "root")
use_database("asdf")

current_cursor.callproc("show_databases")
for i in current_cursor.stored_results():
    print(i.fetchall())

r = current_cursor.callproc("insert_into_customers", ("marko", "ulica 2"))
print(r)
current_connection.commit()

r = current_cursor.callproc("multiply", (5, 4, 0))
print(r)

r = current_cursor.callproc("multiply2", (5, 4))
print(r)

r = current_cursor.callproc("insert_into_customers", ("marko2", "ulica 222"))
print(r)
current_connection.commit()