"""
This file provides api for retrieving data from codeforces.com
"""

import hashlib
import json
import operator
import random
import time
from collections import OrderedDict
from enum import Enum
from urllib.error import HTTPError
from urllib.request import urlopen

from .json_objects import Contest
from .json_objects import Hack
from .json_objects import Problem
from .json_objects import ProblemStatistics
from .json_objects import RanklistRow
from .json_objects import RatingChange
from .json_objects import Submission
from .json_objects import User


__all__ = ['CodeforcesAPI', 'CodeforcesLanguage']


class CodeforcesLanguage(Enum):
    en = 'en'
    ru = 'ru'


class CodeforcesDataRetriever:
    """
    This class hides low-level operations with retrieving data from Codeforces site
    """
    def __init__(self, lang=CodeforcesLanguage.en, key=None, secret=None):
        """
        :param lang: Language
        :type lang: CodeforcesLanguage

        :param key: Private API key. Ignored if secret is None
        :type key: str

        :param secret: Private API secret. Ignored if key is None
        :type secret: str
        """
        self._key = None
        self._secret = None

        if key is not None and secret is not None:
            self.key = key
            self.secret = secret

        self._base_from_language = {
            CodeforcesLanguage.en: 'http://codeforces.com/api/',
            CodeforcesLanguage.ru: 'http://codeforces.ru/api/'
        }

        self._language = lang

    def get_data(self, method, **kwargs):
        """
        Retrieves data by given method with given parameters

        :param method: Request method
        :param kwargs: HTTP parameters
        :return:
        """
        return self.__get_data(self.__generate_url(method, **kwargs))

    def __get_data(self, url):
        """
        Returns data retrieved from given url
        """
        try:
            with urlopen(url) as req:
                return self.__check_json(req.read().decode('utf-8'))
        except HTTPError as http_e:
            try:
                return self.__check_json(http_e.read().decode('utf-8'))
            except Exception as e:
                raise e from http_e

    def __generate_url(self, method, **kwargs):
        """
        Generates request url with given method and named parameters

        :param method: Name of the method
        :type method: str
        :param kwargs: HTTP parameters
        :type kwargs: dict of [str, object]
        :return: Url
        :rtype: str
        """
        url = self.base + method

        if self.key is not None and self.secret is not None:
            kwargs['apiKey'] = self.key
            kwargs['time'] = int(time.time())

        if kwargs:
            args = self.__get_valid_args(**kwargs)
            url += '?' + '&'.join(map(self.__key_value_to_http_parameter, args.items()))

            if self.key is not None and self.secret is not None:
                url += '&apiSig=' + self.__generate_api_sig(method, args)

        return url

    def __generate_api_sig(self, method, params):
        """
        apiSig — signature to ensure that you know both key and secret.

        First six characters of the apiSig parameter can be arbitrary.
        We recommend to choose them at random for each request. Let's denote them as rand.
        The rest of the parameter is hexadecimal representation of SHA-512 hash-code of the following string:
            <rand>/<methodName>?param1=value1&param2=value2...&paramN=valueN#<secret>
        where (param_1, value_1), (param_2, value_2),..., (param_n, value_n) are all the
        request parameters (including apiKey, time, but excluding apiSig) with corresponding values,
        sorted lexicographically first by param_i, then by value_i.
        :return:
        """
        rand = str(random.randint(100000, 999999))

        s = '{}/{}?'.format(rand, method)

        ordered_params = OrderedDict(sorted(params.items(), key=operator.itemgetter(0)))

        s += '&'.join(map(self.__key_value_to_http_parameter, ordered_params.items()))

        s += '#' + self.secret

        return rand + hashlib.sha512(s.encode()).hexdigest()

    @staticmethod
    def __get_valid_args(**kwargs):
        """
        Filters only not None values
        """
        return {k: v for k, v in kwargs.items() if v is not None}

    @staticmethod
    def __key_value_to_http_parameter(key_value):
        """
        Transforms dictionary of values to http parameters
        """
        key, value = key_value

        if isinstance(value, list):
            value = ';'.join(sorted(map(str, value)))
        else:
            value = str(value)

        return '{0}={1}'.format(key, value)

    @staticmethod
    def __check_json(answer):
        """
        Check if answer is correct according to http://codeforces.com/api/help
        """
        values = json.loads(answer)

        try:
            if values['status'] == 'OK':
                return values['result']
            else:
                raise ValueError(values['comment'])
        except KeyError as e:
            raise ValueError('Missed required field', e.args[0])

    @property
    def base(self):
        """
        :return: Base of url according to language
        :rtype: str
        """
        return self._base_from_language[self.language]

    @property
    def language(self):
        """
        :returns: Language. By default is en
        :rtype: CodeforcesLanguage
        """
        return self._language

    @language.setter
    def language(self, value):
        """
        :param value: Language
        :type value: CodeforcesLanguage or str
        """
        assert isinstance(value, (CodeforcesLanguage, str))
        self._language = CodeforcesLanguage(value)

    @property
    def key(self):
        """
        The private api key

        :returns: Key or None if not presented
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, value):
        """
        The private api key

        :param value: Key or None
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._key = value

    @property
    def secret(self):
        """
        The secret part of api key

        :returns: Secret or None if not presented
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, value):
        """
        The secret part of api key

        :param value: Secret or None
        :type value: str
        """
        assert isinstance(value, str) or value is None
        self._secret = value


class CodeforcesAPI:
    """
    This class provides api for retrieving data from codeforces.com
    """

    def __init__(self, lang='en', key=None, secret=None):
        """
        :param lang: Language
        :type lang: str or CodeforcesLanguage

        :param key: Private API key. Ignored if secret is None
        :type key: str

        :param secret: Private API secret. Ignored if key is None
        :type secret: str
        """
        self._data_retriever = CodeforcesDataRetriever(CodeforcesLanguage(lang), key, secret)

    def contest_hacks(self, contest_id):
        """
        Returns list of hacks in the specified contests.

        Full information about hacks is available only after some time after the contest end.
        During the contest user can see only own hacks.

        :param contest_id: Id of the contest.
                           It is not the round number. It can be seen in contest URL. For example: /contest/374/status
        :type contest_id: int
        :return: Returns an iterator of Hack objects.
        :rtype: iterator of Hack
        """
        assert isinstance(contest_id, int)

        data = self._data_retriever.get_data('contest.hacks', contestId=contest_id)

        return map(Hack, data)

    def contest_list(self, gym=False):
        """
        Returns information about all available contests.

        :param gym: If true — than gym contests are returned. Otherwise, regular contests are returned.
        :type gym: bool
        :return: Returns an iterator of Contest objects. If this method is called not anonymously,
                 then all available contests for a calling user will be returned too,
                 including mashups and private gyms.
        :rtype: iterator of Contest
        """
        data = self._data_retriever.get_data('contest.list', gym=gym)

        return map(Contest, data)

    def contest_rating_changes(self, contest_id):
        """
        Returns rating changes after the contest.

        :param contest_id: Id of the contest. It is not the round number. It can be seen in contest URL.
        :return: Returns an iterator of RatingChange objects.
        :rtype: iterator of RatingChange
        """
        data = self._data_retriever.get_data('contest.ratingChanges', contestId=contest_id)

        return map(RatingChange, data)

    def contest_standings(self, contest_id, from_=1, count=None, handles=None, show_unofficial=False):
        """
        Returns the description of the contest and the requested part of the standings.

        :param contest_id: Id of the contest. It is not the round number. It can be seen in contest URL.
                           For example: /contest/374/status
        :type contest_id: int

        :param from_: 1-based index of the standings row to start the ranklist.
        :type from_: int

        :param count: Number of standing rows to return.
        :type count: int

        :param handles: List of handles. No more than 10000 handles is accepted.
        :type handles: list of str

        :param show_unofficial: If true than all participants (virtual, out of competition) are shown.
                                Otherwise, only official contestants are shown.
        :type show_unofficial: bool

        :return: Returns object with three fields: "contest", "problems" and "rows".
                 Field "contest" contains a Contest object.
                 Field "problems" contains an iterator of Problem objects.
                 Field "rows" contains an iteator of RanklistRow objects.
        :rtype: {'contest': Contest,
                 'problems': iterator of Problem,
                 'rows': iterator of RanklistRow}
        """
        assert isinstance(contest_id, int), 'contest_id should be of type int, not {}'.format(type(contest_id))
        assert isinstance(from_, int), 'from_ should be of type int, not {}'.format(type(from_))
        assert isinstance(count, int) or count is None, 'count should be of type int, not {}'.format(type(count))
        assert isinstance(handles, list) or handles is None, \
            'handles should be of type list of str, not {}'.format(type(handles))
        assert handles is None or len(handles) <= 10000, 'No more than 10000 handles is accepted'
        assert isinstance(show_unofficial, bool), \
            'show_unofficial should be of type bool, not {}'.format(type(show_unofficial))

        data = self._data_retriever.get_data('contest.standings',
                                             contestId=contest_id,
                                             count=count,
                                             handles=handles,
                                             showUnofficial=show_unofficial,
                                             **{'from': from_})

        return {'contest': Contest(data['contest']),
                'problems': map(Problem, data['problems']),
                'rows': map(RanklistRow, data['rows'])}

    def contest_status(self, contest_id, handle=None, from_=1, count=None):
        """
        Returns submissions for specified contest.

        Optionally can return submissions of specified user.

        :param contest_id: Id of the contest.
                           It is not the round number. It can be seen in contest URL. For example: /contest/374/status
        :type contest_id: int

        :param handle: Codeforces user handle.
        :type handle: str

        :param from_: 1-based index of the first submission to return.
        :type from_: int

        :param count: Number of returned submissions.
        :type count: int

        :return: Returns an iterator of Submission objects, sorted in decreasing order of submission id.
        :rtype: iterator of Submission
        """
        assert isinstance(contest_id, int)
        assert isinstance(handle, str) or handle is None
        assert isinstance(from_, int)
        assert isinstance(count, int) or count is None

        data = self._data_retriever.get_data('contest.status',
                                             contestId=contest_id,
                                             handle=handle,
                                             count=count,
                                             **{'from': from_})

        return map(Submission, data)

    def problemset_problems(self, tags=None):
        """
        Returns all problems from problemset. Problems can be filtered by tags.

        :param tags: List of tags.
        :type tags: list of str
        :return: Returns two iterators. Iterator of Problem objects and iterator of ProblemStatistics objects.
        :rtype: {'problems': list of Problem,
                 'problemStatistics': list of ProblemStatistics}
        """
        data = self._data_retriever.get_data('problemset.problems', tags=tags)

        return {'problems': map(Problem, data['problems']),
                'problemStatistics': map(ProblemStatistics, data['problemStatistics'])}

    def problemset_recent_status(self, count):
        """
        Returns recent submissions.

        :param count: Number of submissions to return. Can be up to 1000.
        :type count: int

        :return: Returns an iterator of Submission objects, sorted in decreasing order of submission id.
        :rtype: iterator of Submission
        """
        assert isinstance(count, int)
        assert 0 < count <= 1000

        data = self._data_retriever.get_data('problemset.recentStatus', count=count)

        return map(Submission, data)

    def user_info(self, handles):
        """
        Returns information about one or several users.

        :param handles: List of handles. No more than 10000 handles is accepted.
        :type handles: list of str
        :return: Returns an iterator of User objects for requested handles.
        :rtype: iterator of User
        """
        assert isinstance(handles, list)

        data = self._data_retriever.get_data('user.info', handles=handles)

        return map(User, data)

    def user_rated_list(self, active_only=False):
        """
        Returns the list of all rated users.

        :param active_only: If true then only users, who participated in rated contest during the last month are
                            returned. Otherwise, all users with at least one rated contest are returned.
        :type active_only: bool
        :return: Returns an iterator of User objects, sorted in decreasing order of rating.
        :rtype: iterator of User
        """
        assert isinstance(active_only, bool)

        data = self._data_retriever.get_data('user.ratedList', activeOnly=active_only)

        return map(User, data)

    def user_rating(self, handle):
        """
        Returns rating history of the specified user.

        :param handle: Codeforces user handle.
        :type handle: str

        :return: Returns an iterator of RatingChange objects for requested user.
        :rtype: iterator of RatingChange
        """
        assert isinstance(handle, str), 'Handle should have str type, not {}'.format(type(handle))

        data = self._data_retriever.get_data('user.rating', handle=handle)

        return map(RatingChange, data)

    def user_status(self, handle, from_=1, count=None):
        """
        Returns submissions of specified user.

        :param handle: Codeforces user handle.
        :type handle: str
        :param from_: 1-based index of the first submission to return
        :type from_: int
        :param count: Number of returned submissions.
        :type count: int or None
        :return: Returns an iterator of Submission objects, sorted in decreasing order of submission id.
        :rtype: iterator of Submission
        """
        assert isinstance(handle, str)
        assert isinstance(from_, int)
        assert isinstance(count, int) or count is None

        data = self._data_retriever.get_data('user.status', handle=handle, count=count, **{'from': from_})

        return map(Submission, data)
