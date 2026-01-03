# Calculator Documentation

## Overview

The Calculator application (`calculator_up_to_1000.py`) is a command-line calculator that performs basic arithmetic operations on numbers within the range of 0 to 1000.

## Features

- **Addition (+)**: Add two numbers
- **Subtraction (-)**: Subtract one number from another
- **Multiplication (*)**: Multiply two numbers
- **Division (/)**: Divide one number by another

## Number Constraints

- All input numbers must be between 0 and 1000 (inclusive)
- The calculator will reject any numbers outside this range
- Division by zero is not allowed and will display an error message

## How to Use

1. **Start the Calculator**
   ```bash
   python calculator_up_to_1000.py
   ```

2. **Enter Your First Number**
   - You'll be prompted: "Enter the first number (0-1000):"
   - Type a number between 0 and 1000 and press Enter

3. **Choose an Operator**
   - You'll be prompted: "Enter an operator (+, -, *, /):"
   - Type one of the four operators and press Enter

4. **Enter Your Second Number**
   - You'll be prompted: "Enter the second number (0-1000):"
   - Type a number between 0 and 1000 and press Enter

5. **View the Result**
   - The calculator will display the result of your calculation

6. **Continue or Exit**
   - You'll be asked: "Do you want to perform another calculation? (yes/no):"
   - Type "yes" to perform another calculation or "no" to exit

## Example Usage

```
Welcome to the Python Calculator!
You can perform addition, subtraction, multiplication, and division.
Numbers should be between 0 and 1000 (inclusive).

Enter the first number (0-1000): 500
Enter an operator (+, -, *, /): +
Enter the second number (0-1000): 250
Result: 500.0 + 250.0 = 750.0

Do you want to perform another calculation? (yes/no): no
Thank you for using the calculator!
```

## Error Handling

The calculator includes robust error handling for:

- **Invalid Input Types**: Non-numeric inputs are rejected with an error message
- **Out of Range Numbers**: Numbers less than 0 or greater than 1000 are rejected
- **Invalid Operators**: Only +, -, *, / are accepted
- **Division by Zero**: Attempting to divide by zero displays an error message
- **Unexpected Errors**: Generic exception handling for any other errors

## Code Structure

The calculator follows these design patterns:

- **Input Validation Pattern**: Uses while-true loops with try-except blocks
- **Range Checking**: Validates all numbers are within 0-1000 range
- **User-Friendly Messages**: Clear error messages for all validation failures
- **Modular Design**: Self-contained function that can be called multiple times

## Learning Objectives

This calculator demonstrates:
- User input handling in Python
- Exception handling with try-except blocks
- Input validation and range checking
- Basic arithmetic operations
- While loops for repeated operations
- Conditional logic with if-elif-else
- String formatting for output
