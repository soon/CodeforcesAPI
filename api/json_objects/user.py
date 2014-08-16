"""
This file provides class for representing User object

For further information visit http://codeforces.com/api/help/objects#User
"""

from . import BaseJsonObject


__all__ = ['User']


class User(BaseJsonObject):
    """
    This class represents User object

    For further information visit http://codeforces.com/api/help/objects#User
    """

    def __init__(self, s=None):
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

        super().__init__(s)

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
        return self._handle

    @handle.setter
    def handle(self, value):
        assert isinstance(value, str)
        self._handle = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        assert isinstance(value, str) or value is None
        self._email = value

    @property
    def vk_id(self):
        return self._vk_id

    @vk_id.setter
    def vk_id(self, value):
        assert isinstance(value, str) or value is None
        self._vk_id = value

    @property
    def open_id(self):
        return self._open_id

    @open_id.setter
    def open_id(self, value):
        assert isinstance(value, str) or value is None
        self._open_id = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        assert isinstance(value, str) or value is None
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        assert isinstance(value, str) or value is None
        self._last_name = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        assert isinstance(value, str) or value is None
        self._country = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        assert isinstance(value, str) or value is None
        self._city = value

    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, value):
        assert isinstance(value, str) or value is None
        self._organization = value

    @property
    def contribution(self):
        return self._contribution

    @contribution.setter
    def contribution(self, value):
        assert isinstance(value, (int, str))
        self._contribution = int(value)

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        assert isinstance(value, str)
        self._rank = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        assert isinstance(value, (int, str))
        self._rating = int(value)

    @property
    def max_rank(self):
        return self._max_rank

    @max_rank.setter
    def max_rank(self, value):
        assert isinstance(value, str)
        self._max_rank = value

    @property
    def max_rating(self):
        return self._max_rating

    @max_rating.setter
    def max_rating(self, value):
        assert isinstance(value, (int, str))
        self._max_rating = int(value)

    @property
    def last_online_time(self):
        return self._last_online_time

    @last_online_time.setter
    def last_online_time(self, value):
        assert isinstance(value, (int, str))
        self._last_online_time = int(value)

    @property
    def registration_time(self):
        return self._registration_time

    @registration_time.setter
    def registration_time(self, value):
        assert isinstance(value, (int, str))
        self._registration_time = int(value)
