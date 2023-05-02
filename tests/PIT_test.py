import unittest
from incident_classes import *
from incident_classes import PIT as p


class PITSubclassTest(unittest.TestCase):

    def setUp(self):
        self.pit = p("22 april 2023", "1500", "Maven", impact="yes", experience="<1 year")

    def tearDown(self):
        del self.pit

    def testArgInput(self):
        self.assertEqual(self.pit.inc_date, "22 april 2023")
        self.assertEqual(self.pit.inc_time, "1500")
        self.assertEqual(self.pit.inc_employee, "Maven")

    def testKwargInput(self):
        self.assertEqual(self.pit.impact, "yes")
        self.assertEqual(self.pit.experience, "<1 year")

    def testIncorrectArgumentsError(self):
        with self.assertRaises(IncorrectArgumentsError):
            pit = p("22 april 2023", "1500", "Maven", inj_typ="fracture", bod_part="finger")


if __name__ == '__main__':
    unittest.main()
