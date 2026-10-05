import pymysql

def get_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="ecommerce_app"
    )

    #print("connection created")
    cursor=conn.cursor()
    return (conn,cursor)
get_connection()