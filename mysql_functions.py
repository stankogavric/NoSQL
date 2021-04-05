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


def create_database(database_name):
    current_cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))


def show_databases():
    current_cursor.execute("SHOW DATABASES")
    return current_cursor
