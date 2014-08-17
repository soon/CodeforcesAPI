"""
This module contains class for representing base json object
"""

import json
import copy


__all__ = ['BaseJsonObject']


class BaseJsonObject:
    """
    Every Codeforces Json object should extend this class
    """

    def __init__(self, data):
        """
        :param data: Data in JSON format
        :type data: str or dict
        """
        assert isinstance(data, (str, dict)) or data is None

        if data is not None:
            if isinstance(data, str):
                self.load_from_json(data)
            else:
                self.load_from_dict(data)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __hash__(self):
        return make_hash(self.__dict__)

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


# http://stackoverflow.com/a/8714242/1532460
def make_hash(o):
    """
    Makes a hash from a dictionary, list, tuple or set to any level, that contains
    only other hashable types (including any lists, tuples, sets, and
    dictionaries).
    """

    if isinstance(o, (set, tuple, list)):
        return tuple([make_hash(e) for e in o])
    elif not isinstance(o, dict):
        return hash(o)

    new_o = copy.deepcopy(o)
    for k, v in new_o.items():
        new_o[k] = make_hash(v)

    return hash(tuple(frozenset(sorted(new_o.items()))))