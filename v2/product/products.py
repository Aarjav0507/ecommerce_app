from v1.custom_exceptions import( EcommerceError,ProductNotFoundError,CategoryNotFoundError)
import json
# product_details=[
#     {"Product ID":101,"Product":"Laptop","Price":75000,"Quantity":10,"Category":"Electronics"},
#     {"Product ID":102,"Product":"Mouse","Price":3000,"Quantity":25,"Category":"Electronics"},
#     {"Product ID":103,"Product":"Keyboard","Price":2000,"Quantity":15,"Category":"Electronics"},
#     {"Product ID":104,"Product":"Monitor","Price":15000,"Quantity":5,"Category":"Electronics"},
#     {"Product ID":105,"Product":"Jacket","Price":1200,"Quantity":8,"Category":"Fashion"}
# ]
with open("data/products.json","r",encoding='utf-8' ) as file:
        product_details=json.load(file)
     

def view_products(product_details):
     print("\n========== PRODUCTS ==========")
    
     for product in product_details:
                print(
                    product["Product ID"],
                    "|",
                    product["Product"],
                    "|",(product["Price"]),
                    "|",
                    product["Category"]

            )

def search_product(product_details):
         try:
             search = input("\nEnter product name: ").lower()

         except ValueError:
                 print("the product name must be a string")
        
         found = False
        
         for product in product_details:
                    
        
                    if search in product["Product"].lower():
        
                        print(
                            product["Product ID"],
                            "|",
                            product["Product"],
                            "|",product["Price"],
                            "|",
                            product["Category"]
                        )
        
                        found = True
        
         if not found:
                raise ProductNotFoundError("product is not in the list")
def view_categories(product_details):
         print("\n========== CATEGORIES ==========")
        
         categories = []
        
         for product in product_details:
                    
        
                    if product["Category"] not in categories:
                        categories.append(product["Category"])
        
         for category in categories:
                    print("-", category)
        
        
                          