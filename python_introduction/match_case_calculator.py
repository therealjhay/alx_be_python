def match_case_calculator():
    """
    This calculator prompts the user to enter two numbers and select an operation.
    It then performs the selected operation using a Match Case statement and displays the result.
    Handles division by zero gracefully.
    """
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    operation = input("Choose the operation (+, -, *, /): ")

    result = None
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            else:
                result = num1 / num2
        case _:
            print("Invalid operation. Please choose from +, -, *, or /.")
            return

    if result is not None:
        print(f"The result is {result}.")

if __name__ == "__main__":
    match_case_calculator()