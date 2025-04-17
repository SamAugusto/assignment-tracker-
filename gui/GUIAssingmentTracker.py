import tkinter as tk
from tkinter import messagebox
import threading
import schedule
from plyer import notification
from datetime import datetime, timedelta
import time

# Variable to track if the reminder system is running
is_reminder_system_running = False

assignments = []  # List to store assignment details

# Reminder notification function
def send_reminder(message):
    notification.notify(
        title='Reminder',
        message=message,
        timeout=8
    )

# Start the reminder system
def start_reminder_system():
    global is_reminder_system_running
    if not is_reminder_system_running:
        def run_reminders():
            while True:
                schedule.run_pending()
                time.sleep(1)

        reminder_thread = threading.Thread(target=run_reminders, daemon=True)
        reminder_thread.start()
        is_reminder_system_running = True
        print("Reminder system started in the background.")

# Function to add an assignment
def add_assignment_gui(name, due_date_str, reminders, root):
    try:
        due_date = datetime.strptime(due_date_str, "%m-%d-%Y %H:%M")
        assignments.append({"name": name, "due_date": due_date, "reminders": reminders})
        messagebox.showinfo("Success", f"Assignment '{name}' due on {due_date} added!")
        schedule_reminders(name, due_date, reminders)
        root.destroy()  # Close the add assignment window
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use MM-DD-YYYY HH:MM.")

# Function to schedule reminders
def schedule_reminders(name, due_date, reminders):
    for reminder in reminders:
        time_type = reminder['type']
        time_value = reminder['value']

        if time_type == 'minutes':
            reminder_time = due_date - timedelta(minutes=time_value)
        elif time_type == 'hours':
            reminder_time = due_date - timedelta(hours=time_value)
        elif time_type == 'days':
            reminder_time = due_date - timedelta(days=time_value)
        else:
            print(f"Unknown reminder type: {time_type}")
            continue

        if reminder_time > datetime.now():
            schedule.every().day.at(reminder_time.strftime('%H:%M')).do(
                send_reminder, f"The assignment '{name}' is due soon!"
            )
            print(f"Reminder set for {name} at {reminder_time}.")
        else:
            print("Cannot set a reminder in the past.")

# Function to view assignments in a new window
def view_assignments_gui():
    view_window = tk.Toplevel(root)
    view_window.title("View Assignments")
    view_window.geometry("400x300")

    # Set the background color of the view assignments window to match the theme
    view_window.config(bg="lightblue")

    # Label indicating if there are assignments or not
    if not assignments:
        tk.Label(view_window, text="No assignments added yet.", font=("Impact", 14), bg="lightblue", fg="white").pack(pady=20)
    else:
        tk.Label(view_window, text="Upcoming Assignments:", font=("Impact", 14), bg="lightblue", fg="white").pack(pady=10)

        # Loop through each assignment and display it
        for i, assignment in enumerate(assignments, start=1):
            reminders = assignment["reminders"]
            reminders_text = ", ".join(
                [f"{reminder['value']} {reminder['type']}" for reminder in reminders]
            )
            tk.Label(view_window, text=f"{i}. {assignment['name']} - Due: {assignment['due_date'].strftime('%Y-%m-%d %H:%M')} | Reminders: {reminders_text}",
                     font=("Impact", 12), bg="lightblue", fg="white").pack(pady=5)

    # Close button for the view assignments window
    close_button = tk.Button(view_window, text="Close", command=view_window.destroy, font=("Impact", 12), bg="lightblue", fg="red", relief="flat")
    close_button.pack(pady=20)

# GUI for adding an assignment
def add_assignment_gui_window():
    add_window = tk.Toplevel(root)  # Create a new top-level window
    add_window.title("Add Assignment")
    add_window.geometry("400x300")

    # Set the background color of the window itself
    add_window.config(bg="lightblue")  # Set the background color of the entire window

    # Label for Assignment Name with matching background color
    tk.Label(add_window, text="Assignment Name:", font=("Impact", 12), bg="lightblue").pack(pady=5)

    # Entry field for Assignment Name
    name_entry = tk.Entry(add_window, font=("Impact", 12))
    name_entry.pack(pady=5)

    # Label for Due Date with matching background color
    tk.Label(add_window, text="Due Date (MM-DD-YYYY HH:MM):", font=("Impact", 12), bg="lightblue").pack(pady=5)

    # Entry field for Due Date
    due_date_entry = tk.Entry(add_window, font=("Impact", 12))
    due_date_entry.pack(pady=5)

    reminder_entries = []

    def add_reminder_field():
        frame = tk.Frame(add_window)
        frame.pack(pady=5)

        tk.Label(frame, text="Type (minutes/hours/days):", font=("Impact", 10), bg="lightblue").grid(row=0, column=0)
        type_entry = tk.Entry(frame, font=("Impact", 10), width=10)
        type_entry.grid(row=0, column=1)

        tk.Label(frame, text="Value:", font=("Impact", 10), bg="lightblue").grid(row=0, column=2)
        value_entry = tk.Entry(frame, font=("Impact", 10), width=10)
        value_entry.grid(row=0, column=3)

        reminder_entries.append({"type": type_entry, "value": value_entry})

    tk.Button(add_window, text="Add Reminder",font=("Impact",12),activebackground="lightblue",activeforeground="black", relief="flat", bg="lightblue",fg='white', command=add_reminder_field).pack(pady=10)

    def submit_assignment():
        name = name_entry.get()
        due_date_str = due_date_entry.get()
        reminders = []

        for entry in reminder_entries:
            reminder_type = entry["type"].get()
            try:
                reminder_value = int(entry["value"].get())
                reminders.append({"type": reminder_type, "value": reminder_value})
            except ValueError:
                messagebox.showerror("Error", "Invalid reminder value. Please enter a number.")
                return

        add_assignment_gui(name, due_date_str, reminders, add_window)

    submit_button = tk.Button(add_window, font=("Impact",12),text="Add Assignment",activebackground="lightblue",activeforeground="black", relief="flat", bg="lightblue",fg='white',command=submit_assignment)
    submit_button.pack(pady=10)

def close_window():
    root.quit()

# Main GUI window
root = tk.Tk()
root.geometry("400x300")

# Set the title text
root.title("Assignment Tracker")

# Customize the root window's background color to match your desired title appearance
root.config(bg="lightblue")

# Main content of the window
main_frame = tk.Frame(root, bg="lightblue")
main_frame.pack(fill="both", expand=True)

# Set a label to act as a custom title bar
title_label = tk.Label(main_frame, text="Assignment Tracker", fg="white", bg="lightblue", font=("Impact", 18))
title_label.pack(pady=20)

# Start the reminder system when the application starts
start_reminder_system()

add_assignment_button = tk.Button(root,activebackground="lightblue",activeforeground="black", relief="flat",text="Add Assignment", command=add_assignment_gui_window, bg="lightblue",fg='white', font=("Impact", 12))
add_assignment_button.pack(pady=10)

view_assignments_button = tk.Button(root,activebackground="lightblue",activeforeground="black", relief="flat",text="View Assignments", command=view_assignments_gui, bg="lightblue",fg='white', font=("Impact", 12))
view_assignments_button.pack(pady=10)

exit_button = tk.Button(root,relief="flat",activebackground="lightblue",activeforeground="black", text="Exit", command=root.quit,bg="lightblue",fg='red', font=("Impact", 12))
exit_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
