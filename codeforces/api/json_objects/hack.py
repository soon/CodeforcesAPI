"""
This module contains classes for representing Hack object

For further information visit http://codeforces.com/api/help/objects#Hack
"""

from enum import Enum

from . import BaseJsonObject
from . import Party
from . import Problem
from . import JudgeProtocol
from codeforces.utils import lazy_property


__all__ = ['Hack', 'HackVerdictType']


class HackVerdictType(Enum):
    hack_successful = 'HACK_SUCCESSFUL'
    hack_unsuccessful = 'HACK_UNSUCCESSFUL'
    invalid_input = 'INVALID_INPUT'
    generator_incompilable = 'GENERATOR_INCOMPILABLE'
    generator_crashed = 'GENERATOR_CRASHED'
    ignored = 'IGNORED'
    testing = 'TESTING'
    other = 'OTHER'


class Hack(BaseJsonObject):
    """
    Represents a hack, made during Codeforces Round.

    For further information visit http://codeforces.com/api/help/objects#Hack
    """

    def __init__(self, data=None):
        self._id = None
        self._creation_time = None
        self._hacker = None
        self._defender = None
        self._verdict = None
        self._problem = None
        self._test = None
        self._judge_protocol = None

        super().__init__(data)

    def __repr__(self):
        return '<Hack: {}>'.format(self.id)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.id = values['id']
        self.creation_time = values['creationTimeSeconds']
        self.hacker = values['hacker']
        self.defender = values['defender']
        self.problem = values['problem']

    def load_optional_fields_from_dict(self, values):
        super().load_optional_fields_from_dict(values)

        self.verdict = values.get('verdict')
        self.test = values.get('test')
        self.judge_protocol = values.get('judgeProtocol')

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
    def creation_time(self):
        """
        :return: Hack creation time in unix format or None if not initialized
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, value):
        """
        :param value: Hack creation time in unix format.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._creation_time = int(value)

    @lazy_property
    def hacker(self):
        """
        Lazy property.

        :return: Hacker or None if not initialized
        :rtype: Party
        """
        return self._hacker

    @hacker.setter
    def hacker(self, value):
        """
        Lazy property.

        :param value: Hacker
        :type value: Party or str or dict
        """
        assert isinstance(value, (Party, str, dict))

        if not isinstance(value, Party):
            value = Party(value)

        self._hacker = value

    @lazy_property
    def defender(self):
        """
        Lazy property.

        :return: Defender or None if not initialized
        :rtype: Party
        """
        return self._defender

    @defender.setter
    def defender(self, value):
        """
        Lazy property.

        :param value: Defender
        :type value: Party or str or dict
        """
        assert isinstance(value, (Party, str, dict))

        if not isinstance(value, Party):
            value = Party(value)

        self._defender = value

    @property
    def verdict(self):
        """
        Can be absent.

        :return: Verdict or None if not initialized or absent
        :rtype: HackVerdictType
        """
        return self._verdict

    @verdict.setter
    def verdict(self, value):
        """
        Can be absent.

        :param value: Verdict
        :type value: HackVerdictType or str
        """
        assert isinstance(value, (HackVerdictType, str)) or value is None

        if isinstance(value, str):
            value = HackVerdictType(value)

        self._verdict = value

    @lazy_property
    def problem(self):
        """
        Lazy property.

        :return: Hacked problem or None if not initialized
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, value):
        """
        Lazy property.

        :param value: Hacked problem
        :type value: Problem or str or dict
        """
        assert isinstance(value, (Problem, str, dict))

        if not isinstance(value, Problem):
            value = Problem(value)

        self._problem = value

    @property
    def test(self):
        """
        Can be absent

        :return: Test or None if not initialized or absent
        :rtype: str
        """
        return self._test

    @test.setter
    def test(self, value):
        """
        Can be absent

        :param value: Test
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._test = value

    @lazy_property
    def judge_protocol(self):
        """
        Can be absent.
        Lazy property.

        :return: Judge protocol or None if not initialized or absent
        :rtype: JudgeProtocol
        """
        return self._judge_protocol

    @judge_protocol.setter
    def judge_protocol(self, value):
        """
        Can be absent.
        Lazy property.

        :param value: Judge protocol
        :type value: JudgeProtocol or str or dict
        """
        assert isinstance(value, (JudgeProtocol, str, dict)) or value is None

        if isinstance(value, (str, dict)):
            value = JudgeProtocol(value)

        self._judge_protocol = value
