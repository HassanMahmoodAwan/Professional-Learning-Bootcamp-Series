# Dictionary { Mutable,    unordered,    All-DataTypes,   HashMaps,     Passed by Reference }

import copy
def dictionary():
    user:dict = {
        "userName": "Hassan Mahmood",
        "Age": 24,
        "Profession": "Software Engineer",
        "English Proficiency": "Intermediate"
    }
    print(user["Profession"])
    
    user["Habits"] = ["Book Reading", "Badminton", "Swiming", "GYM"]
    user["Profession"] = "Software Engineer (AI Engineer)"
    
    for keys in user:
        print(keys)
    
    for key, value in user.items():
        print(f"{key} : {value}")
        
    user.values()
    user.keys()
    
    user.get("Habits", "Not Found")
    user.get("NotExist")              # Return None.
    user.update({"email": "abl@gmail.com", "phone": "1234567890"})
    
    # user.pop("Habits")              # Arg Required.
    # user.popitem()                  # Last/Latest Item.
    # del user["Habits"]
    # user.clear()
    
    dictShallowCopy = user
    shallowCopy = user.copy()
    dictDeepCopy = copy.deepcopy(user)
    
    

if __name__ == "__main__":
    dictionary()