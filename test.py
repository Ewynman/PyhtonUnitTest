import unittest
from payBill import payBill


class TestPayBill(unittest.TestCase):
    def test_even_split(self):
        bill_dict, extra_guest = payBill(100.0, 4)
        self.assertEqual(len(bill_dict), 4)
        self.assertAlmostEqual(bill_dict['guest1'], 25.0)
        self.assertAlmostEqual(bill_dict['guest2'], 25.0)
        self.assertAlmostEqual(bill_dict['guest3'], 25.0)
        self.assertAlmostEqual(bill_dict['guest4'], 25.0)
        self.assertIsNone(extra_guest)

    def test_one_guest_extra(self):
        bill_dict, extra_guest = payBill(45.16, 3)
        self.assertEqual(len(bill_dict), 3)
        self.assertAlmostEqual(sum(bill_dict.values()), 45.16)
        if extra_guest is not None:
            self.assertIn(extra_guest, bill_dict.keys())

    def test_zero_bill(self):
        bill_dict, extra_guest = payBill(0.0, 5)
        self.assertEqual(len(bill_dict), 5)
        self.assertAlmostEqual(bill_dict['guest1'], 0.0)
        self.assertAlmostEqual(bill_dict['guest2'], 0.0)
        self.assertAlmostEqual(bill_dict['guest3'], 0.0)
        self.assertAlmostEqual(bill_dict['guest4'], 0.0)
        self.assertAlmostEqual(bill_dict['guest5'], 0.0)
        self.assertIsNone(extra_guest)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            payBill(100.0, 0)
        with self.assertRaises(Exception):
            payBill('', 4)
        with self.assertRaises(Exception):
            payBill(100.0, 'four')


if __name__ == '__main__':
    unittest.main()
