import time
import os
import json


usersDatabase = "users.txt"
usersDatabasePath = os.path.abspath(usersDatabase)

def save_data_in_file(filePath:str, content):
    with open(filePath, 'w') as file:
        file.write(json.dumps(content))
        file.close()
    
    time.sleep(4)
    return {"status":200}


def load_data_from_file(filePath:str):
    with open(filePath, 'r') as file:
        data = file.read()
        return json.loads(data)
        


def user_registeration():
    filePath = usersDatabasePath
    username:str
    email:str
    password:str
    
    print("\nTo Register User Provide Following Details: ")
    while True:
            username = input("Enter username:\t")
            if username.isdigit() or len(username) < 4 or len(username) > 16:
                print("\n* Enter Valid Username *\n")
                continue
            break
    
    while True:
            email = input("Enter a valid email:\t")
            if email.isdigit() or len(email) < 10 or len(email) > 50 or email.find('@') == -1:
                print("\n* Enter Valid email *\n")
                continue
            break
        
    while True:
            password = input("Enter your password*:\t")
            if password.isdigit() or password.isalpha() or len(password) < 8 or len(password) > 12:
                print("\n* Enter Valid Password *\n")
                continue
            break    
    
    data = load_data_from_file(filePath)
    print(data)
    if data == None:
        content = [{"username":username, "email":email, "password":password}]
        save_data_in_file(filePath, content)
        return {"status": True, "msg": "User Registered Successfully"}
    
    
    if username not in data:
        content = data.append({"username":username, "email":email, "password":password})
        print(content)
        save_data_in_file(filePath, content)
        return {"status": True, "msg": "User Registered Successfully"}
    else:
        return {"status": False, "msg": "Username Already exist, Change userName"}



def user_login_authentication(username:str, password:str) -> dict[ str, str|bool ]:
    data = load_data_from_file(usersDatabasePath)
    print(data)
    
    if data ==  None:
        return {"username":"", "isAuthenticated":False, "isUserExist":False, "status": "User Doesnot Exist, Login Failed"}
        
    
    for user in data:
        if user["username"] == username:
            if user["password"] == password:
                return {"username":username, "isAuthenticated":True, "isUserExist":True, "status": "User Exist, Login Successful"}
            else:
                return {"username":username, "isAuthenticated":False, "isUserExist":True, "status": "User Exist, Login Failed, Password Inccorect."}
    return {"username":username, "isAuthenticated":False, "isUserExist":False, "status": "User Doesnot Exist, Login Failed"}
        
    
    


def main(tries:int = 1) -> None:
    
    signInChoice:int
    
    print("***************** Welcome to your Youtube Video Management App. ********************", end="\n\n")
    try:
        signInChoice = int(input("Enter 1 to Login or 2 for SignUp:\t"))
    except Exception as e:
        print(f"Invalid Choice Given: {e}")
        
    if signInChoice == 1:
        authenticationTries:int = tries
        print("===== Login into your Application =====")
        while authenticationTries > 0:
            while True:
                username = input("Enter your username*:\t")
                if len(username) < 4:
                    print("\n* Enter Valid username *\n")
                    continue
                break
            
            while True:
                password = input("Enter your password*:\t")
                if password.isdigit() or password.isalpha() or len(password) < 8 or len(password) > 12:
                    print("\n* Enter Valid Password *\n")
                    continue
                break
            
            authenticationTries -= 1
            userLoginStatus = user_login_authentication(username, password)
            print(userLoginStatus["status"])

            if userLoginStatus["isAuthenticated"]:
                print(f"{userLoginStatus["username"]} is successfully Login")
                break
            elif userLoginStatus["isUserExist"]:
                print(f"{userLoginStatus["username"]} is Correct, Password Provided is Incorrect.")
                continue    
            else:
                print(f"{userLoginStatus["username"]} User Doesnot Exist, Register the User or Login Again.")
                continue

        else:
            print("Number of Tries to Login Failed, Register User or Close App.")
            try:
                choice = int(input("To create new User Enter 1 else to Close app enter 2: "))
            except Exception as e:
                print(f"Invalid Input Provided Closing the App, {e} ")
                return

            if choice == 1:
                status = user_registeration()
                print(status)
    
    
    elif signInChoice == 2:
        status = user_registeration()
        print(status)
        
    else:
        print("Invalid Choice Given ")
        return
        


if __name__ == "__main__":
    main(tries = 2)