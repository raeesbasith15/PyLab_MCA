x = int(input("Enter the first number: "))
y = int(input("Enter the second number: ")) 

while True:
    print("Select an operation:")
    print("+ for Addition")
    print("- for Subtraction")
    print("* for Multiplication")
    print("/ for Division")    
    print("'%' for Modulus")
    print("** for Exponentiation")

    print("Type 'quit' to exit the program.")

    op = input("Enter the option: ") 
    match op: 
        case '+':
            result = x + y
            print(f"The result of addition is: {result}")
        case '-':
            result = x - y
            print(f"The result of subtraction is: {result}")
        case '*':
            result = x * y
            print(f"The result of multiplication is: {result}")
        case '/':
            if y != 0:
                result = x / y
                print(f"The result of division is: {result}")
            else:
                print("Error: Division by zero is not allowed.")
        case '%':
            if y != 0:
                result = x % y
                print(f"The result of modulus is: {result}")
            else:
                print("Error: Modulus by zero is not allowed.")
        case '**':
            result = x ** y
            print(f"The result of exponentiation is: {result}")
        case 'quit':
            print("Exiting the program.")
            break
        case _:
            print("Invalid operation selected.")