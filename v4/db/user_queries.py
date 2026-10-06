from pymysql import Error
from db.connection import get_connection


def create_user(full_name,email,phone,password):
    connection,cursor=get_connection()
    if connection is None: 
       
       return None
        
    try:
        query="""INSERT INTO users(full_name,email,phone,password) VALUES(%s,%s,%s,%s)"""
        cursor.execute(query,(full_name,email,phone,password))
        connection.commit()
        return True
    except Error as e:
        connection.rollback()
        print("unable to create user")
        print("database error",e)
        

    finally:
        cursor.close()
        connection.close()

def find_user_by_email(email):
    connection,cursor=get_connection()
    if connection is None:
        return None
    try:
        query="""SELECT user_id,full_name,email,phone,password,role FROM users where email=%s"""
        cursor.execute(query,(email,))
        
        return cursor.fetchone()
    except Error as e:
        print("unable to find user")
        print("database error",e)
        
    finally:
        cursor.close()
        connection.close()

def update_password(user_id,password):
    connection,cursor=get_connection()
    if connection is None:
        return None
    try:
        query="""UPDATE users set password=%s WHERE user_id=%s"""
        cursor.execute(query,(password,user_id))
        connection.commit()
    except Error as e:
        print("password could not be updated")
        print("database error",e)
    finally:
        cursor.close()
        connection.close()