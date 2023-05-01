"""
program: ITA_GUI.py
author: kyle godwin
last date modified: 21 april 2023

GUI for injury tracking application
"""
import tkinter as tk
import csv
from incident_classes import *


def submit():
    incident_type.get()
    incident_date.get()
    incident_time.get()
    incident_employee.get()
    injury_type.get()
    body_part.get()

    if incident_type.get() == "Injury":
        inj = Injury(incident_date.get(), incident_time.get(), incident_employee.get(),
                     inj_type=injury_type.get(), body_part=body_part.get())

        f = open("incidentdata.txt", "a")
        f.write(f"{inj} \n")
        f.close()
        del inj

    elif incident_type.get() == "Near Miss":
        nm = NearMiss(incident_date.get(), incident_time.get(), incident_employee.get(),
                     nm_type=pass, nm_severity=pass)

        f = open("incidentdata.txt", "a")
        f.write(f"{nm} \n")
        f.close()
        del nm


def to_csv(date, time, emp, inc):
    row = [date, time, emp, inc]
    # attributes = ['Date', 'Time', 'Employee', 'Incident Type']

    with open("incidentdatabase.csv", "a") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(row)
        csvfile.close()


# def to_database():
    # call libraries
    # write to a database


def clear_text():
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    employee_entry.delete(0, tk.END)
    injury_entry.delete(0, tk.END)
    body_entry.delete(0, tk.END)


root = tk.Tk()
root.title("ITA")
root.geometry("300x400")

incident_type = tk.StringVar()
incident_options = ["Near Miss", "Injury", "Forklift"]
incident_date = tk.StringVar()
incident_time = tk.StringVar()
incident_employee = tk.StringVar()
injury_type = tk.StringVar()
body_part = tk.StringVar()


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

injury_label = tk.Label(root, text="Nature of injury:")
injury_label.pack()

injury_entry = tk.Entry(root, textvariable=injury_type, width=25, bg="light cyan")
injury_entry.pack()

body_label = tk.Label(root, text="Body part affected:")
body_label.pack()

body_entry = tk.Entry(root, textvariable=body_part, width=25, bg="light cyan")
body_entry.pack()

submit_button = tk.Button(root, text="Submit", command=lambda: [submit(), to_csv(incident_date.get(),
                                                                                 incident_time.get(),
                                                                                 incident_employee.get(),
                                                                                 incident_type.get()),
                                                                clear_text()])
submit_button.pack()

root.mainloop()
