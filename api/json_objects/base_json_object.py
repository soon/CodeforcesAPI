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
        :exception ValueError: raised when given dictionary does not contain required field
        """
        try:
            self.load_required_fields_from_dict(values)
        except KeyError as e:
            raise ValueError('Missed required field', e.args[0])

        self.load_optional_fields_from_dict(values)

    def load_required_fields_from_dict(self, values):
        """
        Loads required fields from given dictionary.

        This method SHOULD NOT care if value was not given

        Note: given dictionary may contain extra fields. just ignore them

        :param values: Dictionary with values
        :type values: dict
        """
        assert isinstance(values, dict)

    def load_optional_fields_from_dict(self, values):
        """
        Loads optional fields from given dictionary.

        Note: given dictionary may not contain needed value. It is recommended to use dict.get method
        The given dictionary may also contain extra fields. Just ignore them

        :param values: Dictionary with optional values
        :type values: dict
        """
        assert isinstance(values, dict)