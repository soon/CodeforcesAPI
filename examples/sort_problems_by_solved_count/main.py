#!/usr/bin/env python3
"""
In this example we are loading only Div2.C problems, sorted by solved count
"""

from collections import defaultdict
from itertools import groupby

from api import CodeforcesAPI
from api import Problem
from api import Contest


def first_or_default(lst, f):
    return next(filter(f, lst), None)


def get_contest_id(x):
    assert isinstance(x, (Problem, Contest))

    if isinstance(x, Problem):
        return x.contest_id
    else:
        return x.id


def group_by_contest_id(iterable):
    res = defaultdict(list)

    for k, vs in groupby(iterable, get_contest_id):
        res[k].extend(vs)

    return res


def make_url(problem):
    return 'http://codeforces.com/contest/{}/problem/{}'.format(problem.contest_id, problem.index)


def filter_div2(iterable):
    return filter(lambda contest: 'Div. 2' in contest.name, iterable)


def filter_c(iterable):
    return filter(lambda problem: 'C' in problem.index, iterable)


def main():
    api = CodeforcesAPI()

    print('Loading contests...')
    contests = group_by_contest_id(filter_div2(api.contest_list()))

    print('Loaded {} Div.2 contests'.format(len(contests)))

    print('Loading problemset...')
    problemset = api.problemset_problems()

    stats = problemset['problemStatistics']
    stats = filter_c(stats)
    stats = filter(lambda s: s.contest_id in contests, stats)
    stats = sorted(stats, key=lambda s: s.solved_count)

    problems = group_by_contest_id(filter_c(problemset['problems']))

    print()
    print('{:30}{:15}{}'.format('Name', 'Solved count', 'Url'))

    for stat in stats[:10]:
        problem = problems[stat.contest_id][0]
        print('{:30}{:<15}{}'.format(problem.name, stat.solved_count, make_url(problem)))


if __name__ == '__main__':
    main()