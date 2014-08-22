"""
This module contains classes for representing ProblemResults object

For further information visit http://codeforces.com/api/help/objects#ProblemResults
"""

from . import BaseJsonObject
from enum import Enum


__all__ = ['ProblemResult', 'ScoringSystemType']


class ScoringSystemType(Enum):
    """
    If type is PRELIMINARY then points can decrease (if, for example, solution will fail during system test).
    Otherwise, party can only increase points for this problem by submitting better solutions.
    """

    preliminary = 'PRELIMINARY'
    final = 'FINAL'


class ProblemResult(BaseJsonObject):
    """
    Represents a submissions results of a party for a problem.

    For further information visit http://codeforces.com/api/help/objects#ProblemResults
    """

    def __init__(self, data=None):
        self._points = None
        self._penalty = None
        self._rejected_attempt_count = None
        self._type = None
        self._best_submission_time = None

        super().__init__(data)

    def __repr__(self):
        return '<ProblemResult: {}>'.format(self.points)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.points = values['points']
        self.rejected_attempt_count = values['rejectedAttemptCount']
        self.type = values['type']

    def load_optional_fields_from_dict(self, values):
        super().load_optional_fields_from_dict(values)

        self.penalty = values.get('penalty')
        self.best_submission_time = values.get('bestSubmissionTimeSeconds')

    @property
    def points(self):
        """
        :return: Points or None if not initialized
        :rtype: float
        """
        return self._points

    @points.setter
    def points(self, value):
        """
        :param value: Points
        :type value: float or str
        """
        assert isinstance(value, (float, str))
        self._points = float(value)

    @property
    def penalty(self):
        """
        Can be absent

        Penalty (in ICPC meaning) of the party for this problem.

        :return: Penalty or None if not initialized or absent
        :rtype: int
        """
        return self._penalty

    @penalty.setter
    def penalty(self, value):
        """
        Can be absent

        Penalty (in ICPC meaning) of the party for this problem.

        :param value: Penalty or None if absent
        :type value: int or str
        """
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(value)

        self._penalty = value

    @property
    def rejected_attempt_count(self):
        """
        :return: Number of incorrect submissions or None if not initialized
        :rtype: int
        """
        return self._rejected_attempt_count

    @rejected_attempt_count.setter
    def rejected_attempt_count(self, value):
        """
        :param value: Number of incorrect submissions.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._rejected_attempt_count = int(value)

    @property
    def type(self):
        """
        :return: Problem type or None if not initialized
        :rtype: ScoringSystemType
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        :param value: Problem type
        :type value: ScoringSystemType or str
        """
        assert isinstance(value, (ScoringSystemType, str))
        self._type = ScoringSystemType(value)

    @property
    def best_submission_time(self):
        """
        Can be absent

        Number of seconds after the start of the contest before the submission, that brought
        maximal amount of points for this problem.

        :return: Best time or None if not initialized or absent
        :rtype: int
        """
        return self._best_submission_time

    @best_submission_time.setter
    def best_submission_time(self, value):
        """
        Can be absent

        Number of seconds after the start of the contest before the submission, that brought
        maximal amount of points for this problem.

        :param value: Best time or None if absent
        :type value: int or str
        """
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(value)

        self._best_submission_time = value
