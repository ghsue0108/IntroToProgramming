name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")
age = int(input("Enter your age (numbers only): "))

bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

print(bio["name"], bio["hometown"], bio["age"], sep="\n")
