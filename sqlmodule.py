import mysql.connector as sqlctr

def connect_server(pw):
    connection=None
    try:
        connection=sqlctr.connect(
            host="localhost",
            user="root",
            password=pw
        )
        val=1
    except:
        print("Incorrect Password")
        val=0
    return connection,pw,val

def connect_database(pwd):
    connection=None
    try:
        connection=sqlctr.connect(
            host="localhost",
            user="root",
            password=pwd,
            database="Medical_Store_DB"
        )
    except:
        pass
    return connection

def execute_query(connection,query):
    cursor=connection.cursor()
    cursor.execute(query)
    connection.commit()

def read_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result



