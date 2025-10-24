# AI Assistant Instructions for Python Experiments

## Project Overview
This repository contains basic Python experiments designed for learning and demonstration purposes. The current implementation includes a calculator application that operates on numbers between 0 and 1000.

## Core Components

### Calculator Implementation (`calculator_up_to_1000.py`)
- Input validation pattern: Uses while-true loops with try-except blocks for robust user input handling
- Number range constraints: All operations limited to numbers between 0-1000 (inclusive)
- Supported operations: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- Error handling patterns:
  - Value range validation (0-1000)
  - Input type validation (numeric inputs)
  - Division by zero protection
  - Generic exception catching with user-friendly messages

## Development Workflows

### Running the Applications
1. Open the desired Python file in VS Code
2. Use the built-in Python REPL:
   - Windows/Linux: `Ctrl + Shift + \``
   - Mac: `Cmd + Shift + \``
3. Save any changes with `Ctrl + S` (Windows/Linux) or `Cmd + S` (Mac)
4. Run the code in the REPL

### Project Structure Conventions
- Each experiment is contained in a single, self-contained Python file
- Files are named descriptively to indicate their purpose and limitations
- Interactive programs use command-line input/output for user interaction

## Error Handling Patterns
When implementing new features, follow these established patterns:
```python
while True:
    try:
        # User input with validation
        if validation_condition:
            break
        print("Error: Specific validation message")
    except ValueError:
        print("Error: Invalid input type message")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

## Testing Considerations
- Manual testing through interactive use
- Test edge cases around number range boundaries (0 and 1000)
- Test invalid inputs (non-numeric, out of range)
- Test division by zero scenarios