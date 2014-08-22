#!/usr/bin/env python3

"""
In this example we are loading last N submissions
"""

import os
import sys

from codeforces.api import CodeforcesAPI


def main(argv):
    api = CodeforcesAPI()

    count_submissions = int(argv[1])

    submissions = api.problemset_recent_status(count_submissions)

    print('{:^20}{}'.format('Submission ID', 'Party members'))

    for s in submissions:
        print('{:^20}{}'.format(s.id, ', '.join(member.handle for member in s.author.members)))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print("Invalid number of arguments")
        print("Usage: python {} [contest id]".format(os.path.basename(sys.argv[0])))