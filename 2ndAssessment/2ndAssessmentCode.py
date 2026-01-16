# displaying the products
print("Welcome to Darick's vending machine\n")
print("Product       Price  Code  Stock")
print("Oman Chips    2aed   1111    1  ")
print("Coke          3aed   2222    1  ")
print("Snickers      5aed   3333    1  ")
print("Aqua Water    1aed   4444    1  ")

# create variables for the products

OmanPrice = 2
CokePrice = 3
SnickersPrice = 5
AquaPrice = 1

OmanStock = 1
CokeStock = 1
SnickersStock = 1
AquaStock = 1

# insert money command and stock availability command

def purchase_item(item, price, stock):
    if stock > 0:
        print(f"You chose {item}. Please insert {price}aed.")
        money_inserted = float(input())
        if money_inserted >= price:
            stock -= 1
            print(f"Here is your {item}. Enjoy!\n")
            if money_inserted > price:
                print(f"Here is your change: {money_inserted - price}aed\n")
        else:
            print("Insufficient money. Please try again.")
    else:
        print(f"Sorry, {item} is out of stock.")
    return stock

# Ask the user to enter the code for the product
while True:
    print("\nplease enter a code for an item")
    userCode = int(input())

    
    if userCode == 1111:
        OmanStock = purchase_item("Oman Chips", OmanPrice, OmanStock)
    
    elif userCode == 2222:
        CokeStock = purchase_item("Coke", CokePrice, CokeStock)

    elif userCode == 3333:
        SnickersStock = purchase_item("Snickers", SnickersPrice, SnickersStock)

    elif userCode == 4444:
        AquaStock = purchase_item("Aqua Water", AquaPrice, AquaStock)
    
    else:
        print("Invalid code. Please try again.")
        continue

    while True:
        TryAgain = input("Would you like to buy another item (yes/no): ").strip().lower() # helps to prevent the computer from being confused by turning all yes/no to lowercase

        if TryAgain == "yes":
            # break inner loop, go back to outer loop to buy another item
            break
        elif TryAgain == "no":
            print("Thank you for using Darick's vending machine! Goodbye!")
            exit() # stops program completely
        else:
            print("Please type 'yes' or 'no'.")