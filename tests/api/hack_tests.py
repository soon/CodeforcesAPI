"""
This module provides classes for testing Hack object
"""

import unittest
import json

from codeforces import Hack
from codeforces import Party
from codeforces import Problem
from codeforces import JudgeProtocol
from codeforces import HackVerdictType


class HackTests(unittest.TestCase):

    def setUp(self):
        self.hack = Hack(None)

    def test_load_from_dict(self):
        d = {
            "id": 88042,
            "creationTimeSeconds": 1387381320,
            "hacker": {
                "contestId": 374,
                "members": [{"handle": "ocozalp"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 24,
                "startTimeSeconds": 1387380600
            },
            "defender": {
                "contestId": 374,
                "members": [{"handle": "h1me"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 24,
                "startTimeSeconds": 1387380600
            },
            "verdict": "HACK_SUCCESSFUL",
            "problem": {
                "contestId": 374,
                "index": "A",
                "name": "Inna and Pink Pony",
                "type": "PROGRAMMING",
                "points": 500.0,
                "tags": ["greedy", "implementation"]
            },
            "test": "1 5 1 3 1 1\r\n\n",
            "judgeProtocol": {
                "manual": "true",
                "protocol": "Solution verdict: \nWRONG_ANSWER\n\nChecker: \nwrong answer 1st words differ - "
                            "expected: \u0027Poor\u0027, found: \u00272\u0027\r\n\n\nInput: \n1 5 1 3 1 1\r\n\n\n"
                            "Output: \n2\r\n\n\nAnswer: \nPoor Inna and pony!\r\n\n\nTime: \n62\n\nMemory: \n0\n",
                "verdict": "Successful hacking attempt"
            }
        }

        self.hack.load_from_dict(d)

        self.assertEqual(88042, self.hack.id)
        self.assertEqual(1387381320, self.hack.creation_time)
        self.assertEqual(Party(d['hacker']), self.hack.hacker)
        self.assertEqual(Party(d['defender']), self.hack.defender)
        self.assertEqual(HackVerdictType.hack_successful, self.hack.verdict)
        self.assertEqual(Problem(d['problem']), self.hack.problem)
        self.assertEqual("1 5 1 3 1 1\r\n\n", self.hack.test)
        self.assertEqual(JudgeProtocol(d['judgeProtocol']), self.hack.judge_protocol)

    def test_load_only_required_from_dict(self):
        """
        Required fields are:
            id,
            creationTimeSeconds,
            hacker,
            defender,
            problem
        """

        d = {
            "id": 88042,
            "creationTimeSeconds": 1387381320,
            "hacker": {
                "contestId": 374,
                "members": [{"handle": "ocozalp"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 24,
                "startTimeSeconds": 1387380600
            },
            "defender": {
                "contestId": 374,
                "members": [{"handle": "h1me"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 24,
                "startTimeSeconds": 1387380600
            },
            "problem": {
                "contestId": 374,
                "index": "A",
                "name": "Inna and Pink Pony",
                "type": "PROGRAMMING",
                "points": 500.0,
                "tags": ["greedy", "implementation"]
            }
        }

        self.hack.load_from_dict(d)

        self.assertEqual(88042, self.hack.id)
        self.assertEqual(1387381320, self.hack.creation_time)
        self.assertEqual(Party(d['hacker']), self.hack.hacker)
        self.assertEqual(Party(d['defender']), self.hack.defender)
        self.assertEqual(Problem(d['problem']), self.hack.problem)

        self.assertIsNone(self.hack.verdict)
        self.assertIsNone(self.hack.test)
        self.assertIsNone(self.hack.judge_protocol)

    def test_load_from_json(self):
        d = {
            "id": 88042,
            "creationTimeSeconds": 1387381320,
            "hacker": {
                "contestId": 374,
                "members": [{"handle": "ocozalp"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 24,
                "startTimeSeconds": 1387380600
            },
            "defender": {
                "contestId": 374,
                "members": [{"handle": "h1me"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 24,
                "startTimeSeconds": 1387380600
            },
            "verdict": "HACK_SUCCESSFUL",
            "problem": {
                "contestId": 374,
                "index": "A",
                "name": "Inna and Pink Pony",
                "type": "PROGRAMMING",
                "points": 500.0,
                "tags": ["greedy", "implementation"]
            },
            "test": "1 5 1 3 1 1\r\n\n",
            "judgeProtocol": {
                "manual": "true",
                "protocol": "Solution verdict: \nWRONG_ANSWER\n\nChecker: \nwrong answer 1st words differ - "
                            "expected: \u0027Poor\u0027, found: \u00272\u0027\r\n\n\nInput: \n1 5 1 3 1 1\r\n\n\n"
                            "Output: \n2\r\n\n\nAnswer: \nPoor Inna and pony!\r\n\n\nTime: \n62\n\nMemory: \n0\n",
                "verdict": "Successful hacking attempt"
            }
        }

        j = json.dumps(d)

        self.hack.load_from_json(j)

        self.assertEqual(88042, self.hack.id)
        self.assertEqual(1387381320, self.hack.creation_time)
        self.assertEqual(Party(d['hacker']), self.hack.hacker)
        self.assertEqual(Party(d['defender']), self.hack.defender)
        self.assertEqual(HackVerdictType.hack_successful, self.hack.verdict)
        self.assertEqual(Problem(d['problem']), self.hack.problem)
        self.assertEqual("1 5 1 3 1 1\r\n\n", self.hack.test)
        self.assertEqual(JudgeProtocol(d['judgeProtocol']), self.hack.judge_protocol)

    def test_load_only_required_from_json(self):
        """
        Required fields are:
            id,
            creationTimeSeconds,
            hacker,
            defender,
            problem
        """

        d = {
            "id": 88042,
            "creationTimeSeconds": 1387381320,
            "hacker": {
                "contestId": 374,
                "members": [{"handle": "ocozalp"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 24,
                "startTimeSeconds": 1387380600
            },
            "defender": {
                "contestId": 374,
                "members": [{"handle": "h1me"}],
                "participantType": "CONTESTANT",
                "ghost": False,
                "room": 24,
                "startTimeSeconds": 1387380600
            },
            "problem": {
                "contestId": 374,
                "index": "A",
                "name": "Inna and Pink Pony",
                "type": "PROGRAMMING",
                "points": 500.0,
                "tags": ["greedy", "implementation"]
            }
        }

        j = json.dumps(d)

        self.hack.load_from_json(j)

        self.assertEqual(88042, self.hack.id)
        self.assertEqual(1387381320, self.hack.creation_time)
        self.assertEqual(Party(d['hacker']), self.hack.hacker)
        self.assertEqual(Party(d['defender']), self.hack.defender)
        self.assertEqual(Problem(d['problem']), self.hack.problem)

        self.assertIsNone(self.hack.verdict)
        self.assertIsNone(self.hack.test)
        self.assertIsNone(self.hack.judge_protocol)

if __name__ == '__main__':
    unittest.main()