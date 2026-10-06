from cart.cart import ( add_to_cart, view_cart,remove_product_from_cart)
from product.products import (view_products,search_product,view_categories,add_product)
from constants import (VIEW_PRODUCTS, 
                       SEARCH_PRODUCT, 
                       ADD_TO_CART,
                       VIEW_CART, 
                       REMOVE_FROM_CART, 
                       CHECKOUT, 
                       VIEW_CATEGORIES, 
                       EXIT, ADD_PRODUCT
)
from checkout.checkout import checkout
from custom_exceptions import ProductNotFoundError


def ecommerce_menu(current_user):
 user_id=current_user[0]
 while True:

    print("\n========== E-COMMERCE STORE ==========")
    print("1. View Products")
    print("2. Search Product")
    print("3. Add Product to Cart")
    print("4. View Cart")
    print("5. Remove Product from Cart")
    print("6. Checkout")
    print("7. View Categories")
    print("8. Add product ")
    print("9. Exit")
    

    choice = int(input("Enter your choice: "))

    # 1. VIEW PRODUCTS
    if choice == VIEW_PRODUCTS:
          view_products(current_user)
    
    # 2. SEARCH PRODUCT
    elif choice == SEARCH_PRODUCT:
           try:
             search_product(current_user)

           except ProductNotFoundError as e:
               print(e)

       

    # 3. ADD PRODUCT TO CART
    elif choice == ADD_TO_CART:
        add_to_cart(current_user)

        

    # 4. VIEW CART
    elif choice == VIEW_CART:
        view_cart(current_user)

       

    # 5. REMOVE PRODUCT FROM CART
    elif choice == REMOVE_FROM_CART:
        remove_product_from_cart(current_user)


        

    # 6. CHECKOUT
    elif choice == CHECKOUT:
        checkout(current_user)

        

    # 7. VIEW CATEGORIES
    elif choice == VIEW_CATEGORIES:
        view_categories(current_user)

    #8. ADD PRODUCT
    elif choice==ADD_PRODUCT:
        add_product(current_user)

       
    # 9. EXIT
    elif choice == EXIT:

        print("\nThank you for visiting the store!")
        break

    else:

        print("\nInvalid choice. Please enter 1-8.")
