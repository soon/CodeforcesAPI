"""
This module contains classes for representing Problem object

For further information visit http://codeforces.com/api/help/objects#Problem
"""

from enum import Enum
from . import BaseJsonObject


__all__ = ['Problem', 'ProblemType']


class ProblemType(Enum):
    programming = 'PROGRAMMING'
    question = 'QUESTION'


class Problem(BaseJsonObject):
    """
    Represents a problem.
    
    For further information visit http://codeforces.com/api/help/objects#Problem
    """

    def __init__(self, data=None):
        self._contest_id = None
        self._index = None
        self._name = None
        self._type = None
        self._points = None
        self._tags = None

        super().__init__(data)

    def __repr__(self):
        return '<Problem: {}/{}>'.format(self.contest_id, self.index)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.contest_id = values['contestId']
        self.index = values['index']
        self.name = values['name']
        self.type = values['type']
        self.tags = values['tags']

    def load_optional_fields_from_dict(self, values):
        super().load_optional_fields_from_dict(values)

        self.points = values.get('points')

    @property
    def contest_id(self):
        """
        Id of the contest, containing the problem.

        :return: Id or None if not initialized
        :rtype: int
        """
        return self._contest_id

    @contest_id.setter
    def contest_id(self, value):
        """
        Id of the contest, containing the problem.

        :param value: Id
        :type value: int
        """
        assert isinstance(value, (int, str))
        self._contest_id = int(value)

    @property
    def index(self):
        """
        Usually a letter or a letter, followed by a digit, that represent a problem index in a contest.

        :return: Index or None if not initialized
        :rtype: str
        """
        return self._index

    @index.setter
    def index(self, value):
        """
        Usually a letter or a letter, followed by a digit, that represent a problem index in a contest.

        :param value: Index
        :type value: str
        """
        assert isinstance(value, str)
        self._index = value

    @property
    def name(self):
        """
        Localized.

        :return: Name or None if not initialized
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Localized.

        :param value: Name
        :type value: str
        """
        assert isinstance(value, str)
        self._name = value

    @property
    def type(self):
        """
        :return: Problem type or None if not initialized
        :rtype: ProblemType
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        :param value: Problem type
        :type value: ProblemType or str
        """
        assert isinstance(value, (ProblemType, str))
        self._type = ProblemType(value)

    @property
    def points(self):
        """
        Can be absent.

        Maximum amount of points for the problem.

        :return: Points or None if not initialized or absent
        :rtype: float
        """
        return self._points

    @points.setter
    def points(self, value):
        """
        Can be absent.

        Maximum amount of points for the problem.

        :param value: Points or None if absent
        :type value: float or str
        """
        assert isinstance(value, (float, str)) or value is None

        if isinstance(value, str):
            value = str(value)

        self._points = value

    @property
    def tags(self):
        """
        :return: Problem tags or None if not initialized
        :rtype: list of str
        """
        return self._tags

    @tags.setter
    def tags(self, value):
        """
        :param value: Problem tags
        :rtype: list of str
        :return:
        """
        assert isinstance(value, list)
        self._tags = value
