import os

fileName:str = "users.txt"
print(os.getcwd()+ f"\{fileName}")
print(os.path.abspath(fileName))