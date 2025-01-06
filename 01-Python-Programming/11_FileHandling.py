import os

"""
Note: IF file not Exist, cannot Read().
"""

try:
    data = open("instructions.txt", "r")
    print(data.read())
except FileNotFoundError:
    print("At start, File doesnot Exsis Error.")
    
   
if not os.path.exists("instructions.txt"):
    with open("instructions.txt", "w") as f:
        data = f.write("Hello world, Lets learn Python Programming")       
        f.close()
else:
    with open("instructions.txt", "a") as f:
        f.write("\n")
        data = f.write("A part of my professional Software Engineering Journey.")       
        f.close()
    

os.rename("instructions.txt", "Instruction.txt")