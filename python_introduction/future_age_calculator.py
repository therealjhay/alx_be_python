# Prompt the user to input their current age
# The input() function reads a line from input, converts it to a string, and returns that.
# We use int() to convert the string input to an integer, as age is a whole number.
current_age = int(input("How old are you? "))

# Calculate how old the user will be in the year 2050.
# Assuming the current year is 2023, the difference to 2050 is 27 years (2050 - 2023).
future_age = current_age + 27

# Print the user's age in 2050 in the specified format.
# An f-string is used for easy formatting and embedding variables directly into the string.
print(f"In 2050, you will be {future_age} years old.")
