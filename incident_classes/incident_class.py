"""
program: incident_class.py
author: kyle godwin
last date modified: 02 may 2023
"""
import datetime


class Incident:

    def __init__(self, date, time, employee, incident_type, sub_date=datetime.datetime.now()):
        self.inc_date = date
        self.inc_time = time
        self.inc_employee = employee
        self.inc_type = incident_type
        self.submit_date = sub_date

    def __str__(self):
        return f"{self.inc_employee} involved in {self.inc_type} on {self.inc_date} at {self.inc_time}." \
               f"\nSubmitted: {self.submit_date}"

    def __repr__(self):
        return f"Incident('{self.inc_date}', '{self.inc_time}', '{self.inc_employee}', '{self.inc_type}')"
