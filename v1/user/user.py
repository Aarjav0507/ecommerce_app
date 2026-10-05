from v1.data.users import users
def signup():
    name=input("Enter full name: ").lower()
    email=input("enter your email: ").strip().lower()
    phone=input("enter your phone number: ")
    password=input("enter your password: ")
    id="U"+str(len(users)+1)

    if not name or not email or not phone or not password:
        print("All fields are required")
        return

    if "@" not in email:
        print("enter a valid email address")
        return

    if len(password)<6:
        print("the password must contain atleast 6 characters")

    for user in users:
        if user["email"]==email:
            print("email already registered")
            return

    user={
        "user_id":id,
        "full_name":name,
        "email":email,
        "phone":phone,
        "password":password,
        "role":"customer",
        "status":"active"
    }
    users.append(user)

    print("registration successful")

def signin():
    print("------------Login------------")

    email=input("enter email:").strip().lower()
    password=input("enter password:").strip()

    for user in users:
        if user["email"]!=email:
            continue

        if user["status"]!="active":
            print("user is inactive")
            return None
        print("check")
        if user["password"]==password:
            print("login successful")

            return user
        print("invalid password")
        return None
    print("user not found")

def view_profile(current_user):
    print("------------User Details-----------")
    print("full name:",current_user["full_name"])
    print("email:",current_user["email"])
    print("phone number:",current_user["phone"])
    

def change_password(current_user):
    password=input("enter your existing password: ")
    if current_user["password"]==password:
        new_password=input("enter new password ")
        current_user["password"]=new_password
        print("password changed successfully")
        return current_user

        

    

    
        
        




    


    
