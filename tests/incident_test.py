import unittest
from incident_classes import *
from incident_classes import Incident as inc


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


if __name__ == '__main__':
    unittest.main()
