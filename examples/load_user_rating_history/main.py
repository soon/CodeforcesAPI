#!/usr/bin/env python3

"""
In this example we are loading users rating history by it's handle
"""

import os
import sys

from codeforces import CodeforcesAPI


def main(argv):
    api = CodeforcesAPI()

    handle = argv[1]

    rating_changes = list(api.user_rating(handle))

    print('Rating history for {}:'.format(handle))
    for rating in rating_changes:
        print(rating.old_rating, end=' -> ')

    print(rating_changes[-1].new_rating)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print("Invalid number of arguments")
        print("Usage: python {} [contest id]".format(os.path.basename(sys.argv[0])))