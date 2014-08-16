"""This file provides api for retrieving data from codeforces.com
"""

import json
from urllib import request

from api import Problem
from api import ProblemStatistics
from api.json_objects.contest import Contest


class CodeforcesAPI:
    """This class provides api for retrieving data from codeforces.com
    """
    def contest_list(self, gym=False):
        method = 'contest.list'
        url = self.__make_request_url(method, gym=gym)
        data = self.__get_data(url)

        return list(map(Contest, data))

    def contest_standings(self, contest_id, **kwargs):
        method = 'contest.standings'
        url = self.__make_request_url(method, contestId=contest_id, **kwargs)
        data = self.__get_data(url)

        return {'contest': list(map(Contest, data['contest'])),
                'problems': list(map(Problem, data['problems'])),
                'rows': data['rows']}

    def problemset_problems(self, *args):
        method = 'problemset.problems'

        url = self.__make_request_url(method, tags=args) if args else self.__make_request_url(method)

        data = self.__get_data(url)

        return {'problems': list(map(Problem, data['problems'])),
                'problemStatistics': list(map(ProblemStatistics, data['problemStatistics']))}

    def __get_data(self, url):
        with request.urlopen(url) as req:
            return self.__check_json(req.readall().decode('utf-8'))

    @staticmethod
    def __check_json(answer):
        values = json.loads(answer)

        try:
            if values['status'] == 'OK':
                return values['result']
            else:
                raise ValueError(values['comment'])
        except KeyError as e:
            raise ValueError('Missed required field', e.args[0])

    @staticmethod
    def __make_request_url(method, **kwargs):
        base = 'http://codeforces.com/api/'

        url = base + method

        if kwargs:
            url += '?' + '&'.join(map(CodeforcesAPI.__key_value_to_http_parameter, kwargs.items()))

        return url

    @staticmethod
    def __key_value_to_http_parameter(key_value):
        key, value = key_value

        if isinstance(value, list):
            value = ';'.join(value)
        else:
            value = str(value)

        return '{0}={1}'.format(key, value)
