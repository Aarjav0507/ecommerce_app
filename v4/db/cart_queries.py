from pymysql import Error
from db.connection import get_connection

def get_cart_items(user_id):
    connection,cursor=get_connection()
    if connection is None:
        return None
    try:
        query="""SELECT ci.product_id,p.product_name,p.price,ci.quantity,(p.price*ci.quantity) AS item_total
               FROM cart_items ci
               INNER JOIN products p
               ON ci.product_id=p.product_id
               WHERE ci.user_id=%s
               ORDER BY ci.cart_item_id"""
        cursor.execute(query,(user_id,))
        return cursor.fetchall()
    except Error as e:
        print("unable to load cart")
        print("database error",e)

    finally:
        cursor.close()
        connection.close()


def add_item_to_cart(user_id, product_id, quantity):

    connection,cursor = get_connection()

    if connection is None:
        return None
    try:
        

        # Check product
        query = """
            SELECT product_id, product_name, price, stock
            FROM products
            WHERE product_id = %s
        """

        cursor.execute(query, (product_id,))
        product = cursor.fetchone()

        if product is None:
            print("Product not found")
            return None

        
        if quantity > product[3]:
            print("Insufficient stock")
            return None

    
        query = """
            SELECT cart_item_id, quantity
            FROM cart_items
            WHERE user_id = %s AND product_id = %s
        """

        cursor.execute(query, (user_id, product_id))
        cart_item = cursor.fetchone()

        if cart_item:
            new_quantity = cart_item[1] + quantity

            if new_quantity > product[3]:
                print("Insufficient stock")
                return None

            query = """
                UPDATE cart_items
                SET quantity = %s
                WHERE cart_item_id = %s
            """

            cursor.execute(query, (new_quantity, cart_item[0]))

        else:
            query = """
                INSERT INTO cart_items(user_id, product_id, quantity)
                VALUES(%s, %s, %s)
            """

            cursor.execute(query, (user_id, product_id, quantity))

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

def remove_from_cart(user_id,product_id):
    connection,cursor=get_connection()
    if connection is None:
            return None

    try:
        query="""DELETE from cart_items where user_id=%s AND product_id=%s"""
        cursor.execute(query,(user_id,product_id))

        if cursor.rowcount==0:
            print("product not found in cart")
            return False

        connection.commit()
        print("product removed from cart")
        return True
    except Error as e:
        connection.rollback()
        print("Unable to remove product from cart")
        print("Database error:", e)


    finally:
        
            cursor.close()

            connection.close()

def clear_cart(user_id):
     connection,cursor=get_connection()
     if connection is None:
                 return None
     
     try:
             query="""DELETE from cart_items where user_id=%s"""
             cursor.execute(query,(user_id,))
     
             if cursor.rowcount==0:
                 print("product not found in cart")
                 return False
     
             connection.commit()
             print("cart cleared")
             return True
     except Error as e:
             connection.rollback()
             print("Unable to remove product from cart")
             print("Database error:", e)
     
     
     finally:
             
                 cursor.close()
     
                 connection.close()
     


