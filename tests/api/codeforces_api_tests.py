"""
This module provides classes for testing User object
"""
import os
import unittest
from unittest import mock

from codeforces.api.codeforces_api import CodeforcesAPI


class CodeforcesAPITests(unittest.TestCase):
    def load_fixture(self, fixture_name):
        with open(os.path.join('fixtures', fixture_name), 'r') as fixture:
            return fixture.read().encode('utf-8')

    def patch_urlopen_read_method(self, urlopen, fixture_name):
        urlopen.return_value.__enter__.return_value.read.return_value = self.load_fixture(fixture_name)

    @mock.patch('codeforces.api.codeforces_api.urlopen', autospec=True)
    def test_contest_rating_changes(self, urlopen):
        self.patch_urlopen_read_method(urlopen, 'contest.ratingChanges.json')
        api = CodeforcesAPI()
        rating_changes = api.contest_rating_changes(42)

        self.assertEqual(9, len(list(rating_changes)))
        urlopen.assert_called_with('http://codeforces.com/api/contest.ratingChanges?contestId=42')


if __name__ == '__main__':
    unittest.main()
