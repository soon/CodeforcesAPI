"""
This module provides classes for testing Contest object
"""

import unittest
from api import Contest
from api import ContestType
from api import ContestPhase


class ContestTest(unittest.TestCase):

    def setUp(self):
        self.contest = Contest()

    def test_load_from_dict(self):
        d = {
            "id": 374,
            "name": "Codeforces Round #220 (Div. 2)",
            "type": "CF",
            "phase": "FINISHED",
            "frozen": False,
            "durationSeconds": 7200,
            "startTimeSeconds": 1387380600,
            "relativeTimeSeconds": 20865158,
            "preparedBy": "just_a_user",
            "websiteUrl": "http://no.website.now",
            "description": "No description",
            "difficulty": "4",
            "kind": "OpenCup Contest",
            "icpcRegion": "No region",
            "country": "No country",
            "city": "No city",
            "season": "No season"
        }

        self.contest.load_from_dict(d)

        self.assertEqual(374, self.contest.id)
        self.assertEqual("Codeforces Round #220 (Div. 2)", self.contest.name)
        self.assertEqual(ContestType.cf, self.contest.type)
        self.assertEqual(ContestPhase.finished, self.contest.phase)
        self.assertEqual(False, self.contest.frozen)
        self.assertEqual(7200, self.contest.duration)
        self.assertEqual(1387380600, self.contest.start_time)
        self.assertEqual(20865158, self.contest.relative_time)
        self.assertEqual("just_a_user", self.contest.prepared_by)
        self.assertEqual("http://no.website.now", self.contest.website_url)
        self.assertEqual("No description", self.contest.description)
        self.assertEqual(4, self.contest.difficulty)
        self.assertEqual("OpenCup Contest", self.contest.kind)
        self.assertEqual("No region", self.contest.icpc_region)
        self.assertEqual("No country", self.contest.country)
        self.assertEqual("No city", self.contest.city)
        self.assertEqual("No season", self.contest.season)

    def test_load_only_required_from_dict(self):
        """
        Required fields are:
            id
            name
            type
            phase
            frozen
            durationSeconds
            startTimeSeconds
            relativeTimeSeconds
        """

        d = {
            "id": 374,
            "name": "Codeforces Round #220 (Div. 2)",
            "type": "CF",
            "phase": "FINISHED",
            "frozen": False,
            "durationSeconds": 7200,
            "startTimeSeconds": 1387380600,
            "relativeTimeSeconds": 20865158,
        }

        self.contest.load_from_dict(d)

        self.assertEqual(374, self.contest.id)
        self.assertEqual("Codeforces Round #220 (Div. 2)", self.contest.name)
        self.assertEqual(ContestType.cf, self.contest.type)
        self.assertEqual(ContestPhase.finished, self.contest.phase)
        self.assertEqual(False, self.contest.frozen)
        self.assertEqual(7200, self.contest.duration)
        self.assertEqual(1387380600, self.contest.start_time)
        self.assertEqual(20865158, self.contest.relative_time)

        self.assertIsNone(self.contest.prepared_by)
        self.assertIsNone(self.contest.website_url)
        self.assertIsNone(self.contest.description)
        self.assertIsNone(self.contest.difficulty)
        self.assertIsNone(self.contest.kind)
        self.assertIsNone(self.contest.icpc_region)
        self.assertIsNone(self.contest.country)
        self.assertIsNone(self.contest.city)
        self.assertIsNone(self.contest.season)

    def load_only_required_from_json(self):
        """
        Required fields are:
            id
            name
            type
            phase
            frozen
            durationSeconds
            startTimeSeconds
            relativeTimeSeconds
        """
        json = '''{
            "id": 374,
            "name": "Codeforces Round #220 (Div. 2)",
            "type": "CF",
            "phase": "FINISHED",
            "frozen": false,
            "durationSeconds": 7200,
            "startTimeSeconds": 1387380600,
            "relativeTimeSeconds": 20865158
        }'''

        self.contest.load_from_json(json)

        self.assertEqual(374, self.contest.id)
        self.assertEqual("Codeforces Round #220 (Div. 2)", self.contest.name)
        self.assertEqual(ContestType.cf, self.contest.type)
        self.assertEqual(ContestPhase.finished, self.contest.phase)
        self.assertEqual(False, self.contest.frozen)
        self.assertEqual(7200, self.contest.duration)
        self.assertEqual(1387380600, self.contest.start_time)
        self.assertEqual(20865158, self.contest.relative_time)

        self.assertIsNone(self.contest.prepared_by)
        self.assertIsNone(self.contest.website_url)
        self.assertIsNone(self.contest.description)
        self.assertIsNone(self.contest.difficulty)
        self.assertIsNone(self.contest.kind)
        self.assertIsNone(self.contest.icpc_region)
        self.assertIsNone(self.contest.country)
        self.assertIsNone(self.contest.city)
        self.assertIsNone(self.contest.season)

    def test_load_from_json(self):

        json = '''{
            "id": 374,
            "name": "Codeforces Round #220 (Div. 2)",
            "type": "CF",
            "phase": "FINISHED",
            "frozen": false,
            "durationSeconds": 7200,
            "startTimeSeconds": 1387380600,
            "relativeTimeSeconds": 20865158,
            "preparedBy": "just_a_user",
            "websiteUrl": "http://no.website.now",
            "description": "No description",
            "difficulty": "4",
            "kind": "OpenCup Contest",
            "icpcRegion": "No region",
            "country": "No country",
            "city": "No city",
            "season": "No season"
        }'''

        self.contest.load_from_json(json)

        self.assertEqual(374, self.contest.id)
        self.assertEqual("Codeforces Round #220 (Div. 2)", self.contest.name)
        self.assertEqual(ContestType.cf, self.contest.type)
        self.assertEqual(ContestPhase.finished, self.contest.phase)
        self.assertEqual(False, self.contest.frozen)
        self.assertEqual(7200, self.contest.duration)
        self.assertEqual(1387380600, self.contest.start_time)
        self.assertEqual(20865158, self.contest.relative_time)
        self.assertEqual("just_a_user", self.contest.prepared_by)
        self.assertEqual("http://no.website.now", self.contest.website_url)
        self.assertEqual("No description", self.contest.description)
        self.assertEqual(4, self.contest.difficulty)
        self.assertEqual("OpenCup Contest", self.contest.kind)
        self.assertEqual("No region", self.contest.icpc_region)
        self.assertEqual("No country", self.contest.country)
        self.assertEqual("No city", self.contest.city)
        self.assertEqual("No season", self.contest.season)

if __name__ == '__main__':
    unittest.main()