"""
This module contains classes for representing Party object

For further information visit http://codeforces.com/api/help/objects#Party
"""

from enum import Enum

from . import BaseJsonObject
from . import Member


__all__ = ['ParticipantType', 'Party']


class ParticipantType(Enum):
    """
    This class represents participant type.
    """

    contestant = 'CONTESTANT'
    practice = 'PRACTICE'
    virtual = 'VIRTUAL'
    manager = 'MANAGER'
    out_of_competition = 'OUT_OF_COMPETITION'


class Party(BaseJsonObject):
    """
    This class represents Party object

    For further information visit http://codeforces.com/api/help/objects#Party
    """

    def __init__(self, data=None):
        self._contest_id = None
        self._members = None
        self._participant_type = None
        self._team_id = None
        self._team_name = None
        self._ghost = None
        self._room = None
        self.start_time = None

        super().__init__(data)

    def __repr__(self):
        return '<Party: {}>'.format(self.members)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.contest_id = values['contestId']
        self.members = values['members']
        self.participant_type = values['participantType']
        self.ghost = values['ghost']

    def load_optional_fields_from_dict(self, values):
        super().load_optional_fields_from_dict(values)

        self.team_id = values.get('teamId')
        self.team_name = values.get('teamName')
        self.room = values.get('room')
        self.start_time = values.get('startTimeSeconds')

    @property
    def contest_id(self):
        """
        :return: Id of the contest, in which party is participating or None if not initialized
        :rtype: int
        """
        return self._contest_id

    @contest_id.setter
    def contest_id(self, value):
        """
        :param value: Id of the contest, in which party is participating.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._contest_id = int(value)

    @property
    def members(self):
        """
        :return: List of Member objects. Members of the party or None if not initialized
        :rtype: list of Member
        """
        return self._members

    @members.setter
    def members(self, value):
        """
        :param value: List of Member objects. Members of the party.
        :type value: list of Member objects or list of dict or list of str
        """
        assert isinstance(value, list)

        if len(value) > 0:
            assert isinstance(value[0], (Member, dict, str))

            if not isinstance(value[0], Member):
                value = list(map(Member, value))

        self._members = value

    @property
    def participant_type(self):
        """
        :return: Participant type or None if not initialized
        :rtype: ParticipantType
        """
        return self._participant_type

    @participant_type.setter
    def participant_type(self, value):
        """
        :param value: Participant type
        :type value: ParticipantType or str
        """
        assert isinstance(value, (ParticipantType, str))
        self._participant_type = ParticipantType(value)

    @property
    def team_id(self):
        """
        Can be absent.
        
        :return: If party is a team, then it is a unique team id. Otherwise, this field is absent.
                 Returns None if not initialized or absent
        :rtype: int
        """
        return self._team_id

    @team_id.setter
    def team_id(self, value):
        """
        Can be absent.
        
        :param value: If party is a team, then it is a unique team id. Otherwise, this field is absent.
        :type value: int or str or None
        """
        assert isinstance(value, (int, str)) or value is None
        
        if isinstance(value, str):
            value = int(str)
            
        self._team_id = value
        
    @property
    def team_name(self):
        """
        Can be absent.
        Localized.

        :return: If party is a team or ghost, then it is a localized name of the team. Otherwise, it is absent.
                 Returns None if not initialized or absent
        :rtype: str
        """
        return self._team_name
    
    @team_name.setter
    def team_name(self, value):
        """
        Can be absent.
        Localized.

        :param value: If party is a team or ghost, then it is a localized name of the team. Otherwise, it is absent.
        :type value: str or None
        """
        assert isinstance(value, str) or value is None
        self._team_name = value

    @property
    def ghost(self):
        """
        :return: If true then this party is a ghost. It participated in the contest, but not on Codeforces.
                 For example, Andrew Stankevich Contests in Gym has ghosts of the participants from
                 Petrozavodsk Training Camp.
                 Returns None if not initialized
        :rtype: bool
        """
        return self._ghost

    @ghost.setter
    def ghost(self, value):
        """
        :param value: If true then this party is a ghost. It participated in the contest, but not on Codeforces.
                      For example, Andrew Stankevich Contests in Gym has ghosts of the participants from
                      Petrozavodsk Training Camp.
        :type value: bool or str
        """
        assert isinstance(value, (str, bool))
        self._ghost = bool(value)

    @property
    def room(self):
        """
        Can be absent.

        :return: Room of the party. If absent, then the party has no room. Returns None if not initialized or absent
        :rtype: int
        """
        return self._room

    @room.setter
    def room(self, value):
        """
        Can be absent.

        :param value: Room of the party. If absent, then the party has no room.
        :type value: int or str or None
        """
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(str)

        self._room = value

    @property
    def start_time(self):
        """
        Can be absent.

        :return: Time, when this party started a contest. Returns None if not initialized or absent
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        """
        Can be absent.

        :param value: Time, when this party started a contest.
        :type value: int or str or None
        """
        assert isinstance(value, (int, str)) or value is None

        if isinstance(value, str):
            value = int(str)

        self._start_time = value
