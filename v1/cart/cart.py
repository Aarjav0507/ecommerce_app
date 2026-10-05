

cart= [
     {"Product ID":101,"Product":"Laptop","Price":75000,"Quantity":1,"Total Price":75000},
     {"Product ID":102,"Product":"Mouse","Price":3000,"Quantity":2,"Total Price":6000}

]

def add_to_cart(product_details, product_id, quantity):
    try:
      product_id = int(input("\nEnter Product ID: "))
    except ValueError:
           print("The product id must be integer")
    
    found = False
    
    for product in product_details:
    
                if product["Product ID"] == product_id:
    
                    found = True
    
                    # Check if product already exists in cart
                    already_in_cart = False
    
                    for item in cart:
    
                        if item["Product ID"] == product_id:
    
                            item["Quantity"] += 1
                            item["Total Price"] = (
                                item["Price"] * item["Quantity"]
                            )
    
                            already_in_cart = True
    
                            print("Product quantity increased.")
                            break
    
                    # If product is not already in cart
                    if already_in_cart == False:
    
                        new_item = {
                            "Product ID": product["Product ID"],
                            "Product": product["Product"],
                            "Price": product["Price"],
                            "Quantity": 1,
                            "Total Price": product["Price"]
                        }
    
                        cart.append(new_item)
    
                        print("Product added to cart.")
    
                    break
    
                    if found == False:
                      print("Product not found.")

def view_cart(cart):
      print("\n========== YOUR CART ==========")
     
      if len(cart) == 0:
     
                 print("Your cart is empty.")
     
      else:
     
          grand_total = 0
     
          for item in cart:
     
                     print(
                         item["Product ID"],
                         "|",
                         item["Product"],
                         "| ₹" + str(item["Price"]),
                         "| Qty:",
                         item["Quantity"],
                         "| Total: ₹" + str(item["Total Price"])
                     )
     
                     grand_total += item["Total Price"]
     
          print("-------------------------------")
          print("Grand Total: ₹", grand_total)

def remove_from_cart(cart, product_id):
      product_id = input("\nEnter Product ID to remove: ")
      
      found = False
      
      for item in cart:
      
                  if item["Product ID"] == product_id:
      
                      cart.remove(item)
      
                      print("Product removed from cart.")
      
                      found = True
                      break
      
      if found == False:
                  print("Product not found in cart.")