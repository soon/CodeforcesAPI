"""
This module contains class for representing base json object
"""

import json


class BaseJsonObject:
    """
    Every Codeforces Json object should extend this class
    """
    def __init__(self, s):
        assert isinstance(s, (str, dict)) or s is None

        if s is not None:
            if isinstance(s, str):
                self.load_from_json(s)
            else:
                self.load_from_dict(s)

    def load_from_json(self, s):
        """
        Loads data from given string in JSON format

        :param s: Data in JSON format
        :type s: str
        """
        values = json.loads(s)

        self.load_from_dict(values)

    def load_from_dict(self, values):
        """
        Loads data from given dictionary

        :param values: Dictionary with values
        :type values: dict
        """
        pass
