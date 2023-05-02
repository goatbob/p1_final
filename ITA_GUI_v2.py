"""
program: ITA_GUI_v2.py
author: kyle godwin
last date modified: 02 may 2023

GUI for injury tracking application
"""
import tkinter as tk
import final_database as db


def submit():

    db.create_incident(conn, (incident_date.get(), incident_time.get(), incident_employee.get(),
                              incident_type.get(), incident_description.get()))


def incident_output():
    """
    :return: incident table in output box
    """
    with conn:
        incidents = db.select_all_incidents(conn)
        for row in incidents:
            database_box.insert(tk.END, row)


def clear_text():
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    employee_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)


root = tk.Tk()
root.title("ITA")
root.geometry("300x500")

conn = db.create_connection("ITA_database.db")
db.create_database("ITA_database.db")

# variable initialization
incident_type = tk.StringVar()
incident_options = ["Near Miss", "Injury", "PIT"]
incident_date = tk.StringVar()
incident_time = tk.StringVar()
incident_employee = tk.StringVar()
incident_description = tk.StringVar()


# incident data entry
incident_label = tk.Label(root, text="Select incident type:")
incident_label.pack()

incident_menu = tk.OptionMenu(root, incident_type, *incident_options)
incident_menu.pack()

date_label = tk.Label(root, text="Incident date:")
date_label.pack()

date_entry = tk.Entry(root, textvariable=incident_date, width=25, bg="light cyan")
date_entry.pack()

time_label = tk.Label(root, text="Incident time:")
time_label.pack()

time_entry = tk.Entry(root, textvariable=incident_time, width=25, bg="light cyan")
time_entry.pack()

employee_label = tk.Label(root, text="Employee(s):")
employee_label.pack()

employee_entry = tk.Entry(root, textvariable=incident_employee, width=25, bg="light cyan")
employee_entry.pack()

description_label = tk.Label(root, text="Description:")
description_label.pack()

description_entry = tk.Entry(root, textvariable=incident_description, width=25, bg="light cyan")
description_entry.pack()

# enter button
enter_button = tk.Button(root, text="Enter Incident", command=lambda: [submit(), clear_text()])
enter_button.pack()

# output box for database
database_box = tk.Text(root, width=25, bg="light cyan")
database_box.pack()

# submit button
submit_button = tk.Button(root, text="Print Incident Database", command=incident_output)
submit_button.pack()


root.mainloop()
