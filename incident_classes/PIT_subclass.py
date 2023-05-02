"""
program: PIT_subclass.py
author: kyle godwin
last date modified: 01 may 2023
"""
from incident_classes import Incident


class PIT(Incident):
    """NearMiss subclass of base class Incident"""
    def __init__(self, date, time, employee, incident_type="PIT", **kwargs):
        super().__init__(date, time, employee, incident_type)
        self.PITs = []
        try:
            self.impact = kwargs["impact"]
            self.experience = kwargs["experience"]
        except KeyError:
            raise IncorrectArgumentsError

    def __str__(self):
        return f"{self.inc_employee} involved in {self.inc_type} on {self.inc_date} at {self.inc_time}." \
               f"\nWas impact: {self.impact}, with operator experience: {self.experience}." \
               f"\nSubmitted: {self.submit_date}"

    def __repr__(self):
        return f"Injury('{self.inc_date}', '{self.inc_time}', '{self.inc_employee}', " \
               f"inj_type='{self.nearMiss_type}', body_part='{self.nearMiss_severity}')"


class IncorrectArgumentsError(Exception):
    pass
