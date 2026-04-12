import unittest
from hehe import calculate_statistics

class TestDataAnalysis(unittest.TestCase):
    def test_calculate_statistics_count(self):
        """Verify that the count of elements in the summary is correct."""
        data = [1, 2, 3, 4, 5]
        result = calculate_statistics(data)
        # 'count' is the first row of the describe() output
        self.assertEqual(result.at['count', 'Values'], 5)

if __name__ == '__main__':
    unittest.main() 