def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations based on the given numbers and operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The arithmetic operation to perform.
                         Accepted values are 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: The result of the operation, or an error message if division by zero occurs
                      or an invalid operation is provided.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Handle division by zero
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        # Handle unsupported operations
        return "Error: Invalid operation. Please choose 'add', 'subtract', 'multiply', or 'divide'."
