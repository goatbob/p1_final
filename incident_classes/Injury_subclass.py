"""
program: Injury_subclass.py
author: kyle godwin
last date modified: 22 april 2023
"""
from incident_classes import Incident


class Injury(Incident):
    """Injury subclass of base class Incident"""
    def __init__(self, date, time, employee, incident_type="Injury", **kwargs):
        # injury_list = ["fracture", "bruise", "laceration", ""]
        super().__init__(date, time, employee, incident_type)
        if

        try:
            self.injury_type = kwargs["inj_type"]
            self.body_part = kwargs["body_part"]
        except KeyError:
            raise IncorrectArgumentsError

    def __str__(self):
        return f"{self.inc_employee} involved in {self.inc_type} on {self.inc_date} at {self.inc_time}." \
               f"\n{self.injury_type} affecting {self.body_part}." \
               f"\nSubmitted: {self.submit_date}"

    def __repr__(self):
        return f"Injury('{self.inc_date}', '{self.inc_time}', '{self.inc_employee}', " \
               f"inj_type='{self.injury_type}', body_part='{self.body_part}')"


class IncorrectArgumentsError(Exception):
    pass
