def daily_reminder():
    """
    Prompts the user for a single task, its priority, and time sensitivity,
    then provides a customized reminder.
    """
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    reminder_message = ""

    match priority:
        case 'high':
            reminder_message = f"Reminder: '{task}' is a high priority task"
        case 'medium':
            reminder_message = f"Note: '{task}' is a medium priority task"
        case 'low':
            reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            print("Invalid priority level. Please choose high, medium, or low.")
            return

    if time_bound == 'yes' and (priority == 'high' or priority == 'medium'):
        reminder_message += " that requires immediate attention today!"
    elif time_bound == 'yes' and priority == 'low':
        reminder_message += ". It's time-bound, so try to get to it today."
    elif time_bound == 'no' and (priority == 'high' or priority == 'medium'):
        reminder_message += ". You should aim to complete it today."


    print(reminder_message)

if __name__ == "__main__":
    daily_reminder()