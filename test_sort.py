import unittest
from main import sort

class TestSortFunction(unittest.TestCase):
    def test_heavy_item(self):
        result = sort(50, 50, 50, 25)  # mass > 20
        self.assertEqual(result, "SPECIAL")

    def test_large_item(self):
        result = sort(250, 50, 50, 10)  # width > 200
        self.assertEqual(result, "SPECIAL")

    def test_bulk_item(self):
        result = sort(100, 100, 100, 10)  # volume = 1,000,000
        self.assertEqual(result, "SPECIAL")

    def test_regular_item(self):
        result = sort(50, 50, 50, 10)  # normal size, normal weight
        self.assertEqual(result, "STANDARD")

    def test_rejected_item(self):
        result = sort(122, 323, 102, 25)  # volume > 1,000,000 and mass > 20
        self.assertEqual(result, "REJECTED")

    def test_invalid_negative_dimensions(self):
        with self.assertRaises(ValueError):
            sort(-10, 50, 50, 10)  # negative width

    def test_invalid_negative_mass(self):
        with self.assertRaises(ValueError):
            sort(50, 50, 50, -5)  # negative mass

    def test_zero_dimension(self):
        with self.assertRaises(ValueError):
            sort(0, 50, 50, 10)  # zero width

if __name__ == "__main__":
    unittest.main()