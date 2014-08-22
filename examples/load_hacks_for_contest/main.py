#!/usr/bin/env python3

"""
In this example we are loading hacks for contest by it's id
"""

import os
import sys

from codeforces import CodeforcesAPI


def main(argv):
    api = CodeforcesAPI()

    contest_id = int(argv[1])

    hacks = api.contest_hacks(contest_id)

    for h in hacks:
        print("[{:^30}] hacked [{:^30}], verdict: {}".format(', '.join(member.handle for member in h.hacker.members),
                                                             ', '.join(member.handle for member in h.defender.members),
                                                             h.verdict.value))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print("Invalid number of arguments")
        print("Usage: python {} [contest id]".format(os.path.basename(sys.argv[0])))