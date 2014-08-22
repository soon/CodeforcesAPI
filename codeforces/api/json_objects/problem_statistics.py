"""
This module contains classes for representing ProblemStatistics object

For further information visit http://codeforces.com/api/help/objects#ProblemStatistics
"""

from . import BaseJsonObject


__all__ = ['ProblemStatistics']


class ProblemStatistics(BaseJsonObject):
    """
    Represents a statistic data about a problem.

    For further information visit http://codeforces.com/api/help/objects#ProblemStatistics
    """

    def __init__(self, data=None):
        self._contest_id = None
        self._index = None
        self._solved_count = None

        super().__init__(data)

    def __repr__(self):
        return '<ProblemStatistics: {}/{}: {}>'.format(self.contest_id, self.index, self.solved_count)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.contest_id = values['contestId']
        self.index = values['index']
        self.solved_count = values['solvedCount']

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
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._contest_id = int(value)
        
    @property
    def index(self):
        """
        Usually a letter or a letter, followed by a digit, that represent a problem index in a contest.

        :return: Index or None if not initialized
        :rtype: int
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
    def solved_count(self):
        """
        :return: Number of users, who solved the problem or None if not initialized
        :rtype: int
        """
        return self._solved_count

    @solved_count.setter
    def solved_count(self, value):
        """
        :param value: Number of users, who solved the problem.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._solved_count = int(value)
