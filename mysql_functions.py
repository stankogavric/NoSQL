import mysql.connector


def connection(host, user, password):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        return mydb
    except mysql.connector.Error as err:
        print(err)
        raise


def create_database(mydb, database_name):
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))


def show_databases(mycursor):
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)
