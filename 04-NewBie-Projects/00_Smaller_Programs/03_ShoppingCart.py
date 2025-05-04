# Creating Resturant Basic Shopping Cart

menu: dict = {
    "pizza": 8.0,
    "burger": 4.0,
    "sandwich": 6,
    "coffee": 2.99,
    "tea": 1.05
}
cart:list = []
total:float = 0

print("\n**************** MENU **************** ", end="\n")

for item in menu:
    print(f"{item:10}: {menu.get(item):.2f}$")
    
print("-------------------------------------- ", end="\n\n")


while True:
    choice = input("Enter what you want to buy from menu, q for quit:\t").lower()
    
    if choice == 'q':
        break
    
    itemprice = menu.get(choice, "")
    if itemprice:
        cart.append(choice)
        total += itemprice
print()        

print(f"{cart}"[1:-1])
print(f"Total is: {total}")
    
    

