"""
This module contains classes for representing RanklistRow object

For further information visit http://codeforces.com/api/help/objects#RanklistRow
"""

from . import BaseJsonObject, Party, ProblemResult
from codeforces.utils import lazy_property


__all__ = ['RanklistRow']


class RanklistRow(BaseJsonObject):
    """
    Represents a ranklist row.

    For further information visit http://codeforces.com/api/help/objects#RanklistRow
    """

    def __init__(self, data=None):
        self._party = None
        self._rank = None
        self._points = None
        self._penalty = None
        self._successful_hack_count = None
        self._unsuccessful_hack_count = None
        self._problem_results = None
        self._last_submission_time = None

        super().__init__(data)

    def __repr__(self):
        return '<RanklistRow: {}>'.format(self.party)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.party = values['party']
        self.rank = values['rank']
        self.points = values['points']
        self.penalty = values['penalty']
        self.successful_hack_count = values['successfulHackCount']
        self.unsuccessful_hack_count = values['unsuccessfulHackCount']
        self.problem_results = values['problemResults']

    def load_optional_fields_from_dict(self, values):
        super().load_optional_fields_from_dict(values)

        self.last_submission_time = values.get('lastSubmissionTimeSeconds')

    @lazy_property
    def party(self):
        """
        Lazy property.

        :return: Party that took a corresponding place in the contest or None if not initialized
        :rtype: Party
        """
        return self._party

    @party.setter
    def party(self, value):
        """
        Lazy property.

        :param value: Party that took a corresponding place in the contest.
        :type value: Party or str or dict
        """
        assert isinstance(value, (Party, str, dict))

        if not isinstance(value, Party):
            value = Party(value)

        self._party = value

    @property
    def rank(self):
        """
        :return: Party place in the contest or None if not initialized
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, value):
        """
        :param value: Party place in the contest.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._rank = int(value)

    @property
    def points(self):
        """
        :return: Total amount of points, scored by the party or None if not initialized
        :rtype: float
        """
        return self._points

    @points.setter
    def points(self, value):
        """
        :param value:  Total amount of points, scored by the party.
        :type value: float or str
        """
        assert isinstance(value, (float, str))
        self._points = float(value)

    @property
    def penalty(self):
        """
        Total penalty (in ICPC meaning) of the party.

        :return: Penalty or None if not initialized
        :rtype: int
        """
        return self._penalty

    @penalty.setter
    def penalty(self, value):
        """
        Total penalty (in ICPC meaning) of the party.

        :param value: Penalty
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._penalty = int(value)

    @property
    def successful_hack_count(self):
        """
        :return: Successful hack count or None if not initialized
        :rtype: int
        """
        return self._successful_hack_count

    @successful_hack_count.setter
    def successful_hack_count(self, value):
        """
        :param value: Successful hack count
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._successful_hack_count = int(value)

    @property
    def unsuccessful_hack_count(self):
        """
        :return: Unsuccessful hack count or None if not initialized
        :rtype: int
        """
        return self._unsuccessful_hack_count

    @unsuccessful_hack_count.setter
    def unsuccessful_hack_count(self, value):
        """
        :param value: Unsuccessful hack count
        :type value: int or str
        """
        self._unsuccessful_hack_count = value

    @lazy_property
    def problem_results(self):
        """
        Lazy property.

        Party results for each problem.

        Order of the problems is the same as in "problems" field of the returned object.

        :return: List of ProblemResult objects or None if not initialized
        :rtype: list of ProblemResult
        """
        return self._problem_results

    @problem_results.setter
    def problem_results(self, value):
        """
        Lazy property.

        Party results for each problem.

        Order of the problems is the same as in "problems" field of the returned object.

        :param value: List of ProblemResult objects
        :type value: list of ProblemResult or list of dict
        """
        assert isinstance(value, list)

        if value:
            if not isinstance(value[0], ProblemResult):
                value = list(map(ProblemResult, value))

        self._problem_results = value

    @property
    def last_submission_time(self):
        """
        For IOI contests only.

        Time in seconds from the start of the contest to the last submission
        that added some points to the total score of the party.

        :return: Time or None if not initialized or absent
        :rtype: int
        """
        return self._last_submission_time

    @last_submission_time.setter
    def last_submission_time(self, value):
        """
        For IOI contests only.

        Time in seconds from the start of the contest to the last submission
        that added some points to the total score of the party.

        :param value: Time
        :type value: int or str
        """
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(value)

        self._last_submission_time = value
