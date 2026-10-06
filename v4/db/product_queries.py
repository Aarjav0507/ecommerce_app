from pymysql import Error
from db.connection import get_connection

def get_all_products():
    connection,cursor=get_connection()

    if connection is None:
        return None

    try:
        query="""SELECT p.product_id,p.product_name,c.category_name AS category,p.price,p.stock
        FROM products p INNER JOIN categories c
        ON p.category_id=c.category_id 
        ORDER BY p.product_id"""

        cursor.execute(query)
        for product in cursor:
            yield product
    
    except Error as e:
        print("Unable to retrieve products")
        print("database error",e)

    finally:
        cursor.close()
        connection.close()
        

def find_product(product_id):
    connection,cursor=get_connection()
    if connection is None:
        return None
    try:
        query="""SELECT p.product_id,p.product_name,c.category_name AS category,p.price,p.stock
        FROM products p INNER JOIN categories c
        ON p.category_id=c.category_id 
        WHERE p.product_id=%s"""
        cursor.execute(query,(product_id,))
        return cursor.fetchone()
    
    except Error as e:
        print("product not found")
        print("database error",e)

    finally:
        cursor.close()
        connection.close()

def get_categories():
    connection,cursor=get_connection()
    if connection is None:
        return None

    try:
        query="""SELECT category_id,category_name FROM categories
               WHERE status='ACTIVE'
               ORDER BY category_name"""
        cursor.execute(query)
        return cursor.fetchall()

    except Error as e:
        print("unable to load categories")
        print("database error",e)

    finally:
        cursor.close()
        connection.close()

def add_product_list(product_name,price,stock,category_id):
    connection,cursor=get_connection()
    if connection is None:
        return
    try:
     query="""INSERT INTO products(product_name,price,stock,category_id) VALUES(%s,%s,%s,%s)"""
     cursor.execute(query,(product_name,price,stock,category_id))
     connection.commit()
     print("Product added to cart")
     return True
    
    except Error as e:
            connection.rollback()
            print("Unable to add product to cart")
            print("Database error:", e)
            return None
    
    finally:
            
                cursor.close()
    
                connection.close()


