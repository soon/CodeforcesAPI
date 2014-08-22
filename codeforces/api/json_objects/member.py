"""
This module contains classes for representing Member object

For further information visit http://codeforces.com/api/help/objects#Member
"""

from . import BaseJsonObject


__all__ = ['Member']


class Member(BaseJsonObject):
    """
    This class represents Member object

    For further information visit http://codeforces.com/api/help/objects#Member
    """

    def __init__(self, data=None):
        self._handle = None

        super().__init__(data)

    def __repr__(self):
        return '<Member: {}>'.format(self.handle)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.handle = values['handle']

    @property
    def handle(self):
        """
        :return: Codeforces user handle or None if not initialized
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, value):
        """
        :param value: Codeforces user handle.
        :type value: str
        """
        assert isinstance(value, str)
        self._handle = value
