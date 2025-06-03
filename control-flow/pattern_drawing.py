def draw_square_pattern():
    """
    Prompts the user for a positive integer and draws a square pattern of asterisks (*)
    of that size using a while loop for rows and a for loop for columns.
    """
    while True:
        try:
            size = int(input("Enter the size of the pattern: "))
            if size <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    row_count = 0
    while row_count < size:
        for _ in range(size):
            print("*", end="")
        print()  # Move to the next line after printing a row
        row_count += 1

if __name__ == "__main__":
    draw_square_pattern()