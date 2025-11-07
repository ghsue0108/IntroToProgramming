correct_password = "12345"

user = input("Enter password: ")

while user != correct_password:
    print("Hint: Count 1-5")
    user = input("Enter password: ")

print("Access granted!")
