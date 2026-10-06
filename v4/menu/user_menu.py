from user.user import(signup,signin,change_password,view_profile)
from constants import(SIGN_UP,SIGN_IN,ECOMMERCE,VIEW_PROFILE,CHANGE_PASSWORD,LOGOUT,BACK)
from menu.ecommerce_menu import ecommerce_menu
def user_menu(current_user):
    while True:
        print("-------------------USER MENU----------------")
        if current_user is None:
          print("1. signup ")
          print("2. signin ")

        elif current_user is not None:
            print("3. Ecommerce Menu")
            print("4. View Profile ")
            print("5. Change Password ")
            print("6. Logout ")
        print("7. Back ")
        print("*****************************")

        choice=int(input("enter your choice: ").strip())

        if choice==SIGN_UP:
            signup()

        elif choice==SIGN_IN:
            logged_in_user=signin(current_user)
            if logged_in_user is not None:
                current_user=logged_in_user
        elif choice==ECOMMERCE and current_user is not None:
            ecommerce_menu(current_user)
        
        elif choice==VIEW_PROFILE and current_user is not None:
            view_profile(current_user)

        elif choice==CHANGE_PASSWORD and current_user is not None:
            current_user=change_password(current_user)

        elif choice==LOGOUT and current_user is not None:
            current_user=None
            print("logout successful")

        elif choice==BACK:
            return current_user

        else:
            print("invalid choice ")



            
    


