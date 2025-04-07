import unittest
from app.services import calculate

class TestCalculate(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculate(2,3,'add'), 5)
    def test_sous(self):
        self.assertEqual(calculate(20,5,'sub'), 15)
    def test_div(self):
        self.assertEqual(calculate(10,5,'div'),2)
    def test_mul(self):
        self.assertEqual(calculate(4, 3, 'mul'), 12)
    def test_div_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(10,0,'div')
    def test_invalid_op(self):
        with self.assertRaises(ValueError):
            calculate(23,23,'pow')

