import math

while True:

    print("\n===== CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")
    print("========================")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        print("Result =", round(a + b, 3))

    elif choice == 2:

        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        print("Result =", round(a - b, 3))

    elif choice == 3:

        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        print("Result =", round(a * b, 3))

    elif choice == 4:

        a = float(input("Enter First Number: "))
        b = float(input("Enter Second Number: "))

        if b == 0:
            print("Error! Cannot divide by zero.")
        else:
            print("Result =", round(a / b, 3))

    elif choice == 5:

        a = float(input("Enter Base Number: "))
        b = float(input("Enter Power: "))

        print("Result =", round(a ** b, 3))

    elif choice == 6:

        a = float(input("Enter Number: "))

        if a < 0:
            print("Error! Square root of a negative number is not possible.")
        else:
            print("Result =", round(math.sqrt(a), 3))

    elif choice == 7:

        print("Thank you for using Calculator!")
        break

    else:

        print("Please enter a valid option (1-7).")
