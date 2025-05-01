"""
    Note: EveryThing in Python Variables, functions, etc are Objects. 
          Example:
                 <class Int>
"""
print("Hello World!", "Lets Learn Python", f"Date: 2-May-25 & {1.22:.1f}", end="!\n", sep=", ")


import math, random, time

def basic_concepts() -> None:
    """ Variable: Store, Types, camelCase, DeepCopy """
    
    userName: str = input("Enter Name: \t")
    
    try:
        age: int = int(input("Enter Age: \t"))
    except ValueError:
        print("Age should be Numeric")
        basic_concepts()
        return
    
    flag:bool = True
    weight:float = 85.4
    undefined:None = None
    
    one = two = three = 40
    # one, two, three = 10
    one, two, three = 10, 20, 30
    tple = 1, 2, 3
    
    abs(-20)
    pow(20, 2)
    round(0.8787, 1)        # -> 0.9
    max(20, 30, 40)
    min(20, 30, 40)
    
    print(math.pi, type(math.pi), sep=(",  "))
    math.e
    math.sqrt(10)
    math.ceil(9.1)
    math.floor(9.9)
    
    round(random.random(), 2)
    random.randint(10, 20)
    random.choice([10, 20, 30])

    time.sleep(2)   # Sync 2 secs delay.
    
    help(random)    # explain all methods and attributes.
    dir(random)     # List all methods and attributes.



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
    


def conditional_statements() -> None:
    """ if-elif-else  ,  match-case-default , Ternary Operator (if-else Shorthand) """
    marks: int = 80
    percentage = 80 / 100 * 100
    
    if percentage >= 80:
         "Good"
    elif 65 >= percentage < 80:
        "satisfy"
    else:
        "Need Improvment"
        
    print("Good") if percentage >= 80 else print("Work Hard")
 



if __name__ == "__main__":
    basic_concepts()
    # operators()
    # conditional_statements()