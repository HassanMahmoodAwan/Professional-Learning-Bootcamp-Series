import time
import os
import json


def save_content_in_file(filePath:str, content):
    with open(filePath, 'w') as file:
        file.write(json.dumps(content))
        file.close()
    
    time.sleep(4)
    return {"status":200}

def user_login_authentication(username:str, password:str) -> dict[ str, str|bool ]:
    fileName:str = "users.txt"
    filePath:str = os.path.abspath(fileName)
    content = [{"username":username, "password":password}]
    
    save_content_in_file(filePath, content)
    
    return {"username":username, "isAuthenticated":True, "isUserExist":True, "status": "User Exist, Login Successful"}


def main(tries:int = 1) -> None:
    authenticationTries:int = tries
    
    print("***************** Welcome to your Youtube Video Management App. ********************", end="\n\n")
    
    print("===== Login into your Application =====")
    while authenticationTries > 0:
        
        username = input("Enter your Username*:\t")
        if len(username) < 4:
            print("\n* Enter Valid Username *\n")
            continue
        password = input("Enter your password*:\t")
        if password.isdigit() or password.isalpha() or len(password) < 8 or len(password) > 12:
            print("\n* Enter Valid Password *\n")
            continue
        
        authenticationTries -= 1
        userLoginStatus = user_login_authentication(username, password)
        
        if userLoginStatus["isAuthenticated"]:
            print(f"{userLoginStatus["username"]} is successfully Login")
            break
        elif userLoginStatus["isUserExist"]:
            print(f"{userLoginStatus["username"]} is Correct, Password Provided is Incorrect.")
            continue
        else:
            print(f"{userLoginStatus["username"]} Doesnot Exist, Register the User or Login Again.")
            continue
            
    else:
        print("Number of Tries to Login Failed, Closing the Application.")
        return
        


if __name__ == "__main__":
    main(tries = 5)