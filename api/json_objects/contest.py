"""
This module contains classes for representing Contest object

For further information visit http://codeforces.com/api/help/objects#Contest
"""

from enum import Enum
from api import BaseJsonObject


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
    This class represents Contest object

    For further information visit http://codeforces.com/api/help/objects#Contest
    """

    def __init__(self, s=None):
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

        super().__init__(s)

    def load_from_dict(self, values):
        try:
            self.id = values['id']
            self.name = values['name']
            self.type = values['type']
            self.phase = values['phase']
            self.frozen = values['frozen']
            self.duration = values['durationSeconds']
        except KeyError as e:
            raise ValueError('Missed required field', e.args[0])

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
        return self._id

    @id.setter
    def id(self, value):
        assert isinstance(value, (int, str))

        if isinstance(value, str):
            value = int(value)

        self._id = value

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
        assert isinstance(value, (ContestType, str))

        if isinstance(value, str):
            value = ContestType(value)

        self._type = value

    @property
    def phase(self):
        return self._phase

    @phase.setter
    def phase(self, value):
        assert isinstance(value, (ContestPhase, str))

        if isinstance(value, str):
            value = ContestPhase(value)

        self._phase = value

    @property
    def frozen(self):
        return self._frozen

    @frozen.setter
    def frozen(self, value):
        assert isinstance(value, (bool, str))

        if isinstance(value, str):
            value = bool(value)

        self._frozen = value

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        assert isinstance(value, (int, str))

        if isinstance(value, str):
            value = int(value)

        self._duration = value

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(value)

        self._start_time = value

    @property
    def relative_time(self):
        return self._relative_time

    @relative_time.setter
    def relative_time(self, value):
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(value)

        self._relative_time = value

    @property
    def prepared_by(self):
        return self._prepared_by

    @prepared_by.setter
    def prepared_by(self, value):
        assert isinstance(value, str) or value is None
        self._prepared_by = value

    @property
    def website_url(self):
        return self._website_url

    @website_url.setter
    def website_url(self, value):
        assert isinstance(value, str) or value is None
        self._website_url = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        assert isinstance(value, str) or value is None
        self._description = value

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, value):
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(value)

        self._difficulty = value

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, value):
        assert isinstance(value, str) or value is None
        self._kind = value

    @property
    def icpc_region(self):
        return self._icpc_region

    @icpc_region.setter
    def icpc_region(self, value):
        assert isinstance(value, str) or value is None
        self._icpc_region = value

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
    def season(self):
        return self._season

    @season.setter
    def season(self, value):
        assert isinstance(value, str) or value is None
        self._season = value
