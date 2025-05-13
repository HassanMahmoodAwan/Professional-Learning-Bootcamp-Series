import os

print(os.name)                        # nt for windows, posix for mac/linux
print(os.path.exists("main.py"))

# Get working Directory
abs_path = os.getcwd()                      # Absolute Path.
print(os.path.join(abs_path, "main.py"))

print(os.path.abspath("main.py"))

if  os.path.exists("created.txt"):
    os.mkdir("created")
    
    
print(os.listdir())

os.rename("instructions.txt", "Instruction.txt")    #Source -> Destination

os.rmdir("created") 