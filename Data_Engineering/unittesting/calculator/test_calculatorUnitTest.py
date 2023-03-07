import unittest

from calculator_UnitTest import addUT, subtractUT, multiplyUT, divideUT


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addUT(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtractUT((5, 3), 2))

    def test_multiplication(self):
        self.assertEqual(multiplyUT(2, 3), 6)

    def test_division(self):
        self.assertEqual(divideUT(10, 5), 2)


if __name__ == '__main__':
    unittest.main()
