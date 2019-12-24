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

    Fields that should always be available are:
        handle
        contribution
        lastOnlineTimeSeconds
        registrationTimeSeconds
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
        self._friend_of_count = None
        self._avatar = None
        self._title_photo = None
        super().__init__(data)

    def __repr__(self):
        return '<User: {}>'.format(self.handle)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.handle = values['handle']
        self.contribution = values['contribution']
        self.last_online_time = values['lastOnlineTimeSeconds']
        self.registration_time = values['registrationTimeSeconds']

    def load_optional_fields_from_dict(self, values):
        super().load_optional_fields_from_dict(values)

        self.rank = values.get('rank')
        self.max_rank = values.get('maxRank')
        self.rating = values.get('rating')
        self.max_rating = values.get('maxRating')

        self.email = values.get('email')
        self.vk_id = values.get('vkId')
        self.open_id = values.get('openId')
        self.first_name = values.get('firstName')
        self.last_name = values.get('lastName')
        self.country = values.get('country')
        self.city = values.get('city')
        self.organization = values.get('organization')
        self.friend_of_count = values.get('friendOfCount')
        self.avatar = values.get('avatar')
        self.title_photo = values.get('titlePhoto')

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
        :rtype: str or NoneType
        """
        return self._rank

    @rank.setter
    def rank(self, value):
        """
        Localized.

        :param value: Rank
        :type value: str or NoneType
        """
        assert isinstance(value, str) or value is None
        self._rank = value

    @property
    def rating(self):
        """
        :return: Rating or None if not initialized
        :rtype: int or NoneType
        """
        return self._rating

    @rating.setter
    def rating(self, value):
        """
        :param value: Rating
        :type value: int, str or NoneType
        """
        assert isinstance(value, (int, str)) or value is None
        if value is None:
            self._rating = 0
        else:
            self._rating = int(value)

    @property
    def max_rank(self):
        """
        Localized.

        :return: Max rank or None if not initialized
        :rtype: str or NoneType
        """
        return self._max_rank

    @max_rank.setter
    def max_rank(self, value):
        """
        Localized.

        :param value: Max rank
        :type value: str or NoneType
        """
        assert isinstance(value, str) or value is None
        self._max_rank = value

    @property
    def max_rating(self):
        """
        :return: Max rating or None if not initialized
        :rtype: int or NoneType
        """
        return self._max_rating

    @max_rating.setter
    def max_rating(self, value):
        """
        :param value: Max rating
        :type value: int, str or NoneType
        """
        assert isinstance(value, (int, str)) or value is None
        if value is None:
            self._max_rating = 0
        else:
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

    @property
    def friend_of_count(self):
        """
        Integer. Amount of users who have this user in friends.

        :return: Amount of users who have this user in friends, or None if not initialized
        :rtype: int
        """
        return self._friend_of_count
    
    @friend_of_count.setter
    def friend_of_count(self, value):
        """
        Integer. Amount of users who have this user in friends.

        :param value: Amount of users who have this user in friends
        :type value: int
        """
        assert isinstance(value, int) or value is None
        self._friend_of_count = value

    @property
    def title_photo(self):
        """
        String. User's avatar URL.
        
        :return User's avatar URL, or None if not initialized
        :rtype: str
        """
        return self._title_photo
    
    @title_photo.setter
    def title_photo(self, value):
        """
        String. User's avatar URL.

        :param value: User's avatar URL.
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._title_photo = value

    @property
    def avatar(self):
        """
        String. User's title photo URL.

        :return String. User's title photo URL, or None if not initialized.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        """
        String. User's title photo URL.

        :param value: User's title photo URL.
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._avatar = value
    
