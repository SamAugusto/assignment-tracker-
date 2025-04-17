###Assigment Tracker CLI version
import threading
import time 
import schedule
from plyer import notification
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import simpledialog, messagebox
# Importing time is important because it allow us to put the function to sleep 
# and not constantly run in the background.
#Importing schedule from our installed package to help us with defining time and managing the reminders
# and plyer is mostly used to notify the desktop

# Variable to track if the reminder system is running
is_reminder_system_running = False

assignments= [] #List to store assignment details

#Lets define the function  that will send the reminder

def send_reminder(message):#function that sends the message for the reminders
    """
    
    Function to send a notification.
    """

    notification.notify(
        title='Reminder', #title for notification
        message=message, #the message that will appear in the notification
        timeout=8 #Duration for the notification on screen
        
        
        )
def add_assignment():#Allow us to set a due data and a name for an assigment and make them relate to each other
    """Function to add an assigment with a due date and time."""
    name = input("Enter the assigment name:")
    due_date_str = input("Enter the due date and time (MM-DD-YYYY HH:MM, 24-hour format): ")

    try:
        due_date = datetime.strptime(due_date_str, "%m-%d-%Y %H:%M")
    except ValueError:
        print("Invalid date format. Please try again")
        return
    assignments.append({"name": name, "due_date": due_date})
    print(f"Assigment '{name}' due on {due_date} added!")
    schedule_reminders(name, due_date)

def schedule_reminders(name, due_date):
    #Defines a lot costumization here we can have multiple assigments and schedules everything 
    #A bunch of loops and if statements to make sure every single command line works as it should
    """Schedule reminders for the assigment."""
    num_reminders = int(input("How many reminders would you like to set?"))
    for _ in range(num_reminders):
        reminder_type = input("What kind of reminders would you like? (hourly, daily,minutes )").lower()

        if reminder_type == "minutes":
            while True:
                try:
                    minutes_reminder = int(input("How many minutes before the due date do you want the reminder? "))
                    break  # Exit the loop once a valid input is provided
                except ValueError:
                    print("Invalid input. Please enter an integer value for minutes.")
            reminder_time = due_date - timedelta(minutes=minutes_reminder)
            # Debugging print lines
            print(f"Current time: {datetime.now()}")
            print(f"Reminder time: {reminder_time}")
            print(f"Time difference: {reminder_time - datetime.now()}")

            if reminder_time > datetime.now():
                # Schedule the reminder to run exactly at reminder_time (not in intervals)
                schedule.every().day.at(reminder_time.strftime('%H:%M')).do(send_reminder, f"The '{name}' is due in {minutes_reminder} minutes at {due_date.strftime('%H:%M')}!")
                print(f"Reminder set for {minutes_reminder} minutes before the due date at {reminder_time.strftime('%Y-%m-%d %H:%M')}")
                print(f"Reminder scheduled for {reminder_time.strftime('%Y-%m-%d %H:%M')}")  # Debug print
            else:
                print('Reminder time is in the past, cannot set reminder.')
        elif reminder_type == "daily":
            daily_reminder = int(input("How many days before the due date do you want the reminder? "))
            reminder_time = due_date - timedelta(days=daily_reminder)
            if reminder_time > datetime.now():
                schedule.every().day.at(reminder_time.strftime('%H:%M')).do(send_reminder, f"The '{name}' is due in {daily_reminder} days at {due_date.strftime('%H:%M')}!")
                print(f"Reminder set for {daily_reminder} days before the due date at {reminder_time.strftime('%Y-%m-%d %H:%M')}")
                print(f"Reminder scheduled for {reminder_time.strftime('%Y-%m-%d %H:%M')}")  # Debug print
            else:
                print('Reminder time is in the past, cannot set reminder.')
        elif reminder_type == "hourly":
            hour_reminder = int(input("How many hours before the due date do you want the reminder? "))
            reminder_time = due_date - timedelta(hours=hour_reminder)
            if reminder_time > datetime.now():
                schedule.every().day.at(reminder_time.strftime('%H:%M')).do(send_reminder, f"The '{name}' is due in {hour_reminder} hours at {due_date.strftime('%H:%M')}!")
                print(f"Reminder set for {hour_reminder} hours before the due date at {reminder_time.strftime('%Y-%m-%d %H:%M')}")
                print(f"Reminder scheduled for {reminder_time.strftime('%Y-%m-%d %H:%M')}")  # Debug print
            else:
                print('Reminder time is in the past, cannot set reminder.')
        else:
            print("Invalid format chosen please make sure you choose one of the formats above (daily, hourly or minutes)")                                                                                                                                    
