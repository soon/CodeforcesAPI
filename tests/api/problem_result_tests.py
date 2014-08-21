"""
This module provides classes for testing ProblemResult object
"""

import unittest

from api import ProblemResult
from api import ScoringSystemType


class ProblemResultTests(unittest.TestCase):

    def setUp(self):
        self.result = ProblemResult(None)

    def test_load_from_dict(self):
        d = {
            "points": 312.0,
            "penalty": 42,
            "rejectedAttemptCount": 1,
            "type": "FINAL",
            "bestSubmissionTimeSeconds": 4174
        }

        self.result.load_from_dict(d)

        self.assertEqual(312.0, self.result.points)
        self.assertEqual(42, self.result.penalty)
        self.assertEqual(1, self.result.rejected_attempt_count)
        self.assertEqual(ScoringSystemType.final, self.result.type)
        self.assertEqual(4174, self.result.best_submission_time)

    def test_load_only_required_from_dict(self):
        """
        Required fields are:

            points,
            rejectedAttemptCount,
            type

        """
        d = {
            "points": 312.0,
            "rejectedAttemptCount": 1,
            "type": "FINAL"
        }

        self.result.load_from_dict(d)

        self.assertEqual(312.0, self.result.points)
        self.assertEqual(1, self.result.rejected_attempt_count)
        self.assertEqual(ScoringSystemType.final, self.result.type)

        self.assertIsNone(self.result.penalty)
        self.assertIsNone(self.result.best_submission_time)

    def test_load_from_json(self):
        json = '''{
            "points": 312.0,
            "penalty": 42,
            "rejectedAttemptCount": 1,
            "type": "FINAL",
            "bestSubmissionTimeSeconds": 4174
        }'''

        self.result.load_from_json(json)

        self.assertEqual(312.0, self.result.points)
        self.assertEqual(42, self.result.penalty)
        self.assertEqual(1, self.result.rejected_attempt_count)
        self.assertEqual(ScoringSystemType.final, self.result.type)
        self.assertEqual(4174, self.result.best_submission_time)

    def test_load_only_required_from_json(self):
        """
        Required fields are:

            points,
            rejectedAttemptCount,
            type

        """
        json = '''{
            "points": 312.0,
            "rejectedAttemptCount": 1,
            "type": "FINAL"
        }'''

        self.result.load_from_json(json)

        self.assertEqual(312.0, self.result.points)
        self.assertEqual(1, self.result.rejected_attempt_count)
        self.assertEqual(ScoringSystemType.final, self.result.type)

        self.assertIsNone(self.result.penalty)
        self.assertIsNone(self.result.best_submission_time)


if __name__ == '__main__':
    unittest.main()
