"""
This module provides classes for testing Problem object
"""

import unittest

from codeforces import Problem
from codeforces import ProblemType


class ProblemTests(unittest.TestCase):

    def setUp(self):
        self.problem = Problem()

    def test_load_from_dict(self):
        d = {
            "contestId": 374,
            "index": "A",
            "name": "Inna and Pink Pony",
            "type": "PROGRAMMING",
            "points": 500.0,
            "tags": ["greedy", "implementation"]
        }

        self.problem.load_from_dict(d)

        self.assertEqual(374, self.problem.contest_id)
        self.assertEqual('A', self.problem.index)
        self.assertEqual('Inna and Pink Pony', self.problem.name)
        self.assertEqual(ProblemType.programming, self.problem.type)
        self.assertEqual(500.0, self.problem.points)
        self.assertEqual(["greedy", "implementation"], self.problem.tags)

    def load_only_required_from_dict(self):
        d = {
            "contestId": 374,
            "index": "A",
            "name": "Inna and Pink Pony",
            "type": "PROGRAMMING",
            "tags": ["greedy", "implementation"]
        }

        self.problem.load_from_dict(d)

        self.assertEqual(374, self.problem.contest_id)
        self.assertEqual('A', self.problem.index)
        self.assertEqual('Inna and Pink Pony', self.problem.name)
        self.assertEqual(ProblemType.programming, self.problem.type)
        self.assertEqual(["greedy", "implementation"], self.problem.tags)

        self.assertIsNone(self.problem.points)

    def test_load_from_json(self):
        json = '''{
            "contestId": 374,
            "index": "A",
            "name": "Inna and Pink Pony",
            "type": "PROGRAMMING",
            "points": 500.0,
            "tags": ["greedy","implementation"]
        }'''

        self.problem.load_from_json(json)

        self.assertEqual(374, self.problem.contest_id)
        self.assertEqual('A', self.problem.index)
        self.assertEqual('Inna and Pink Pony', self.problem.name)
        self.assertEqual(ProblemType.programming, self.problem.type)
        self.assertEqual(500.0, self.problem.points)
        self.assertEqual(["greedy", "implementation"], self.problem.tags)

    def load_only_required_from_json(self):
        json = '''{
            "contestId": 374,
            "index": "A",
            "name": "Inna and Pink Pony",
            "type": "PROGRAMMING",
            "tags": ["greedy","implementation"]
        }'''

        self.problem.load_from_json(json)

        self.assertEqual(374, self.problem.contest_id)
        self.assertEqual('A', self.problem.index)
        self.assertEqual('Inna and Pink Pony', self.problem.name)
        self.assertEqual(ProblemType.programming, self.problem.type)
        self.assertEqual(["greedy", "implementation"], self.problem.tags)

        self.assertIsNone(self.problem.points)


if __name__ == '__main__':
    unittest.main()
