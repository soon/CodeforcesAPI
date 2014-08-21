"""
This module provides classes for testing RanklistRow object
"""

import unittest
from api import RanklistRow, Party, ProblemResult


class RanklistRowTests(unittest.TestCase):

    def setUp(self):
        self.row = RanklistRow(None)

    def load_from_dict(self):
        d = {
            "party": {
                "contestId": 374,
                "members": [{"handle": "Deception"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 46,
                "startTimeSeconds": 1387380600
            },
            "rank": 1,
            "points": 4902.0,
            "penalty": 0,
            "successfulHackCount": 11,
            "unsuccessfulHackCount": 1,
            "problemResults": [
                {
                    "points": 312.0,
                    "rejectedAttemptCount": 1,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 4174
                }, {
                    "points": 596.0,
                    "rejectedAttemptCount": 2,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 4583
                }, {
                    "points": 1128.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 3751
                }, {
                    "points": 1816.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 1430
                }, {
                    "points": 0.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL"
                }
            ],
            "lastSubmissionTimeSeconds": 424242
        }

        self.row.load_from_dict(d)

        self.assertEqual(Party(d['party']), self.row.party)
        self.assertEqual(1, self.row.rank)
        self.assertEqual(4902.0, self.row.points)
        self.assertEqual(0, self.row.penalty)
        self.assertEqual(11, self.row.successful_hack_count)
        self.assertEqual(1, self.row.unsuccessful_hack_count)
        self.assertEqual(list(map(ProblemResult, d['problemResults'])), self.row.problem_results)
        self.assertEqual(424242, self.row.last_submission_time)

    def load_only_required_from_dict(self):
        """
        Required fields are:

            party
            rank
            points
            penalty
            successfulHackCount
            unsuccessfulHackCount
            problemResults
        """
        d = {
            "party": {
                "contestId": 374,
                "members": [{"handle": "Deception"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 46,
                "startTimeSeconds": 1387380600
            },
            "rank": 1,
            "points": 4902.0,
            "penalty": 0,
            "successfulHackCount": 11,
            "unsuccessfulHackCount": 1,
            "problemResults": [
                {
                    "points": 312.0,
                    "rejectedAttemptCount": 1,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 4174
                }, {
                    "points": 596.0,
                    "rejectedAttemptCount": 2,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 4583
                }, {
                    "points": 1128.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 3751
                }, {
                    "points": 1816.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 1430
                }, {
                    "points": 0.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL"
                }
            ]
        }

        self.row.load_from_dict(d)

        self.assertEqual(Party(d['party']), self.row.party)
        self.assertEqual(1, self.row.rank)
        self.assertEqual(4902.0, self.row.points)
        self.assertEqual(0, self.row.penalty)
        self.assertEqual(11, self.row.successful_hack_count)
        self.assertEqual(1, self.row.unsuccessful_hack_count)
        self.assertEqual(list(map(ProblemResult, d['problemResults'])), self.row.problem_results)

        self.assertIsNone(self.row.last_submission_time)

    def test_load_from_json(self):
        d = {
            "party": {
                "contestId": 374,
                "members": [{"handle": "Deception"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 46,
                "startTimeSeconds": 1387380600
            },
            "rank": 1,
            "points": 4902.0,
            "penalty": 0,
            "successfulHackCount": 11,
            "unsuccessfulHackCount": 1,
            "problemResults": [
                {
                    "points": 312.0,
                    "rejectedAttemptCount": 1,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 4174
                }, {
                    "points": 596.0,
                    "rejectedAttemptCount": 2,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 4583
                }, {
                    "points": 1128.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 3751
                }, {
                    "points": 1816.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 1430
                }, {
                    "points": 0.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL"
                }
            ],
            "lastSubmissionTimeSeconds": 424242
        }

        json = str(d).replace('False', 'false').replace("'", '"')

        self.row.load_from_json(json)

        self.assertEqual(Party(d['party']), self.row.party)
        self.assertEqual(1, self.row.rank)
        self.assertEqual(4902.0, self.row.points)
        self.assertEqual(0, self.row.penalty)
        self.assertEqual(11, self.row.successful_hack_count)
        self.assertEqual(1, self.row.unsuccessful_hack_count)
        self.assertEqual(list(map(ProblemResult, d['problemResults'])), self.row.problem_results)
        self.assertEqual(424242, self.row.last_submission_time)

    def test_load_only_required_from_json(self):
        """
        Required fields are:

            party
            rank
            points
            penalty
            successfulHackCount
            unsuccessfulHackCount
            problemResults
        """
        d = {
            "party": {
                "contestId": 374,
                "members": [{"handle": "Deception"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 46,
                "startTimeSeconds": 1387380600
            },
            "rank": 1,
            "points": 4902.0,
            "penalty": 0,
            "successfulHackCount": 11,
            "unsuccessfulHackCount": 1,
            "problemResults": [
                {
                    "points": 312.0,
                    "rejectedAttemptCount": 1,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 4174
                }, {
                    "points": 596.0,
                    "rejectedAttemptCount": 2,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 4583
                }, {
                    "points": 1128.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 3751
                }, {
                    "points": 1816.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL",
                    "bestSubmissionTimeSeconds": 1430
                }, {
                    "points": 0.0,
                    "rejectedAttemptCount": 0,
                    "type": "FINAL"
                }
            ]
        }

        json = str(d).replace('False', 'false').replace("'", '"')

        self.row.load_from_json(json)

        self.assertEqual(Party(d['party']), self.row.party)
        self.assertEqual(1, self.row.rank)
        self.assertEqual(4902.0, self.row.points)
        self.assertEqual(0, self.row.penalty)
        self.assertEqual(11, self.row.successful_hack_count)
        self.assertEqual(1, self.row.unsuccessful_hack_count)
        self.assertEqual(list(map(ProblemResult, d['problemResults'])), self.row.problem_results)

        self.assertIsNone(self.row.last_submission_time)


if __name__ == '__main__':
    unittest.main()
