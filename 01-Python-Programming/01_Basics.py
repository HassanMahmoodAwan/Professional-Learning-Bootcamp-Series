"""
    Note: EveryThing in Python Variables, functions, etc are Objects. 
          Example:
                 <class Int>
"""
print("Hello World!", "Lets Learn Python", end="!\n", sep=", ")


import math, random
def variables() -> None:
    """ Store, Types, camelCase, DeepCopy """
    
    userName: str = input("Enter Name: \t")
    
    try:
        age: int = int(input("Enter Age: \t"))
    except ValueError:
        print("Age should be Numeric")
        variables()
        return
    
    flag:bool = True
    weight:float = 85.4
    undefined:None = None
    
    one = two = three = 40
    # one, two, three = 10
    one, two, three = 10, 20, 30
    tple = 1, 2, 3
    
    print(math.pi, type(math.pi), sep=(",  "))
    
    round(random.random(), 2)
    random.randint(10, 20)
    random.choice([10, 20, 30])




def operators() -> None:
    """ Arithmatic, Relational, Logical, Comparison, Mapping """
    
    # Arithmatic (**, /, // , *, +, -, %)  Left -> Right  BEDMAS
    mathEq: int | float = (10 / 10 ** 20) * 4 + 2 - 4
    print(mathEq)
    
    # Logical Operators (and, not, or)
    flag: bool = not(10 == 20 and 20 != 40 or "apple" != "Apple")
    print(flag)
    
    # Comparision Operators
    compare: bool = 10 == 20 and 50 != 60
    print(compare)
    
    # Relational Operators (> < >= <=)
    condition: bool = 10 > 20 and 13 <= 30
    print(condition)
    
    # Bitwise Operators (>>, <<)
    
    # Mapping Operators
    check: bool = "Has" in "Hassan"
    print(check)
    


def conditionalStatements() -> None:
    """ if-elif-else  ,  match-case-default , Ternary Operator (if-else Shorthand) """
    marks: int = 80
    percentage = 80 / 100 * 100
    
    if percentage >= 80:
         "Good"
    elif percentage < 80 and percentage >= 70:
        "satisfy"
    else:
        "Need Improvment"
        
    print("Good") if percentage >= 80 else print("Work Hard")
 



if __name__ == "__main__":
    variables()
    # operators()
    # conditionalStatements()