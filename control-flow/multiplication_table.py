def generate_multiplication_table():
    """
    Prompts the user for a number and prints its multiplication table from 1 to 10.
    """
    try:
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return

    print(f"Multiplication table for {number}:")
    for i in range(1, 11):  # Loop from 1 to 10 (11 is exclusive)
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    generate_multiplication_table()