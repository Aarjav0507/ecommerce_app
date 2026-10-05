import json
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
                with open("data/cart.json","w",encoding="utf-8") as file:
                     json.dump(cart,file,indent=4)

            else:

                print("Checkout cancelled.")