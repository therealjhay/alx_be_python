# Define the variable 'hours' and assign it a value of 2.
hours = 2

# Calculate the number of seconds in the given hours.
# There are 60 minutes in an hour and 60 seconds in a minute,
# so 1 hour = 60 * 60 = 3600 seconds.
seconds = hours * 3600

# Print the result in the specified format.
# Using an f-string to easily embed the 'hours' and 'seconds' variables.
print(f"{hours} hour(s) is {seconds} seconds.")