def view_assigments():
    """Display all assigments."""
    if not assignments:
        print("No assigments have been added yet.")
    else:
        print("\nUpcoming Assignments:")
        for i, assignment in enumerate(assignments, start=1 ):
            print(f"{i}. {assignment['name']} - Due:{assignment['due_date'].strftime('%Y-%m-%d %H:%M')}")

def run_reminders():#Funciton will keep the program running and checking for scheduled tasks
    """

    Run the reminder schedule and keep the app running.
    """
    while True:# While true makes an infinite loop that will keep the script running  forever. That is necessary
               #Because we need the system to constantly check the schedule for scheduled tasks.
        schedule.run_pending() #Run the scheduled tasks
        time.sleep(1) #This makes the script wait for 1 second before checking the schedule again without it the script would continuously check the schedule
                      #it is not efficient to continuously check the schedule
#Starts the checking calendar system and tells it to run in the background so the user can still
#add and costumize in the main window
def start_reminder_system():
    """Start the reminder sytem if it is not already running."""
    global is_reminder_system_running
    if not is_reminder_system_running: #Check if the system is already running
        print("Starting the reminder system...")
        reminder_thread = threading.Thread(target=run_reminders,daemon = True)
        reminder_thread.start()
        is_reminder_system_running = True
        print("Reminder system is now running in the background.")
    else:
        print("Reminder system is already running")
         
##Main Execution Block
# if __name__ == '__main__':
#    print("Welcome to the Assigment Tracker!")
#    #Start menu
#    input("Press Enter to start the reminder system...")
#    start_reminder_system()
#    #Main Menu
#    while True:
#     print("\n Main Menu:")
#     print("1. Add an assignment")
#     print("2. View assignments")
#     print("3. Exit")

#     choice = input("Choose an option: ")
#     if choice == "1":
#         add_assignment()
#     elif choice == "2":
#         view_assigments()
#     elif choice == "3":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please select one of the numbers from the menu prompt.")


##GUI
#create the main window using Tkinter

root = tk.Tk()
root.title("Assigment Tracker")
root.geometry("1920x1080")
#Lauch the tracker

start_reminder_system()
#functions for each button assigned to actual functions of code
def show_add_assigment():
    add_assignment()
def show_view_assignment():
    view_assigments()
def exit_app():
    root.quit()

#assign each button the root means they know they are in the root window
#and assign each button a function to do when pressed
add_assignment_button = tk.Button(root, text="Add Assignment", command= show_add_assigment)
view_assigments_button = tk.Button(root,text = "View Assigments", command=show_view_assignment)
exit_button = tk.Button(root,text="Exit",command=exit_app)

#Designing the buttons
#buttons are packed vertically 10 pixels of space between them top and botton
add_assignment_button.pack(pady=10)
view_assigments_button.pack(pady=10)
exit_button.pack(pady=10)


root.mainloop()#Purpose:

#This starts the event loop, which is essential for handling GUI interactions.
#The event loop continuously listens for user actions (like button clicks) and updates the interface accordingly.
#How It Works:

#The program stays in this loop until the window is closed (or the root.quit() method is called).
#During this loop:
#Button clicks are detected and routed to the corresponding command functions.
#The interface remains responsive, and scheduled tasks (like reminders) can run in the background.#
