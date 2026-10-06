from db.user_queries import create_user,find_user_by_email,update_password
from decorators import logging,execution_time



@execution_time
def signup():
    name=input("Enter full name: ").lower()
    email=input("enter your email: ").strip().lower()
    phone=input("enter your phone number: ")
    password=input("enter your password: ")
    

    if not name or not email or not phone or not password:
        print("All fields are required")
        return

    if "@" not in email:
        print("enter a valid email address")
        return

    if len(password)<6:
        print("the password must contain atleast 6 characters")

    else:
        create_user(name,email,phone,password)
    
    

        print("registration successful")



@execution_time
def signin(email):
    print("------------Login------------")

    email=input("enter email:").strip().lower()
    password=input("enter password:").strip()
    user=find_user_by_email(email)
    if user is None:
        print("user not found")
        return None
    if user[4]==password:
        print("login successful")
        return user
    print("inavlaid password")
    return None


@logging
@execution_time
def view_profile(current_user):
    print("------------User Details-----------")
    print("full name:",current_user[1])
    print("email:",current_user[2])
    print("phone number:",current_user[3])
    

@logging
@execution_time
def change_password(current_user):

    password = input("Enter your existing password: ")

    if current_user[4] != password:
        print("Incorrect existing password")
        return current_user

    new_password = input("Enter new password: ")

    if len(new_password) < 6:
        print("Password must contain at least 6 characters")
        return current_user

    result = update_password(
        current_user[0],
        new_password
    )

    if result:
        print("Password changed successfully")

        # Keep current_user updated
        current_user = (
            current_user[0],
            current_user[1],
            current_user[2],
            current_user[3],
            new_password,
            current_user[5]
        )

    return current_user
        

    

    
        
        




    


    
