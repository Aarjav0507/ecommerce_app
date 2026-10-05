from v1.cart.cart import cart
def checkout():

    if len(cart) == 0:

            print("\nYour cart is empty.")

    else:

            grand_total = 0

            print("\n========== CHECKOUT ==========")

            for item in cart:

                print(
                    item["Product"],
                    "x",
                    item["Quantity"],
                    " =",item["Total Price"]
                )

                grand_total += item["Total Price"]

            print("-------------------------------")
            print("Total Amount: ₹", grand_total)

            confirm = input("Confirm order? (yes/no): ").lower()

            if confirm == "yes":

                print("\nOrder placed successfully!")
                print("Thank you for shopping with us.")

                cart.clear()

            else:

                print("Checkout cancelled.")