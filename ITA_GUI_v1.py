"""
program: ITA_GUI_v1.py
author: kyle godwin
last date modified: 21 april 2023

GUI for injury tracking application
"""
import tkinter as tk
import csv
from incident_classes import *


def submit():

    if incident_type.get() == "Injury":
        inj = Injury(incident_date.get(), incident_time.get(), incident_employee.get(),
                     inj_type=injury_type.get(), body_part=body_part.get())

        f = open("incidentdata.txt", "a")
        f.write(f"{inj} \n")
        f.close()
        del inj

    elif incident_type.get() == "Near Miss":
        nm = NearMiss(incident_date.get(), incident_time.get(), incident_employee.get(),
                      nm_type=nearmiss_type.get(), nm_severity=nearmiss_severity.get())

        f = open("incidentdata.txt", "a")
        f.write(f"{nm} \n")
        f.close()
        del nm
        
    elif incident_type.get() == "PIT":
        pit = PIT(incident_date.get(), incident_time.get(), incident_employee.get(),
                  impact=pit_collision.get(), experience=pit_experience.get())

        f = open("incidentdata.txt", "a")
        f.write(f"{pit} \n")
        f.close()
        del pit
        
    else:
        incorrect_label.config(text="Incident type not selected")


def to_csv():
    incident = [incident_date.get(), incident_time.get(), incident_employee.get(), incident_type.get()]

    with open("incidentdatabase.csv", "a") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(incident)
        csvfile.close()


def clear_text():
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    employee_entry.delete(0, tk.END)
    injury_entry.delete(0, tk.END)
    body_entry.delete(0, tk.END)
    collision_entry.delete(0, tk.END)
    experience_entry.delete(0, tk.END)
    nmtype_entry.delete(0, tk.END)
    nmseverity_entry.delete(0, tk.END)


root = tk.Tk()
root.title("ITA")
root.geometry("300x500")

# variable initialization
incident_type = tk.StringVar()
incident_options = ["Near Miss", "Injury", "PIT"]
incident_date = tk.StringVar()
incident_time = tk.StringVar()
incident_employee = tk.StringVar()
injury_type = tk.StringVar()
body_part = tk.StringVar()
pit_collision = tk.StringVar()
pit_experience = tk.StringVar()
nearmiss_type = tk.StringVar()
nearmiss_severity = tk.StringVar()

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

# injury data entry
injury_label = tk.Label(root, text="Nature of injury (if injury):")
injury_label.pack()

injury_entry = tk.Entry(root, textvariable=injury_type, width=25, bg="light cyan")
injury_entry.pack()

body_label = tk.Label(root, text="Body part affected (if injury):")
body_label.pack()

body_entry = tk.Entry(root, textvariable=body_part, width=25, bg="light cyan")
body_entry.pack()

# PIT data entry
collision_label = tk.Label(root, text="PIT collision (if PIT):")
collision_label.pack()

collision_entry = tk.Entry(root, textvariable=pit_collision, width=25, bg="light cyan")
collision_entry.pack()

experience_label = tk.Label(root, text="PIT experience (if PIT):")
experience_label.pack()

experience_entry = tk.Entry(root, textvariable=pit_experience, width=25, bg="light cyan")
experience_entry.pack()

# near miss data entry
nmtype_label = tk.Label(root, text="Near miss type (if near miss):")
nmtype_label.pack()

nmtype_entry = tk.Entry(root, textvariable=nearmiss_type, width=25, bg="light cyan")
nmtype_entry.pack()

nmseverity_label = tk.Label(root, text="Near miss severity (if near miss):")
nmseverity_label.pack()

nmseverity_entry = tk.Entry(root, textvariable=nearmiss_severity, width=25, bg="light cyan")
nmseverity_entry.pack()

# submit button
submit_button = tk.Button(root, text="Submit", command=lambda: [submit(), to_csv(), clear_text()])
submit_button.pack()

# label to display message when incident type not selected
incorrect_label = tk.Label(root, text="")
incorrect_label.pack()


root.mainloop()
