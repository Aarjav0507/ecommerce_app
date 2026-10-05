from v1.cart.cart import (cart, add_to_cart, view_cart,remove_from_cart)
from v1.product.products import (product_details,view_products,search_product,view_categories)
from v1.constants import (VIEW_PRODUCTS, 
                       SEARCH_PRODUCT, 
                       ADD_TO_CART,
                       VIEW_CART, 
                       REMOVE_FROM_CART, 
                       CHECKOUT, 
                       VIEW_CATEGORIES, 
                       EXIT
)
from v1.checkout.checkout import checkout
from v1.custom_exceptions import ProductNotFoundError


def ecommerce_menu(current_user):
 while True:

    print("\n========== E-COMMERCE STORE ==========")
    print("1. View Products")
    print("2. Search Product")
    print("3. Add Product to Cart")
    print("4. View Cart")
    print("5. Remove Product from Cart")
    print("6. Checkout")
    print("7. View Categories")
    print("8. Exit")
    

    choice = int(input("Enter your choice: "))

    # 1. VIEW PRODUCTS
    if choice == VIEW_PRODUCTS:
          view_products(product_details)
    
    # 2. SEARCH PRODUCT
    elif choice == SEARCH_PRODUCT:
           try:
             search_product(product_details)

           except ProductNotFoundError as e:
               print(e)

       

    # 3. ADD PRODUCT TO CART
    elif choice == ADD_TO_CART:
        add_to_cart(product_details, choice, 1)

        

    # 4. VIEW CART
    elif choice == VIEW_CART:
        view_cart(cart)

       

    # 5. REMOVE PRODUCT FROM CART
    elif choice == REMOVE_FROM_CART:
        remove_from_cart(cart,choice)


        

    # 6. CHECKOUT
    elif choice == CHECKOUT:
        checkout()

        

    # 7. VIEW CATEGORIES
    elif choice == VIEW_CATEGORIES:
        view_categories(product_details)

       
    # 8. EXIT
    elif choice == EXIT:

        print("\nThank you for visiting the store!")
        break

    else:

        print("\nInvalid choice. Please enter 1-8.")
