"""
This module provides classes for testing ProblemStatistics object
"""

import unittest
from api import ProblemStatistics


class ProblemStatisticsTests(unittest.TestCase):

    def setUp(self):
        self.stats = ProblemStatistics()

    def test_load_from_dict(self):
        d = {
            "contestId": 460,
            "index": "B",
            "solvedCount": 2246
        }

        self.stats.load_from_dict(d)

        self.assertEqual(460, self.stats.contest_id)
        self.assertEqual('B', self.stats.index)
        self.assertEqual(2246, self.stats.solved_count)

    def test_load_from_json(self):
        json = '''{
            "contestId": 460,
            "index": "B",
            "solvedCount": 2246
        }'''

        self.stats.load_from_json(json)

        self.assertEqual(460, self.stats.contest_id)
        self.assertEqual('B', self.stats.index)
        self.assertEqual(2246, self.stats.solved_count)


if __name__ == '__main__':
    unittest.main()
