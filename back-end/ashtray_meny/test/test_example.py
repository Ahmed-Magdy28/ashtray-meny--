from django.test import TestCase, SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        """Test adding numbers together."""
        self.assertEqual(calc.add(5, 6), 11)

    def test_subtract_numbers(self):
        "Test subtract"
        self.assertEqual(calc.subtract(5, 5), 0)


class ExampleTest1(TestCase):
    def test_basic_addition(self):
        """Test that 1 + 1 equals 2."""
        self.assertEqual(1 + 1, 2)
