from db.cart_queries import get_cart_items, clear_cart
from decorators import logging,authorize,execution_time


@authorize("customer")
@logging
@execution_time
def checkout(current_user):
    user_id=current_user[0]

    cart_items = get_cart_items(user_id)

    if not cart_items:
        print("\nYour cart is empty.")
        return

    grand_total = 0

    print("\n========== CHECKOUT ==========")

    for item in cart_items:

        print(
            item[1],
            "x",
            item[3],
            " = ₹",
            item[4]
        )

        grand_total += item[4]

    print("-------------------------------")
    print("Total Amount: ₹", grand_total)

    confirm = input("Confirm order? (yes/no): ").strip().lower()

    if confirm == "yes":

        print("\nOrder placed successfully!")
        print("Thank you for shopping with us.")

        clear_cart(user_id)

    else:

        print("Checkout cancelled.")