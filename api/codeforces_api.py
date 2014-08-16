"""
This file provides api for retrieving data from codeforces.com
"""

import json
from urllib import request

from api import Problem
from api import Hack
from api import User
from api import ProblemStatistics
from api import Contest
from api import Submission


class CodeforcesAPI:
    """
    This class provides api for retrieving data from codeforces.com
    """

    def contest_hacks(self, contest_id):
        """
        Returns list of hacks in the specified contests.

        Full information about hacks is available only after some time after the contest end.
        During the contest user can see only own hacks.

        :param contest_id: Id of the contest.
                           It is not the round number. It can be seen in contest URL. For example: /contest/374/status
        :type contest_id: int
        :return: Returns a list of Hack objects.
        :rtype: list of Hack
        """
        assert isinstance(contest_id, int)

        method = 'contest.hacks'
        url = self.__make_request_url(method, contestId=contest_id)
        data = self.__get_data(url)

        return list(map(Hack, data))

    def contest_list(self, gym=False):
        """
        Returns information about all available contests.

        :param gym: If true — than gym contests are returned. Otherwise, regular contests are returned.
        :type gym: bool
        :return: Returns a list of Contest objects. If this method is called not anonymously,
                 then all available contests for a calling user will be returned too,
                 including mashups and private gyms.
        :rtype: list of Contest
        """
        method = 'contest.list'
        url = self.__make_request_url(method, gym=gym)
        data = self.__get_data(url)

        return list(map(Contest, data))

    def contest_standings(self, contest_id, **kwargs):
        """
        Returns the description of the contest and the requested part of the standings.

        :param contest_id: Id of the contest. It is not the round number. It can be seen in contest URL.
                           For example: /contest/374/status
        :type contest_id: int
        :param kwargs:
        :return: Returns object with three fields: "contest", "problems" and "rows".
                 Field "contest" contains a Contest object.
                 Field "problems" contains a list of Problem objects.
                 Field "rows" contains a list of RanklistRow objects.
        :rtype: {'contest': Contest,
                 'problems': list of Problem,
                 'rows': list of RanklistRow}
        """

        # TODO
        # Split kwargs into optional parameters

        method = 'contest.standings'
        url = self.__make_request_url(method, contestId=contest_id, **kwargs)
        data = self.__get_data(url)

        return {'contest': list(map(Contest, data['contest'])),
                'problems': list(map(Problem, data['problems'])),
                'rows': data['rows']}

    def problemset_problems(self, tags=None):
        """
        Returns all problems from problemset. Problems can be filtered by tags.

        :param tags: List of tags.
        :type tags: list of str
        :return: Returns two lists. List of Problem objects and list of ProblemStatistics objects.
        :rtype: {'problems': list of Problem,
                 'problemStatistics': list of ProblemStatistics}
        """
        method = 'problemset.problems'
        url = self.__make_request_url(method, tags=tags)
        data = self.__get_data(url)

        return {'problems': list(map(Problem, data['problems'])),
                'problemStatistics': list(map(ProblemStatistics, data['problemStatistics']))}

    def user_info(self, handles):
        """
        Returns information about one or several users.

        :param handles: List of handles. No more than 10000 handles is accepted.
        :type handles: list of str
        :return: Returns a list of User objects for requested handles.
        :rtype: list of User
        """
        assert isinstance(handles, list)

        method = 'user.info'
        url = self.__make_request_url(method, handles=handles)
        data = self.__get_data(url)

        return list(map(User, data))

    def user_rated_list(self, active_only=False):
        """
        Returns the list of all rated users.

        :param active_only: If true then only users, who participated in rated contest during the last month are
                            returned. Otherwise, all users with at least one rated contest are returned.
        :type active_only: bool
        :return: Returns a list of User objects, sorted in decreasing order of rating.
        :rtype: list of User
        """
        assert isinstance(active_only, bool)

        method = 'user.ratedList'
        url = self.__make_request_url(method, activeOnly=active_only)
        data = self.__get_data(url)

        return list(map(User, data))

    def user_status(self, handle, from_=1, count=None):
        """
        Returns submissions of specified user.

        :param handle: Codeforces user handle.
        :type handle: str
        :param from_: 1-based index of the first submission to return
        :type from_: int
        :param count: Number of returned submissions.
        :type count: int or None
        :return: Returns a list of Submission objects, sorted in decreasing order of submission id.
        :rtype: list of Submission
        """
        assert isinstance(handle, str)
        assert isinstance(from_, int)
        assert isinstance(count, int) or count is None

        method = 'user.status'
        url = self.__make_request_url(method, handle=handle, count=count, **{'from': from_})
        data = self.__get_data(url)

        return list(map(Submission, data))

    def __get_data(self, url):
        """
        Returns data retrieved from given url
        """
        with request.urlopen(url) as req:
            return self.__check_json(req.readall().decode('utf-8'))

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

    @staticmethod
    def __get_args(**kwargs):
        """
        Filters only not None values
        """
        return {k: v for k, v in kwargs.items() if v is not None}

    @staticmethod
    def __make_request_url(method, **kwargs):
        """
        Makes request url in the form
        http://codeforces.com/api/@method?@kwargs

        :param method: Name of the method
        :param kwargs: HTTP parameters
        :return: Url
        """
        base = 'http://codeforces.com/api/'

        url = base + method

        if kwargs:
            args = CodeforcesAPI.__get_args(**kwargs)
            url += '?' + '&'.join(map(CodeforcesAPI.__key_value_to_http_parameter, args.items()))

        return url

    @staticmethod
    def __key_value_to_http_parameter(key_value):
        """
        Transforms dictionary of values to http parameters
        """
        key, value = key_value

        if isinstance(value, list):
            value = ';'.join(value)
        else:
            value = str(value)

        return '{0}={1}'.format(key, value)
