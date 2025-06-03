def daily_reminder():
    """
    Prompts the user for a single task, its priority, and time sensitivity,
    then provides a customized reminder.
    """
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # We will build the suffix for the reminder message
    suffix_message = ""

    # Determine the suffix based on time_bound
    if time_bound == 'yes':
        suffix_message = " that requires immediate attention today!"
    elif time_bound == 'no':
        # For non-time-bound, we'll only add a specific suffix for high/medium
        # Low priority non-time-bound will be handled by its base message
        if priority == 'high' or priority == 'medium':
            suffix_message = ". You should aim to complete it today."

    # Use match-case to print the main reminder line directly
    match priority:
        case 'high':
            # This line directly contains "Reminder: " in its print statement
            print(f"Reminder: '{task}' is a high priority task{suffix_message}")
        case 'medium':
            print(f"Note: '{task}' is a medium priority task{suffix_message}")
        case 'low':
            # Special handling for low priority: default non-time-bound message
            # and a specific time-bound message
            if time_bound == 'yes':
                print(f"Note: '{task}' is a low priority task. It's time-bound, so try to get to it today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level. Please choose high, medium, or low.")
            return # Exit the function if priority is invalid

if __name__ == "__main__":
    daily_reminder()
