print("Simple Calculator")

while True:
    print("\n------Menu------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. exit")

    choice = input("Choose an operation: ")

    if choice == "5":
        print("Thanks for using the simple calculator")
        break
    
    num1 = float(input("First Number: "))
    num2 = float(input("Second Number"))

    if choice == "1":
        result = num1 + num2
        print(f"{result}")
    elif choice == "2":
        result = num1 - num2
        print(f"{result}")
    elif choice == "3":
        result = num1 * num2
        print(f"{result}")
    elif choice == "4":
        result = num1 / num2
        if num2 == "0":
            print("You cant divude by 0!")
        else:
            print(f"{result}")
    else:
        print("Invalid choice - try again")      
