"""
This module contains classes for representing Problem object

For further information visit http://codeforces.com/api/help/objects#Problem
"""

from enum import Enum
from . import BaseJsonObject


class ProblemType(Enum):
    programming = 'PROGRAMMING'
    question = 'QUESTION'


class Problem(BaseJsonObject):
    """
    This class represents Problem object
    
    For further information visit http://codeforces.com/api/help/objects#Problem
    """

    def __init__(self, s=None):
        self._contest_id = None
        self._index = None
        self._name = None
        self._type = None
        self._points = None
        self._tags = None

        super().__init__(s)

    def load_from_dict(self, values):
        try:
            self.contest_id = values['contestId']
            self.index = values['index']
            self.name = values['name']
            self.type = values['type']
            self.tags = values['tags']
        except KeyError as e:
            raise ValueError('Missed required field', e.args[0])

        self.points = values.get('points')

    @property
    def contest_id(self):
        return self._contest_id

    @contest_id.setter
    def contest_id(self, value):
        assert isinstance(value, (int, str))

        if isinstance(value, str):
            value = int(value)

        self._contest_id = value

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        assert isinstance(value, str)
        self._index = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str)
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        assert isinstance(value, (ProblemType, str))

        if isinstance(value, str):
            value = ProblemType(value)

        self._type = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        assert isinstance(value, (float, str)) or value is None

        if isinstance(value, str):
            value = str(value)

        self._points = value

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, value):
        assert isinstance(value, list)
        self._tags = value
