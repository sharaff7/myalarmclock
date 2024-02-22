import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class AlarmClock:
    def __init__(self, root):
        # Initialize the Tkinter window
        self.root = root
        self.root.title("Python Alarm Clock")
        self.root.geometry("400x200")

        # Create and place GUI components (Label, Entry, Button)
        self.label = tk.Label(root, text="Set Alarm (24-hour format):", font=("Helvetica", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 14))
        self.entry.pack(pady=10)

        self.btn_set_alarm = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.btn_set_alarm.pack(pady=20)

    def set_alarm(self):
        # Get the entered alarm time from the Entry widget
        alarm_time_str = self.entry.get()
        
        try:
            # Convert the entered time string to a datetime object
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M").replace(second=0)
            current_time = datetime.now().replace(second=0)
            
            # Calculate the time difference between current time and alarm time
            time_difference = (alarm_time - current_time).total_seconds()
            
            # Show a confirmation message with the set alarm time
            messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_time_str}.")
            
            # Schedule the show_alarm_message function after the calculated time difference
            self.root.after(int(time_difference * 1000), self.show_alarm_message)
        except ValueError:
            # Show an error message for invalid time format
            messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")

    def show_alarm_message(self):
        # Hide the main Tkinter window
        self.root.iconify()

        # Show a message when the alarm goes off
        messagebox.showinfo("Alarm", "Time to wake up!")

        # Deiconify the main Tkinter window after showing the messagebox
        self.root.deiconify()

# Create the Tkinter root window and the AlarmClock instance
root = tk.Tk()
alarm_clock = AlarmClock(root)

# Run the Tkinter event loop
root.mainloop()

