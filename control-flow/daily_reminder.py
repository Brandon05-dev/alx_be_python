# File: daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use Match Case for priority levels
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unspecified priority"

# Add time-sensitivity message if applicable
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority == "low" or priority == "medium" or priority == "high":
        reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print(reminder)
