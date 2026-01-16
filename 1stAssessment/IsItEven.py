def check_even_odd(num):
    if num % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

def main():
    value = int(input("Enter a number: "))
    result = check_even_odd(value)
    print(result)

if __name__ == "__main__":
    main()
