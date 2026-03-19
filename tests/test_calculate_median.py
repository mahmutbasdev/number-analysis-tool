import unittest
from number_analysis.calculations import calculate_median


class TestCalculations(unittest.TestCase):
    """Unit tests for calculate_median function."""

    def test_empty_list(self):
        # Empty list should return None.
        self.assertIsNone(calculate_median([]))

    def test_odd_list(self):
        # Median of odd-length list should be middle element after sorting.
        numbers = [3, 1, 2]
        self.assertEqual(calculate_median(numbers), 2)

    def test_even_list(self):
        # Median of even-length list should be average of two middle elements.
        numbers = [4, 2, 1, 3]
        self.assertEqual(calculate_median(numbers), 2.5)

    def test_sorted_list(self):
        # Median of already sorted list.
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_median(numbers), 3)

    def test_unsorted_list(self):
        #Median of unsorted list should be correctly computed.
        numbers = [10, 5, 7, 3]
        self.assertEqual(calculate_median(numbers), 6)


if __name__ == "__main__":
    unittest.main()
