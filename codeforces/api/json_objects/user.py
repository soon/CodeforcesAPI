"""
This file provides class for representing User object

For further information visit http://codeforces.com/api/help/objects#User
"""

from . import BaseJsonObject


__all__ = ['User']


class User(BaseJsonObject):
    """
    Represents a Codeforces user.

    For further information visit http://codeforces.com/api/help/objects#User
    """

    def __init__(self, data=None):
        self._handle = None
        self._email = None
        self._vk_id = None
        self._open_id = None
        self._first_name = None
        self._last_name = None
        self._country = None
        self._city = None
        self._organization = None
        self._contribution = None
        self._rank = None
        self._rating = None
        self._max_rank = None
        self._max_rating = None
        self._last_online_time = None
        self._registration_time = None

        super().__init__(data)

    def __repr__(self):
        return '<User: {}>'.format(self.handle)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.handle = values['handle']
        self.contribution = values['contribution']
        self.rank = values['rank']
        self.rating = values['rating']
        self.max_rank = values['maxRank']
        self.max_rating = values['maxRating']
        self.last_online_time = values['lastOnlineTimeSeconds']
        self.registration_time = values['registrationTimeSeconds']

    def load_optional_fields_from_dict(self, values):
        super().load_optional_fields_from_dict(values)

        self.email = values.get('email')
        self.vk_id = values.get('vkId')
        self.open_id = values.get('openId')
        self.first_name = values.get('firstName')
        self.last_name = values.get('lastName')
        self.country = values.get('country')
        self.city = values.get('city')
        self.organization = values.get('organization')

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
    def email(self):
        """
        Shown only if user allowed to share his contact info.

        :return: Email or None if not initialized or user denied to share his contact info
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, value):
        """
        Shown only if user allowed to share his contact info.

        :param value: Email or None if user denied to share his contact info
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._email = value

    @property
    def vk_id(self):
        """
        User id for VK social network. Shown only if user allowed to share his contact info.

        :return: Id or None if not initialized or user denied to share his contact info
        :rtype: str
        """
        return self._vk_id

    @vk_id.setter
    def vk_id(self, value):
        """
        User id for VK social network. Shown only if user allowed to share his contact info.

        :param value: Id or None if user denied to share his contact info
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._vk_id = value

    @property
    def open_id(self):
        """
        Shown only if user allowed to share his contact info.

        :return: Id or None if not initialized or user denied to share his contact info
        :rtype: str
        """
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        """
        Shown only if user allowed to share his contact info.

        :param value: Id or None if user denied to share his contact info
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._open_id = value

    @property
    def first_name(self):
        """
        Can be absent. Localized.

        :return: First name or None if not initialized or absent
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """
        Can be absent. Localized.

        :param value: First name or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._first_name = value

    @property
    def last_name(self):
        """
        Can be absent. Localized.

        :return: Last name or None if not initialized or absent
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """
        Can be absent. Localized.

        :param value: Last name or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._last_name = value

    @property
    def country(self):
        """
        Can be absent. Localized.

        :return: Country or None if not initialized or absent
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, value):
        """
        Can be absent. Localized.

        :param value: Country or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._country = value

    @property
    def city(self):
        """
        Can be absent. Localized.

        :return: City or None if not initialized or absent
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, value):
        """
        Can be absent. Localized.

        :param value: City or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._city = value

    @property
    def organization(self):
        """
        Can be absent. Localized.

        :return: Organization or None if not initialized or absent
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, value):
        """
        Can be absent. Localized.

        :param value: Organization or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._organization = value

    @property
    def contribution(self):
        """
        :return: Contribution or None if not initialized
        :rtype: int
        """
        return self._contribution

    @contribution.setter
    def contribution(self, value):
        """
        :param value: Contribution
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._contribution = int(value)

    @property
    def rank(self):
        """
        Localized.

        :return: Rank or None if not initialized
        :rtype: str
        """
        return self._rank

    @rank.setter
    def rank(self, value):
        """
        Localized.

        :param value: Rank
        :type value: str
        """
        assert isinstance(value, str)
        self._rank = value

    @property
    def rating(self):
        """
        :return: Rating or None if not initialized
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, value):
        """
        :param value: Rating
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._rating = int(value)

    @property
    def max_rank(self):
        """
        Localized.

        :return: Max rank or None if not initialized
        :rtype: str
        """
        return self._max_rank

    @max_rank.setter
    def max_rank(self, value):
        """
        Localized.

        :param value: Max rank
        :type value: str
        """
        assert isinstance(value, str)
        self._max_rank = value

    @property
    def max_rating(self):
        """
        :return: Max rating or None if not initialized
        :rtype: int
        """
        return self._max_rating

    @max_rating.setter
    def max_rating(self, value):
        """
        :param value: Max rating
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._max_rating = int(value)

    @property
    def last_online_time(self):
        """
        Time, when user was last seen online, in unix format.

        :return: Time or None if not initialized
        :rtype: int
        """
        return self._last_online_time

    @last_online_time.setter
    def last_online_time(self, value):
        """
        Time, when user was last seen online, in unix format.

        :param value: Time
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._last_online_time = int(value)

    @property
    def registration_time(self):
        """
        Time, when user was registered, in unix format.

        :return: Time or None if not initialized
        :rtype: int
        """
        return self._registration_time

    @registration_time.setter
    def registration_time(self, value):
        """
        Time, when user was registered, in unix format.

        :param value: Time
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._registration_time = int(value)
