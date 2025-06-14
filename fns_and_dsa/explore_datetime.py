from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains the current date and time, formats it, and prints it to the console.
    """
    # Get the current date and time
    current_date = datetime.now()

    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_current_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_current_datetime}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date by adding
    these days to the current date, and prints the future date.
    """
    while True:
        try:
            # Prompt the user to enter a number of days
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            if days_to_add < 0:
                print("Please enter a non-negative number of days.")
                continue
            break # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    # Get the current date (without time for future date calculation context)
    current_date_only = datetime.now().date()

    # Calculate the future date by adding the specified number of days
    future_date = current_date_only + timedelta(days=days_to_add)

    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate a future date based on user input
    calculate_future_date()
