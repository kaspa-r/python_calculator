from Calculator.calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self, calculator = Calculator):
        self.calc = calculator(0, False)

    def test_starting_sequence(self):
        starting_result = self.calc.result_in_memory
        starting_operation_counter = self.calc.operation_counter
        self.assertEqual(starting_result, 0, "Should be 0.")
        self.assertEqual(starting_operation_counter, 0, "Should be 0.")

    def test_check_input_types(self):
        with self.assertRaises(AssertionError):
            Calculator.check_input_types(5, "No", 4, 56)
            Calculator.check_input_types("String", "Cat", "Mouse")

    def test_find_decimal_point(self):
        self.assertEqual(self.calc.find_decimal_point(7.7777777, 1.1, 2.22, 3.333, 4.4444, 5.55555, 6.666666), 7, "Should be 7.")

    def test_store_memory(self):
        self.calc.change_return_type()
        self.assertEqual(self.calc.add(52,-3,86, 100), 'You have added 235 to 0 to get: 235.', "Should be 0")

    def test_change_return_type(self):
        self.assertEqual(self.calc.add(52,-3,86, 100), 235, "Should be 235")
        self.calc.change_return_type()
        self.assertEqual(self.calc.add(52,-3,86, 100), 'You have added 235 to 235 to get: 470.', "Should be 235")

    def test_add(self):
        self.assertEqual(self.calc.add(52,-3,86, 100), 235, "Should be 235")
        self.assertEqual(self.calc.add(-52.2, -3.0004, 86.0000032, 100.1, 0.00000001), 365.89960321, "Should be 365.8996032")

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(52,-3,86, 100), -235, "Should be -235")
        self.assertEqual(self.calc.subtract(-52.2,-3.0004,86.0000032, 100.1, 0.00000001), -365.89960321, "Should be -365.89960321")

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(52,-3,86, 100), 0, "Should be 0")
        self.calc.add(1)
        self.assertEqual(self.calc.multiply(-52.2,-3.0004,86.0000032, 100.1, 0.00000001), 0.01348287, "Should be 0.01348287")

    def test_division(self):
        self.calc.add(100)
        self.assertEqual(self.calc.divide(52, -3, 86, 100), -7.453786523553966e-05, "Should be -7.453786523553966e-05")
        self.assertEqual(self.calc.divide(-52.2, -3.0004, 86.0000032, 100.1, 0.00000001), -0.00552834, "Should be -0.00552834")

    def test_floor_division(self):
        self.calc.add(100)
        self.assertEqual(self.calc.floor_divide(52, -3, 86, 100), -1.0, "Should be -1")
        self.assertEqual(self.calc.floor_divide(-52.2,-3.0004,86.0000032, 100.1, 0.00000001), -0.0, "Should be -0.0")

    def test_root(self):
        self.calc.add(100)
        self.assertEqual(self.calc.root(52, -3, 86, 100), 0.9999965674103443, "Should be 0.9999965674103443")
        self.assertEqual(self.calc.root(-52.2, -3.0004, 86.0000032, 100.1, 0.00000001), 0.99974545, "Should be 0.99974545")

    def test_reset(self):
        self.calc.reset()
        self.assertEqual(self.calc.operation_counter, 0, "Should be 0.")
        self.assertEqual(self.calc.result_in_memory, 0, "Should be 0.")

if __name__ == '__main__':
    unittest.main()