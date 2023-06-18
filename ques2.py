import tkinter as tk
import calendar

def show_calendar():   #The try and ValueError are part of the exception handling mechanism in
    #  Python.
    # They are used to handle potential errors that may occur during the execution of a program.
    try:
        year = int(year_entry.get())

        cal = calendar.calendar(year)
        calendar_text.config(text=cal)
    except ValueError:
        calendar_text.config(text="Invalid year. Please enter a valid year.")

window = tk.Tk()
window.title("Calendar Application")

tk.Label(window, text="Enter Year:").pack()
year_entry = tk.Entry(window)
year_entry.pack()

tk.Button(window, text="Show Calendar", command=show_calendar).pack()

calendar_text = tk.Label(window, text="")
calendar_text.pack()

window.mainloop()
