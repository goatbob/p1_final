import unittest
from incident_classes import *
from incident_classes import Injury as i


class ITA(unittest.TestCase):

    def setUp(self):
        self.inj = i("22 april 2023", "1500", "Maven", inj_type="fracture", body_part="finger")

    def tearDown(self):
        del self.inj

    def testArgInput(self):
        self.assertEqual(self.inj.inc_date, "22 april 2023")
        self.assertEqual(self.inj.inc_time, "1500")
        self.assertEqual(self.inj.inc_employee, "Maven")

    def testKwargInput(self):
        self.assertEqual(self.inj.injury_type, "fracture")
        self.assertEqual(self.inj.body_part, "finger")

    def testIncorrectArgumentsError(self):
        with self.assertRaises(IncorrectArgumentsError):
            inj = i("22 april 2023", "1500", "Maven", inj_typ="fracture", bod_part="finger")


if __name__ == '__main__':
    unittest.main()
