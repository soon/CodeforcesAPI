"""
This module provides classes for testing Hack object
"""

import unittest
from api import Member


class MemberTests(unittest.TestCase):

    def setUp(self):
        self.member = Member(None)

    def test_load_from_dict(self):
        d = {
            "handle": "soon"
        }

        self.member.load_from_dict(d)

        self.assertEqual('soon', self.member.handle)

    def test_load_from_json(self):
        json = '''{
            "handle": "soon"
        }'''

        self.member.load_from_json(json)

        self.assertEqual('soon', self.member.handle)


if __name__ == '__main__':
    unittest.main()