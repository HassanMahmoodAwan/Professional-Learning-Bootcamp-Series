class Employee:
    # Class Attributes.
    COMPANY="Allied bank Limited"
    
    @classmethod
    def company_details(cls):
        return cls.COMPANY
    
    # Special Method to Initialze Instance Attributes
    def __init__(self, name="Hassan", grade="MG-10"):
        # Instance Attributes.
        self.name = name
        self.grade = grade
        
    # Method
    def employee_info(self):
        return self.name, self.grade
    
        

if __name__ == "__main__":
    emp = Employee(name="Hassan Mahmood")    
    
    print(emp.name)
    
    name, grade = emp.employee_info()
    print(name, grade, sep="\n")
    
    print(Employee.company_details())
    emp.COMPANY = "Allied Bank Limited, Lahore."
    print(emp.company_details())

        