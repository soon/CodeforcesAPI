"""
This module contains classes for representing Contest object

For further information visit http://codeforces.com/api/help/objects#Contest
"""

from enum import Enum
from . import BaseJsonObject


__all__ = ['Contest', 'ContestType', 'ContestPhase']


class ContestType(Enum):
    cf = 'CF'
    ioi = 'IOI'
    icpc = 'ICPC'


class ContestPhase(Enum):
    before = 'BEFORE'
    coding = 'CODING'
    pending_system_test = 'PENDING_SYSTEM_TEST'
    system_test = 'SYSTEM_TEST'
    finished = 'FINISHED'


class Contest(BaseJsonObject):
    """
    Represents a contest on Codeforces.

    For further information visit http://codeforces.com/api/help/objects#Contest
    """

    def __init__(self, data=None):
        self._id = None
        self._name = None
        self._type = None
        self._phase = None
        self._frozen = None
        self._duration = None
        self._start_time = None
        self._relative_time = None
        self._prepared_by = None
        self._website_url = None
        self._description = None
        self._difficulty = None
        self._kind = None
        self._icpc_region = None
        self._country = None
        self._city = None
        self._season = None

        super().__init__(data)

    def __repr__(self):
        return '<Contest: {}>'.format(self.id)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.id = values['id']
        self.name = values['name']
        self.type = values['type']
        self.phase = values['phase']
        self.frozen = values['frozen']
        self.duration = values['durationSeconds']

    def load_optional_fields_from_dict(self, values):
        super().load_optional_fields_from_dict(values)

        self.start_time = values.get('startTimeSeconds')
        self.relative_time = values.get('relativeTimeSeconds')
        self.prepared_by = values.get('preparedBy')
        self.website_url = values.get('websiteUrl')
        self.description = values.get('description')
        self.difficulty = values.get('difficulty')
        self.kind = values.get('kind')
        self.icpc_region = values.get('icpcRegion')
        self.country = values.get('country')
        self.city = values.get('city')
        self.season = values.get('season')

    @property
    def id(self):
        """
        :return: ID or None if not initialized
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, value):
        """
        :param value: ID
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._id = int(value)

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
        :return: Scoring system used for the contest or None if not initialized
        :rtype: ContestType
        """
        return self._type

    @type.setter
    def type(self, value):
        """
        :param value: Scoring system used for the contest.
        :type value: ContestType or str
        """
        assert isinstance(value, (ContestType, str))
        self._type = ContestType(value)

    @property
    def phase(self):
        """
        :return: Phase or None if not initialized
        :rtype: ContestPhase
        """
        return self._phase

    @phase.setter
    def phase(self, value):
        """
        :param value: Phase
        :type value: ContestPhase or str
        """
        assert isinstance(value, (ContestPhase, str))
        self._phase = ContestPhase(value)

    @property
    def frozen(self):
        """
        If true, then the ranklist for the contest is frozen and shows only submissions, created before freeze.

        :return: If ranklist is frozen or None if not initialized
        :rtype: bool
        """
        return self._frozen

    @frozen.setter
    def frozen(self, value):
        """
        If true, then the ranklist for the contest is frozen and shows only submissions, created before freeze.

        :param value: If ranklist is frozen
        :type value: bool or str
        """
        assert isinstance(value, (bool, str))
        self._frozen = bool(value)

    @property
    def duration(self):
        """
        :return: Duration of the contest in seconds or None if not initialized
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, value):
        """
        :param value: Duration of the contest in seconds.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._duration = int(value)

    @property
    def start_time(self):
        """
        Can be absent.

        :return: Contest start time in unix format or None if not initialized or absent
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        """
        Can Be absent

        :param value: Contest start time in unix format or None if absent
        :rtype: int or str
        """
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(value)

        self._start_time = value

    @property
    def relative_time(self):
        """
        Can be absent.

        Number of seconds, passed after the start of the contest. Can be negative.

        :return: Relative time or None if not initialized or absent
        :rtype: int
        """
        return self._relative_time

    @relative_time.setter
    def relative_time(self, value):
        """
        Can be absent.

        Number of seconds, passed after the start of the contest. Can be negative.

        :param value: Relative time or None if absent
        :type value: int or str
        """
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(value)

        self._relative_time = value

    @property
    def prepared_by(self):
        """
        Can be absent.

        Handle of the user, how created the contest.

        :return: Handle or None if not initialized or absent
        :rtype: str
        """
        return self._prepared_by

    @prepared_by.setter
    def prepared_by(self, value):
        """
        Can be absent.

        Handle of the user, how created the contest.

        :param value: Handle or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._prepared_by = value

    @property
    def website_url(self):
        """
        Can be absent.

        URL for contest-related website.

        :return: URL or None if not initialized or absent
        :rtype: str
        """
        return self._website_url

    @website_url.setter
    def website_url(self, value):
        """
        Can be absent.

        URL for contest-related website.

        :param value: URL or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._website_url = value

    @property
    def description(self):
        """
        Can be absent.

        Localized.

        :return: Description or None if not initialized ot absent
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, value):
        """
        Can be absent.

        Localized.

        :param value: Description or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._description = value

    @property
    def difficulty(self):
        """
        Can be absent.

        From 1 to 5. Larger number means more difficult problems.

        :return: Difficulty or None if not initialized or absent
        :rtype: int
        """
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        """
        Can be absent.

        From 1 to 5. Larger number means more difficult problems.

        :param value: Difficulty or None if absent
        :type value: int or str
        """
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(value)

        self._difficulty = value

    @property
    def kind(self):
        """
        Can be absent. Localized.

        Human-readable type of the contest from the following categories:

            Official ACM-ICPC Contest,
            Official School Contest,
            OpenCup Contest,
            School/University/City/Region Championship,
            Training Camp Contest,
            Official International Personal Contest,
            Training Contest.

        :return: Kind or None if not initialized or absent
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, value):
        """
        Can be absent. Localized.

        Human-readable type of the contest from the following categories:

            Official ACM-ICPC Contest,
            Official School Contest,
            OpenCup Contest,
            School/University/City/Region Championship,
            Training Camp Contest,
            Official International Personal Contest,
            Training Contest.

        :param value: Kind or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._kind = value

    @property
    def icpc_region(self):
        """
        Can be absent. Localized.

        Name of the ICPC Region for official ACM-ICPC contests.

        :return: Name of the region or None if not initialized or absent
        :rtype: str
        """
        return self._icpc_region

    @icpc_region.setter
    def icpc_region(self, value):
        """
        Can be absent. Localized.

        Name of the ICPC Region for official ACM-ICPC contests.

        :param value: Name of the region or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._icpc_region = value

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
    def season(self):
        """
        Can be absent.

        :return: Season or None if not initialized or absent
        :rtype: str
        """
        return self._season

    @season.setter
    def season(self, value):
        """
        Can be absent.

        :param value: Season or None if absent
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._season = value
