from db.product_queries import (
    get_all_products,
    find_product,
    get_categories
)


def view_products():
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


def search_product():
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


def view_categories():
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