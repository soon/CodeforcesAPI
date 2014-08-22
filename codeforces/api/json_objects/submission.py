"""
This module contains classes for representing Submission object

For further information visit http://codeforces.com/api/help/objects#Submission
"""

from enum import Enum

from . import BaseJsonObject, Problem
from . import Party
from codeforces.utils import lazy_property


__all__ = ['VerdictType', 'TestsetType', 'Submission']


class VerdictType(Enum):
    """
    This class represents verdict type
    """

    failed = 'FAILED'
    ok = 'OK'
    partial = 'PARTIAL'
    compilation_error = 'COMPILATION_ERROR'
    runtime_error = 'RUNTIME_ERROR'
    wrong_answer = 'WRONG_ANSWER'
    presentation_error = 'PRESENTATION_ERROR'
    time_limit_exceeded = 'TIME_LIMIT_EXCEEDED'
    memory_limit_exceeded = 'MEMORY_LIMIT_EXCEEDED'
    idleness_limit_exceeded = 'IDLENESS_LIMIT_EXCEEDED'
    security_violated = 'SECURITY_VIOLATED'
    crashed = 'CRASHED'
    input_preparation_crashed = 'INPUT_PREPARATION_CRASHED'
    challenged = 'CHALLENGED'
    skipped = 'SKIPPED'
    testing = 'TESTING'
    rejected = 'REJECTED'


class TestsetType(Enum):
    """
    This class represents testset type
    """

    samples = 'SAMPLES'
    pretests = 'PRETESTS'
    tests = 'TESTS'
    challenges = 'CHALLENGES'
    tests1 = 'TESTS1'
    tests2 = 'TESTS2'
    tests3 = 'TESTS3'
    tests4 = 'TESTS4'
    tests5 = 'TESTS5'
    tests6 = 'TESTS6'
    tests7 = 'TESTS7'
    tests8 = 'TESTS8'
    tests9 = 'TESTS9'
    tests10 = 'TESTS10'


class Submission(BaseJsonObject):
    """
    This class represents Submission object

    For further information visit http://codeforces.com/api/help/objects#Submission
    """

    def __init__(self, data=None):
        self._id = None
        self._contest_id = None
        self._creation_time = None
        self._relative_time = None
        self._problem = None
        self._author = None
        self._programming_language = None
        self._verdict = None
        self._testset = None
        self._passed_test_count = None
        self._time_consumed = None
        self._memory_consumed = None

        super().__init__(data)

    def __repr__(self):
        return '<Submission: {}>'.format(self.id)

    def load_required_fields_from_dict(self, values):
        super().load_required_fields_from_dict(values)

        self.id = values['id']
        self.contest_id = values['contestId']
        self.creation_time = values['creationTimeSeconds']
        self.relative_time = values['relativeTimeSeconds']
        self.problem = values['problem']
        self.author = values['author']
        self.programming_language = values['programmingLanguage']
        self.testset = values['testset']
        self.passed_test_count = values['passedTestCount']
        self.time_consumed = values['timeConsumedMillis']
        self.memory_consumed = values['memoryConsumedBytes']

    def load_optional_fields_from_dict(self, values):
        super().load_optional_fields_from_dict(values)

        self.verdict = values.get('verdict')

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
    def contest_id(self):
        """
        :return: Contest ID or None if not initialized
        :rtype: int
        """
        return self._contest_id

    @contest_id.setter
    def contest_id(self, value):
        """
        :param value: Contest ID 
        :return: int or str
        """
        assert isinstance(value, (int, str))
        self._contest_id = int(value)

    @property
    def creation_time(self):
        """
        :return: Time, when submission was created, in unix-format or None if not initialized
        :rtype: int
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, value):
        """
        :param value: Time, when submission was created, in unix-format.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._creation_time = int(value)
        
    @property
    def relative_time(self):
        """
        :return: Number of seconds, passed after the start of the contest (or a virtual start for virtual parties),
                 before the submission, or None if not initialized
        :rtype: int
        """
        return self._relative_time
    
    @relative_time.setter
    def relative_time(self, value):
        """
        :param value: Number of seconds, passed after the start of the contest (or a virtual start for virtual parties),
                      before the submission.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._relative_time = int(value)

    @lazy_property
    def problem(self):
        """
        Lazy property.

        :return: Problem object or None if not initialized
        :rtype: Problem
        """
        return self._problem

    @problem.setter
    def problem(self, value):
        """
        Lazy property.

        :param value: Problem object
        :type value: Problem or dict or str
        """
        assert isinstance(value, (Problem, dict, str))

        if not isinstance(value, Problem):
            value = Problem(value)

        self._problem = value

    @lazy_property
    def author(self):
        """
        Lazy property.

        :return: Party object or None if not initialized
        :rtype: Party
        """
        return self._author

    @author.setter
    def author(self, value):
        """
        Lazy property.

        :param value: Party object
        :type value: Party or dict or str
        """
        assert isinstance(value, (Party, dict, str))

        if not isinstance(value, Party):
            value = Party(value)

        self._author = value

    @property
    def programming_language(self):
        """
        :return: Programming language or None if not initialized
        :rtype: str
        """
        return self._programming_language

    @programming_language.setter
    def programming_language(self, value):
        """
        :param value: Programming language
        :type value: str
        """
        assert isinstance(value, str)
        self._programming_language = value

    @property
    def verdict(self):
        """
        Can be absent.

        :return: Verdict or None if not initialized or absent
        :rtype: VerdictType
        """
        return self._verdict

    @verdict.setter
    def verdict(self, value):
        """
        Can be absent.

        :param value: Verdict
        :type value: VerdictType or str or None
        """
        assert isinstance(value, (VerdictType, str)) or value is None

        if isinstance(value, str):
            value = VerdictType(value)

        self._verdict = value

    @property
    def testset(self):
        """
        Testset used for judging the submission.

        :return: Testset or None if not initialized
        :rtype: TestsetType
        """
        return self._testset

    @testset.setter
    def testset(self, value):
        """
        Testset used for judging the submission.

        :param value: Testset
        :type value: TestsetType or str
        """
        assert isinstance(value, (TestsetType, str))
        self._testset = TestsetType(value)

    @property
    def passed_test_count(self):
        """
        :return: Number of passed tests or None if not initialized
        :rtype: int
        """
        return self._passed_test_count

    @passed_test_count.setter
    def passed_test_count(self, value):
        """
        :param value: Number of passed tests.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._passed_test_count = int(value)

    @property
    def time_consumed(self):
        """
        :return: Maximum time in milliseconds, consumed by solution, for one test, or None if not initialized
        :rtype: int
        """
        return self._time_consumed

    @time_consumed.setter
    def time_consumed(self, value):
        """
        :param value: Maximum time in milliseconds, consumed by solution, for one test.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._time_consumed = int(value)

    @property
    def memory_consumed(self):
        """
        :return: Maximum memory in bytes, consumed by solution, for one test, or None if not initialized
        :rtype: int
        """
        return self._memory_consumed

    @memory_consumed.setter
    def memory_consumed(self, value):
        """
        :param value: Maximum memory in bytes, consumed by solution, for one test.
        :type value: int or str
        """
        assert isinstance(value, (int, str))
        self._memory_consumed = int(value)