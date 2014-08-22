"""
This module contains classes for representing JudgeProtocol object

For further information visit http://codeforces.com/api/help/objects#Hack
"""

from . import BaseJsonObject


__all__ = ['JudgeProtocol']


class JudgeProtocol(BaseJsonObject):
    """
    This class represents JudgeProtocol object

    For further information visit http://codeforces.com/api/help/objects#Hack
    """

    def __init__(self, data=None):
        self._manual = None
        self._protocol = None
        self._verdict = None

        super().__init__(data)

    def __repr__(self):
        return '<JudgeProtocol: {}>'.format(self.verdict)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.manual = values['manual']
        self.protocol = values['protocol']
        self.verdict = values['verdict']

    @property
    def manual(self):
        """
        :return: If test for the hack was entered manually returns True, otherwise False
                 Returns None if not initialized
        :rtype: bool
        """
        return self._manual

    @manual.setter
    def manual(self, value):
        """
        :param value: True, if test for the hack was entered manually returns True, otherwise False
        :type value: bool or str
        """
        assert isinstance(value, (bool, str))
        self._manual = bool(value)

    @property
    def protocol(self):
        """
        Localized.

        :return: Human-readable description of judge protocol or None if not initialized
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, value):
        """
        Localized.

        :param value: Human-readable description of judge protocol
        :type value: str
        """
        assert isinstance(value, str)
        self._protocol = value

    @property
    def verdict(self):
        """
        Localized.

        :return: Human-readable hack verdict or None if not initialized
        :rtype: str
        """
        return self._verdict

    @verdict.setter
    def verdict(self, value):
        """
        Localized.

        :param value: Human-readable hack verdict or None if not initialized
        :type value: str
        """
        assert isinstance(value, str)
        self._verdict = value
