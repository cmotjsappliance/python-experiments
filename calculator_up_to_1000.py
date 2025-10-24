def calculator():
    """
    A simple calculator that performs addition, subtraction, multiplication, and division
    on numbers between 0 and 1000.
    """
    print("Welcome to the Python Calculator!")
    print("You can perform addition, subtraction, multiplication, and division.")
    print("Numbers should be between 0 and 1000 (inclusive).")

    while True:
        try:
            num1 = float(input("Enter the first number (0-1000): "))
            if 0 <= num1 <= 1000:
                break
            print("Error: First number must be between 0 and 1000.")
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    while True:
        try:
            operator = input("Enter an operator (+, -, *, /): ")
            if operator in ['+', '-', '*', '/']:
                break
            print("Error: Invalid operator. Please use +, -, *, or /.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    while True:
        try:
            num2 = float(input("Enter the second number (0-1000): "))
            if 0 <= num2 <= 1000:
                break
            print("Error: Second number must be between 0 and 1000.")
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2

    print(f"Result: {num1} {operator} {num2} = {result}")

    while True:
        try:
            another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if another_calculation in ['yes', 'no']:
                break
            print("Error: Invalid input. Please enter yes or no.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    if another_calculation == 'no':
        print("Thank you for using the calculator!")

if __name__ == "__main__":
    calculator()

