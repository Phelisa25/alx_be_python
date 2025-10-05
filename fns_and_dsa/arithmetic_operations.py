def perform_operation(num1, num2, operation):
    
    """Performs a basic arithmetic operation on two numbers."""

    Parameters:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. 
                         Options: 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: The result of the operation, or an error message for invalid inputs.
    if operation == 'add':
        return num1 + num2  
        elif operation == 'subtract':
        return num1 - num2
        elif operation == 'multiply':   
        return num1 * num2
        elif operation == 'divide': 
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: invalid operation."
    else:
        return "Error: invalid operation."
    """
    if operation == 'add':
        return num1 + num2  
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':   
        return num1 * num2
    elif operation == 'divide': 
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Error: invalid operation."