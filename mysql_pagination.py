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

while True:
    limit_per_page = int(input("LIMIT: "))
    page = (int(input("PAGE: "))-1)*limit_per_page

    sql = "SELECT * FROM customers LIMIT %s OFFSET %s"
    val = (limit_per_page, page)
    current_cursor.execute(sql, val)
    r = current_cursor.fetchall()
    print(r)   