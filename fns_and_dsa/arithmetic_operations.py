def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation.

    Parameters:
    - num1 (float): First number
    - num2 (float): Second number
    - operation (str): 'add', 'subtract', 'multiply', or 'divide'

    Returns:
    - float result if operation is valid
    - str message if dividing by zero or invalid operation
    """

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1 / num2

    else:
        return "Error: Invalid operation"
