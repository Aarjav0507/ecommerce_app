from db.cart_queries import (
    add_item_to_cart,
    remove_from_cart,
    clear_cart,
    get_cart_items
)


def add_to_cart(user_id):

    try:
        product_id = int(input("\nEnter Product ID: "))
        quantity = int(input("Enter Quantity: "))

    except ValueError:
        print("Product ID and quantity must be integers.")
        return

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    result = add_item_to_cart(
        user_id,
        product_id,
        quantity
    )

    if result:
        print("Product added to cart.")


def view_cart(user_id):

    print("\n========== YOUR CART ==========")

    cart_items = get_cart_items(user_id)

    if not cart_items:
        print("Your cart is empty.")
        return

    grand_total = 0

    for item in cart_items:

        print(
            f"Product ID: {item[0]} | "
            f"Product: {item[1]} | "
            f"Price: ₹{item[2]} | "
            f"Quantity: {item[3]} | "
            f"Total: ₹{item[4]}"
        )

        grand_total += item[4]

    print("--------------------------------")
    print("Grand Total: ₹", grand_total)


def remove_product_from_cart(user_id):

    try:
        product_id = int(
            input("\nEnter Product ID to remove: ")
        )

    except ValueError:
        print("Product ID must be an integer.")
        return

    remove_from_cart(
        user_id,
        product_id
    )


def clear_user_cart(user_id):

    clear_cart(user_id)