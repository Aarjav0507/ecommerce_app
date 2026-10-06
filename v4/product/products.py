from db.product_queries import (
    get_all_products,
    find_product,
    get_categories,add_product_list
)
from decorators import authorize,logging,execution_time


@logging
@execution_time
def view_products(current_user):
    print("\n========== PRODUCTS ==========")

    products = get_all_products()

    if not products:
        print("No products available.")
        return
    
    

    for product in products:
        print(
            f"ID: {product[0]} | "
            f"Name: {product[1]} | "
            f"Category: {product[2]} | "
            f"Price: ₹{product[3]} | "
            f"Stock: {product[4]}"
        )

@logging
@execution_time
def search_product(current_user):
    try:
        product_id = int(input("\nEnter product ID: "))

    except ValueError:
        print("Product ID must be an integer.")
        return

    product = find_product(product_id)

    if product is None:
        print("Product not found.")
        return
    

    print("\n========== PRODUCT DETAILS ==========")
    print("Product ID:", product[0])
    print("Product Name:", product[1])
    print("Category:", product[2])
    print("Price:", product[3])
    print("Stock:", product[4])

@logging
@execution_time
def view_categories(current_user):
    print("\n========== CATEGORIES ==========")

    categories = get_categories()

    if not categories:
        print("No categories available.")
        return

    for category in categories:
        print(
            f"ID: {category[0]} | "
            f"Category: {category[1]}"
        )


@authorize("admin")
@logging
@execution_time
def add_product(current_user):
    
    product_name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter product stock: "))
    category_id=int(input("enter the category_id:"))

    print("\nProduct added successfully!")
    add_product_list(product_name,price,stock,category_id)