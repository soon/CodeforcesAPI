"""
This module provides classes for testing Pary object
"""

import unittest
from api import Party
from api import Member
from api import ParticipantType


class PartyTests(unittest.TestCase):

    def setUp(self):
        self.party = Party(None)

    def test_load_from_dict(self):
        d = {
            "contestId": 374,
            "members": [{"handle": "ocozalp"},
                        {"handle": "awesomeHandle"}],
            "participantType": "CONTESTANT",
            "teamId": 42,
            "teamName": "The best team. Ever",
            "ghost": False,
            "room": 24,
            "startTimeSeconds": 1387380600
        }

        self.party.load_from_dict(d)

        self.assertEqual(374, self.party.contest_id)
        self.assertEqual([Member({"handle": "ocozalp"}),
                          Member({"handle": "awesomeHandle"})],
                         self.party.members)
        self.assertEqual(ParticipantType.contestant, self.party.participant_type)
        self.assertEqual(42, self.party.team_id)
        self.assertEqual("The best team. Ever", self.party.team_name)
        self.assertEqual(False, self.party.ghost)
        self.assertEqual(24, self.party.room)
        self.assertEqual(1387380600, self.party.start_time)

    def test_load_only_required_from_dict(self):
        """
        Required fields are:

            contestId,
            members,
            participantType,
            ghost
        """
        d = {
            "contestId": 374,
            "members": [{"handle": "ocozalp"},
                        {"handle": "awesomeHandle"}],
            "participantType": "CONTESTANT",
            "ghost": False
        }

        self.party.load_from_dict(d)

        self.assertEqual(374, self.party.contest_id)
        self.assertEqual([Member({"handle": "ocozalp"}),
                          Member({"handle": "awesomeHandle"})],
                         self.party.members)
        self.assertEqual(ParticipantType.contestant, self.party.participant_type)
        self.assertEqual(False, self.party.ghost)

        self.assertIsNone(self.party.team_id)
        self.assertIsNone(self.party.team_name)
        self.assertIsNone(self.party.room)
        self.assertIsNone(self.party.start_time)

    def test_load_from_json(self):
        json = '''{
            "contestId": 374,
            "members": [{"handle": "ocozalp"},
                        {"handle": "awesomeHandle"}],
            "participantType": "CONTESTANT",
            "teamId": 42,
            "teamName": "The best team. Ever",
            "ghost": false,
            "room": 24,
            "startTimeSeconds": 1387380600
        }'''

        self.party.load_from_json(json)

        self.assertEqual(374, self.party.contest_id)
        self.assertEqual([Member({"handle": "ocozalp"}),
                          Member({"handle": "awesomeHandle"})],
                         self.party.members)
        self.assertEqual(ParticipantType.contestant, self.party.participant_type)
        self.assertEqual(42, self.party.team_id)
        self.assertEqual("The best team. Ever", self.party.team_name)
        self.assertEqual(False, self.party.ghost)
        self.assertEqual(24, self.party.room)
        self.assertEqual(1387380600, self.party.start_time)

    def test_load_only_required_from_json(self):
        """
        Required fields are:

            contestId,
            members,
            participantType,
            ghost
        """
        json = '''{
            "contestId": 374,
            "members": [{"handle": "ocozalp"},
                        {"handle": "awesomeHandle"}],
            "participantType": "CONTESTANT",
            "ghost": false
        }'''

        self.party.load_from_json(json)

        self.assertEqual(374, self.party.contest_id)
        self.assertEqual([Member({"handle": "ocozalp"}),
                          Member({"handle": "awesomeHandle"})],
                         self.party.members)
        self.assertEqual(ParticipantType.contestant, self.party.participant_type)
        self.assertEqual(False, self.party.ghost)

        self.assertIsNone(self.party.team_id)
        self.assertIsNone(self.party.team_name)
        self.assertIsNone(self.party.room)
        self.assertIsNone(self.party.start_time)
