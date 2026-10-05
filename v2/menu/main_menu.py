from v1.constants import(USER_MENU,ECOMMERCE_MENU,EXIT_MAIN)
from v1.menu.user_menu import user_menu
from v1.menu.ecommerce_menu import ecommerce_menu
def main_menu():
    current_user=None
    print("*"*30)
    print("Welcome in ecommerce app")
    print("*"*30)
    
    while True:
         print("-----Main Menu-----")
         print("1. User Menu ")
         print("2. Ecommerce Menu ")
         print("3. Exit the application ")
         try:
          choice=int(input("enter your choice: ").strip())
         
         except ValueError:
             print("enter integer value")
         if choice==USER_MENU:
              current_user=user_menu(current_user)

         elif choice==ECOMMERCE_MENU:
              if current_user is not None:
                   ecommerce_menu(current_user)
              else:
                   print("please sign in first")

         elif choice==EXIT_MAIN:
              print("------------------------------------")
              print("thank you for visiting the store")
              print("please visit again")
              break

         else:
              print("invalid choice")
            
              
              

        
