"""
This module provides classes for testing Submission object
"""

import unittest

from codeforces import Submission
from codeforces import VerdictType
from codeforces import Problem
from codeforces import Party
from codeforces import TestsetType


class SubmissionTests(unittest.TestCase):

    def setUp(self):
        self.submission = Submission()

    def test_load_from_dict(self):
        d = {
            "id": 7268482,
            "contestId": 452,
            "creationTimeSeconds": 1406487265,
            "relativeTimeSeconds": 6865,
            "problem": {
                "contestId": 452,
                "index": "E",
                "name": "Three strings",
                "type": "PROGRAMMING",
                "points": 2500.0,
                "tags": [
                    "data structures",
                    "dsu",
                    "string suffix structures",
                    "strings"
                ]
            },
            "author": {
                "contestId": 452,
                "members": [{"handle": "Fefer_Ivan"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 86,
                "startTimeSeconds": 1406480400
            },
            "programmingLanguage": "GNU C++0x",
            "verdict": "OK",
            "testset": "TESTS",
            "passedTestCount": 67,
            "timeConsumedMillis": 343,
            "memoryConsumedBytes": 34816000
        }

        self.submission.load_from_dict(d)

        self.assertEqual(7268482, self.submission.id)
        self.assertEqual(452, self.submission.contest_id)
        self.assertEqual(1406487265, self.submission.creation_time)
        self.assertEqual(6865, self.submission.relative_time)
        self.assertEqual(Problem(d['problem']), self.submission.problem)
        self.assertEqual(Party(d['author']), self.submission.author)
        self.assertEqual("GNU C++0x", self.submission.programming_language)
        self.assertEqual(VerdictType.ok, self.submission.verdict)
        self.assertEqual(TestsetType.tests, self.submission.testset)
        self.assertEqual(67, self.submission.passed_test_count)
        self.assertEqual(343, self.submission.time_consumed)
        self.assertEqual(34816000, self.submission.memory_consumed)

    def test_load_only_required_from_dict(self):
        """
        Required fields are:

            id
            contestId
            creationTimeSeconds
            relativeTimeSeconds
            problem
            author
            programmingLanguage
            testset
            passedTestCount
            timeConsumedMillis
            memoryConsumedBytes
        """
        d = {
            "id": 7268482,
            "contestId": 452,
            "creationTimeSeconds": 1406487265,
            "relativeTimeSeconds": 6865,
            "problem": {
                "contestId": 452,
                "index": "E",
                "name": "Three strings",
                "type": "PROGRAMMING",
                "points": 2500.0,
                "tags": [
                    "data structures",
                    "dsu",
                    "string suffix structures",
                    "strings"
                ]
            },
            "author": {
                "contestId": 452,
                "members": [{"handle": "Fefer_Ivan"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 86,
                "startTimeSeconds": 1406480400
            },
            "programmingLanguage": "GNU C++0x",
            "testset": "TESTS",
            "passedTestCount": 67,
            "timeConsumedMillis": 343,
            "memoryConsumedBytes": 34816000
        }

        self.submission.load_from_dict(d)

        self.assertEqual(7268482, self.submission.id)
        self.assertEqual(452, self.submission.contest_id)
        self.assertEqual(1406487265, self.submission.creation_time)
        self.assertEqual(6865, self.submission.relative_time)
        self.assertEqual(Problem(d['problem']), self.submission.problem)
        self.assertEqual(Party(d['author']), self.submission.author)
        self.assertEqual("GNU C++0x", self.submission.programming_language)
        self.assertEqual(TestsetType.tests, self.submission.testset)
        self.assertEqual(67, self.submission.passed_test_count)
        self.assertEqual(343, self.submission.time_consumed)
        self.assertEqual(34816000, self.submission.memory_consumed)

        self.assertIsNone(self.submission.verdict)

    def test_load_from_json(self):
        d = {
            "id": 7268482,
            "contestId": 452,
            "creationTimeSeconds": 1406487265,
            "relativeTimeSeconds": 6865,
            "problem": {
                "contestId": 452,
                "index": "E",
                "name": "Three strings",
                "type": "PROGRAMMING",
                "points": 2500.0,
                "tags": [
                    "data structures",
                    "dsu",
                    "string suffix structures",
                    "strings"
                ]
            },
            "author": {
                "contestId": 452,
                "members": [{"handle": "Fefer_Ivan"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 86,
                "startTimeSeconds": 1406480400
            },
            "programmingLanguage": "GNU C++0x",
            "verdict": "OK",
            "testset": "TESTS",
            "passedTestCount": 67,
            "timeConsumedMillis": 343,
            "memoryConsumedBytes": 34816000
        }

        json = str(d).replace('False', 'false').replace("'", '"')

        self.submission.load_from_json(json)

        self.assertEqual(7268482, self.submission.id)
        self.assertEqual(452, self.submission.contest_id)
        self.assertEqual(1406487265, self.submission.creation_time)
        self.assertEqual(6865, self.submission.relative_time)
        self.assertEqual(Problem(d['problem']), self.submission.problem)
        self.assertEqual(Party(d['author']), self.submission.author)
        self.assertEqual("GNU C++0x", self.submission.programming_language)
        self.assertEqual(VerdictType.ok, self.submission.verdict)
        self.assertEqual(TestsetType.tests, self.submission.testset)
        self.assertEqual(67, self.submission.passed_test_count)
        self.assertEqual(343, self.submission.time_consumed)
        self.assertEqual(34816000, self.submission.memory_consumed)

    def test_load_only_required_from_json(self):
        """
        Required fields are:

            id
            contestId
            creationTimeSeconds
            relativeTimeSeconds
            problem
            author
            programmingLanguage
            testset
            passedTestCount
            timeConsumedMillis
            memoryConsumedBytes
        """
        d = {
            "id": 7268482,
            "contestId": 452,
            "creationTimeSeconds": 1406487265,
            "relativeTimeSeconds": 6865,
            "problem": {
                "contestId": 452,
                "index": "E",
                "name": "Three strings",
                "type": "PROGRAMMING",
                "points": 2500.0,
                "tags": [
                    "data structures",
                    "dsu",
                    "string suffix structures",
                    "strings"
                ]
            },
            "author": {
                "contestId": 452,
                "members": [{"handle": "Fefer_Ivan"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 86,
                "startTimeSeconds": 1406480400
            },
            "programmingLanguage": "GNU C++0x",
            "testset": "TESTS",
            "passedTestCount": 67,
            "timeConsumedMillis": 343,
            "memoryConsumedBytes": 34816000
        }

        json = str(d).replace('False', 'false').replace("'", '"')

        self.submission.load_from_json(json)

        self.assertEqual(7268482, self.submission.id)
        self.assertEqual(452, self.submission.contest_id)
        self.assertEqual(1406487265, self.submission.creation_time)
        self.assertEqual(6865, self.submission.relative_time)
        self.assertEqual(Problem(d['problem']), self.submission.problem)
        self.assertEqual(Party(d['author']), self.submission.author)
        self.assertEqual("GNU C++0x", self.submission.programming_language)
        self.assertEqual(TestsetType.tests, self.submission.testset)
        self.assertEqual(67, self.submission.passed_test_count)
        self.assertEqual(343, self.submission.time_consumed)
        self.assertEqual(34816000, self.submission.memory_consumed)

        self.assertIsNone(self.submission.verdict)


if __name__ == '__main__':
    unittest.main()
