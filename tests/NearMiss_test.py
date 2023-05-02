import unittest
from incident_classes import *
from incident_classes import NearMiss as n


class NearMissSubclassTest(unittest.TestCase):

    def setUp(self):
        self.nm = n("22 april 2023", "1500", "Maven", nm_type="fall", nm_severity="high")

    def tearDown(self):
        del self.nm

    def testArgInput(self):
        self.assertEqual(self.nm.inc_date, "22 april 2023")
        self.assertEqual(self.nm.inc_time, "1500")
        self.assertEqual(self.nm.inc_employee, "Maven")

    def testKwargInput(self):
        self.assertEqual(self.nm.nearMiss_type, "fall")
        self.assertEqual(self.nm.nearMiss_severity, "high")

    def testIncorrectArgumentsError(self):
        with self.assertRaises(IncorrectArgumentsError):
            nm = n("22 april 2023", "1500", "Maven", inj_typ="fracture", bod_part="finger")


if __name__ == '__main__':
    unittest.main()
