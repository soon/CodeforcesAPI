"""
This module provides classes for testing RatingChange object
"""

import unittest
from api import RatingChange


class RatingChangeTests(unittest.TestCase):

    def setUp(self):
        self.rating = RatingChange(None)

    def test_load_from_dict(self):
        d = {
            "contestId": 1,
            "contestName": "Codeforces Beta Round #1",
            "rank": 30,
            "ratingUpdateTimeSeconds": 1266588000,
            "oldRating": 0,
            "newRating": 1502
        }

        self.rating.load_from_dict(d)

        self.assertEqual(1, self.rating.contest_id)
        self.assertEqual("Codeforces Beta Round #1", self.rating.contest_name)
        self.assertEqual(30, self.rating.rank)
        self.assertEqual(1266588000, self.rating.rating_update_time)
        self.assertEqual(0, self.rating.old_rating)
        self.assertEqual(1502, self.rating.new_rating)

    def test_load_from_json(self):
        json = '''{
            "contestId": 1,
            "contestName": "Codeforces Beta Round #1",
            "rank": 30,
            "ratingUpdateTimeSeconds": 1266588000,
            "oldRating": 0,
            "newRating": 1502
        }'''

        self.rating.load_from_json(json)

        self.assertEqual(1, self.rating.contest_id)
        self.assertEqual("Codeforces Beta Round #1", self.rating.contest_name)
        self.assertEqual(30, self.rating.rank)
        self.assertEqual(1266588000, self.rating.rating_update_time)
        self.assertEqual(0, self.rating.old_rating)
        self.assertEqual(1502, self.rating.new_rating)


if __name__ == '__main__':
    unittest.main()
