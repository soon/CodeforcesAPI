"""
This module contains classes for representing RatingChange object

For further information visit http://codeforces.com/api/help/objects#RatingChange
"""

from . import BaseJsonObject


__all__ = ['RatingChange']


class RatingChange(BaseJsonObject):
    """
    Represents a participation of user in rated contest.

    For further information visit http://codeforces.com/api/help/objects#RatingChange
    """

    def __init__(self, data=None):
        self._contest_id = None
        self._contest_name = None
        self._handle = None
        self._rank = None
        self._rating_update_time = None
        self._old_rating = None
        self._new_rating = None

        super().__init__(data)

    def __repr__(self):
        return '<RatingChange: {}, {}->{}>'.format(self.contest_id, self.old_rating, self.new_rating)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.contest_id = values['contestId']
        self.contest_name = values['contestName']
        self.handle = values['handle']
        self.rank = values['rank']
        self.rating_update_time = values['ratingUpdateTimeSeconds']
        self.old_rating = values['oldRating']
        self.new_rating = values['newRating']

    @property
    def contest_id(self):
        """
        :return: Contest ID or None if not initialized
        :rtype: int
        """
        return self._contest_id

    @contest_id.setter
    def contest_id(self, value):
        """
        :param value: Contest ID
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._contest_id = int(value)

    @property
    def contest_name(self):
        """
        Localized.

        :return: Contest name or None if not initialized
        :rtype: str
        """
        return self._contest_name

    @contest_name.setter
    def contest_name(self, value):
        """
        Localized.

        :param value: Contest name
        :type value: str
        """
        assert isinstance(value, str)
        self._contest_name = value

    @property
    def handle(self):
        """
        Codeforces user handle.

        :return: Handle or None if not initialized
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, value):
        """
        Codeforces user handle.

        :param value: Handle
        :type value: str
        """
        assert isinstance(value, str)
        self._handle = value

    @property
    def rank(self):
        """
        Place of the user in the contest.

        This field contains user rank on the moment of rating update.
        If afterwards rank changes (e.g. someone get disqualified), this field will not be update
        and will contain old rank.

        :return: User rank or None if not initialized
        :rtype: int
        """
        return self._rank

    @rank.setter
    def rank(self, value):
        """
        Place of the user in the contest.

        This field contains user rank on the moment of rating update.
        If afterwards rank changes (e.g. someone get disqualified), this field will not be update
        and will contain old rank.

        :param value: User rank
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._rank = int(value)

    @property
    def rating_update_time(self):
        """
        :return: Time, when rating for the contest was update, in unix-format, or None if not initialized
        :rtype: int
        """
        return self._rating_update_time

    @rating_update_time.setter
    def rating_update_time(self, value):
        """
        :param value: Time, when rating for the contest was update, in unix-format.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._rating_update_time = int(value)

    @property
    def old_rating(self):
        """
        :return: User rating before the contest or None if not initialized
        :rtype: int
        """
        return self._old_rating

    @old_rating.setter
    def old_rating(self, value):
        """
        :param value: User rating before the contest.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._old_rating = int(value)

    @property
    def new_rating(self):
        """
        :return: User rating after the contest or None if not initialized
        :rtype: int
        """
        return self._new_rating

    @new_rating.setter
    def new_rating(self, value):
        """
        :param value: User rating after the contest.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._new_rating = int(value)
