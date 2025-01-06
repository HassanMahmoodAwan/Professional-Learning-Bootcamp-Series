# Dictionary { Mutable,    unordered,    All-DataTypes,   HashMaps }

import copy
def dictionary():
    user:dict = {
        "userName": "Hassan Mahmood",
        "Age": 23,
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
    
    # user.pop("Habits")              # Arg Required.
    # del user["Habits"]
    # user.clear()
    
    dictShallowCopy = user
    shallowCopy = user.copy()
    dictDeepCopy = copy.deepcopy(user)
    
    

if __name__ == "__main__":
    dictionary()