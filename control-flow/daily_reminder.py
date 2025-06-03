def daily_reminder():
    """
    Prompts the user for a single task, its priority, and time sensitivity,
    then provides a customized reminder.
    """
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder_message = ""

    # Use match-case to set the base reminder message based on priority
    match priority:
        case 'high':
            reminder_message = f"Reminder: '{task}' is a high priority task"
        case 'medium':
            reminder_message = f"Note: '{task}' is a medium priority task"
        case 'low':
            reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            print("Invalid priority level. Please choose high, medium, or low.")
            return # Exit the function if priority is invalid

    # Use if-elif to modify the message based on time sensitivity
    if time_bound == 'yes' and (priority == 'high' or priority == 'medium'):
        reminder_message += " that requires immediate attention today!"
    elif time_bound == 'yes' and priority == 'low':
        reminder_message += ". It's time-bound, so try to get to it today."
    elif time_bound == 'no' and (priority == 'high' or priority == 'medium'):
        reminder_message += ". You should aim to complete it today."
    # No else needed if time_bound is 'no' and priority is 'low',
    # as the base message for 'low' is already comprehensive.

    # Print the final constructed reminder message
    print(reminder_message)

if __name__ == "__main__":
    daily_reminder()
