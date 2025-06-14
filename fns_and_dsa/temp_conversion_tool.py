# Define Global Conversion Factors
# Factor to convert Fahrenheit to Celsius: (F - 32) * 5/9
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
# Factor to convert Celsius to Fahrenheit: (C * 9/5) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction for temperature conversion.
    Prompts the user for temperature and unit, then performs and displays the conversion.
    """
    while True:
        try:
            # Prompt the user to enter a temperature
            temp_input = input("Enter the temperature to convert: ")
            temperature = float(temp_input) # Convert input to a float

            # Prompt the user to specify the unit
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is {converted_temp}°F")
                break # Exit loop if conversion is successful
            elif unit == 'F':
                converted_temp = convert_to_celsius(temperature)
                print(f"{temperature}°F is {converted_temp}°C")
                break # Exit loop if conversion is successful
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError:
            # Handle non-numeric input for temperature
            print("Invalid temperature. Please enter a numeric value.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main() # Run the main function when the script is executed
