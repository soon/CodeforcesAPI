#!/usr/bin/env python3

"""
In this example we are counting successful submissions of specified contest
"""

import os
import plotly.plotly as py
from plotly.graph_objs import *
import sys

from codeforces.api import CodeforcesAPI
from codeforces.api import VerdictType
from codeforces.api import ParticipantType

from collections import Counter


def filter_only_contestants(submissions):
    return filter(lambda s: s.author.participant_type == ParticipantType.contestant, submissions)


def get_submissions(contest_id):
    api = CodeforcesAPI()

    return filter_only_contestants(api.contest_status(contest_id))


def get_submission_count(contest_id, period=60):
    submissions_count = Counter()
    successful_submission_count = Counter()

    for s in get_submissions(contest_id):
        submissions_count[s.relative_time // period] += 1
        if s.verdict == VerdictType.ok:
            successful_submission_count[s.relative_time // period] += 1

    return submissions_count, successful_submission_count


def get_x_y_plot_data(counter):
    x, y = [], [0]
    for time, count in sorted(counter.items()):
        x.append(time)
        y[-1] += count
        y.append(y[-1])

    return x, y


def create_layout(title):
    return Layout(
        title=title,
        barmode='group',
        boxmode='overlay',
        yaxis=YAxis(
            title='Submissions'
        ),
        xaxis=XAxis(
            title='Minutes'
        )
    )


def create_scatter(x, y, name, line_color):
    return Scatter(
        x=x,
        y=y,
        name=name,
        fill='tozeroy',
        line=Line(
            color=line_color
        )
    )


def create_scatter_for_counter(counter, name, line_color):
    x, y = get_x_y_plot_data(counter)
    return create_scatter(x, y, name, line_color)


def main(argv):
    contest_id = int(argv[1])

    print('Loading submissions...')
    submissions_count, successful_submission_count = get_submission_count(contest_id)
    print('Submissions loaded')

    scatters = [create_scatter_for_counter(submissions_count,
                                           'All submissions',
                                           'rgb(255, 102, 0)'),
                create_scatter_for_counter(successful_submission_count,
                                           'Successful submissions',
                                           'rgb(0, 178, 0)')]

    data = Data(scatters)
    layout = create_layout('Contest #{} / Submissions'.format(contest_id))

    py.sign_in('Python-Demo-Account', 'gwt101uhh0')

    fig = Figure(data=data, layout=layout)
    py.plot(fig, filename='contest_{}_submissions'.format(contest_id))
    py.image.save_as(fig, 'awesome_image.png')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print("Invalid number of arguments")
        print("Usage: python {} [contest id]".format(os.path.basename(sys.argv[0])))