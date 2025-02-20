class Employee:
    COMPANY="Allied bank Limited"
    WEBSITE="www.abl.com.pk"
    
    # Special Method to Initialze Instance Attributes
    def __init__(self, name="Hassan", grade="MG-10"):
        # Instance Attributes.
        self.name = name
        self.grade = grade
        

if __name__ == "__main__":
    emp = Employee(name="Hassan Mahmood")    
    print(emp_obj.name)
        