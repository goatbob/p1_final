"""
program: NearMiss_subclass.py
author: kyle godwin
last date modified: 30 april 2023
"""
from incident_classes import Incident


class NearMiss(Incident):
    """NearMiss subclass of base class Incident"""
    def __init__(self, date, time, employee, incident_type="Near Miss", **kwargs):
        super().__init__(date, time, employee, incident_type)
        self.nearMisses = []
        try:
            self.nearMiss_type = kwargs["nm_type"]
            self.nearMiss_severity = kwargs["nm_severity"]
        except KeyError:
            raise IncorrectArgumentsError

    def __str__(self):
        return f"{self.inc_employee} involved in {self.inc_type} on {self.inc_date} at {self.inc_time}." \
               f"\n{self.nearMiss_type} of {self.nearMiss_severity} severity." \
               f"\nSubmitted: {self.submit_date}"

    def __repr__(self):
        return f"Injury('{self.inc_date}', '{self.inc_time}', '{self.inc_employee}', " \
               f"inj_type='{self.nearMiss_type}', body_part='{self.nearMiss_severity}')"


class IncorrectArgumentsError(Exception):
    pass
