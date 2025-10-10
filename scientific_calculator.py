import math

def menu():
    print("1. Square root")
    print("2. Factorial")
    print("3. Natural log")
    print("4. Power")
    print("5. Exit")
    while True:
        choice = input("Choose: ")
        if choice == "1":
            x = float(input("Enter number: "))
            print("Result:", math.sqrt(x))
        elif choice == "2":
            x = int(input("Enter integer: "))
            print("Result:", math.factorial(x))
        elif choice == "3":
            x = float(input("Enter number: "))
            print("Result:", math.log(x))
        elif choice == "4":
            x = float(input("Enter base: "))
            y = float(input("Enter exponent: "))
            print("Result:", math.pow(x, y))
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
