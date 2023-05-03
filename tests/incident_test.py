import unittest
from incident_classes import *
from incident_classes import Incident as inc
import datetime


class IncidentClassTest(unittest.TestCase):

    def setUp(self):
        self.incident = inc("22 april 2023", "1500", "Maven", "Near Miss")

    def tearDown(self):
        del self.incident

    def testInput(self):
        self.assertEqual(self.incident.inc_date, "22 april 2023")
        self.assertEqual(self.incident.inc_time, "1500")
        self.assertEqual(self.incident.inc_employee, "Maven")
        self.assertEqual(self.incident.inc_type, "Near Miss")

    def testString(self):
        self.assertEqual(str(self.incident), "Maven involved in Near Miss on 22 april 2023 at 1500.")

    def testRepresentation(self):
        self.assertEqual(repr(self.incident), "Incident('22 april 2023', '1500', 'Maven', 'Near Miss')")


if __name__ == '__main__':
    unittest.main()
