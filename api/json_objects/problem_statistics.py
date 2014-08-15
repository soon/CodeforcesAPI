"""
This module contains classes for representing ProblemStatistics object

For further information visit http://codeforces.com/api/help/objects#ProblemStatistics
"""

from . import BaseJsonObject


class ProblemStatistics(BaseJsonObject):
    """
    This class represents ProblemStatistics object

    For further information visit http://codeforces.com/api/help/objects#ProblemStatistics
    """

    def __init__(self, s=None):
        self._contest_id = None
        self._index = None
        self._solved_count = None

        super().__init__(s)

    def load_from_dict(self, values):
        try:
            self.contest_id = values['contestId']
            self.index = values['index']
            self.solved_count = values['solvedCount']
        except KeyError as e:
            raise ValueError('Missed required field', e.args[0])

    @property
    def contest_id(self):
        return self._contest_id 
    
    @contest_id.setter
    def contest_id(self, value):
        assert isinstance(value, (int, str))
        
        if isinstance(value, str):
            value = int(value)
            
        self._contest_id = value
        
    @property
    def index(self):
        return self._index
    
    @index.setter
    def index(self, value):
        assert isinstance(value, str)
        self._index = value

    @property
    def solved_count(self):
        return self._solved_count

    @solved_count.setter
    def solved_count(self, value):
        assert isinstance(value, (int, str))

        if isinstance(value, str):
            value = int(value)

        self._solved_count = value
