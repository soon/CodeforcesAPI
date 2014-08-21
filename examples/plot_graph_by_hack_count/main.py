#!/usr/bin/env python3

"""
In this example we are loading hacks for contest by it's id and plotting a graph
"""

import os
import plotly.plotly as py
from plotly.graph_objs import *
import sys

from api import CodeforcesAPI
from api import HackVerdictType

from collections import defaultdict
from collections import Counter


def create_bar(x, y, name, color):
    return Bar(
        x=x,
        y=y,
        name=name,
        marker=Marker(
            color=color
        )
    )


def group_hacks_by_verdict(hacks):
    res = defaultdict(list)

    for h in hacks:
        res[h.verdict].append(h)

    return res


def get_hacks_count_by_problem(hacks, problem_indices):
    c = Counter(h.problem.index for h in hacks)

    for i in problem_indices:
        if i not in c:
            c[i] = 0

    return c


def get_verdict_order(verdict):
    return {
        HackVerdictType.hack_successful: 0,
        HackVerdictType.hack_unsuccessful: 1,
        HackVerdictType.invalid_input: 2,
        HackVerdictType.ignored: 3,
        HackVerdictType.generator_crashed: 4,
        HackVerdictType.generator_incompilable: 5,
        HackVerdictType.testing: 6,
        HackVerdictType.other: 7
    }[verdict]


def get_verdict_human_readable(verdict):
    return {
        HackVerdictType.hack_successful: "Successful",
        HackVerdictType.hack_unsuccessful: "Unsuccessful",
        HackVerdictType.invalid_input: "Invalid input",
        HackVerdictType.ignored: "Ignored",
        HackVerdictType.generator_crashed: "Generator crashed",
        HackVerdictType.generator_incompilable: "Generator incompilable",
        HackVerdictType.testing: "Testing",
        HackVerdictType.other: "Other"
    }[verdict]


def get_verdict_color(verdict):
    return {
        HackVerdictType.hack_successful: "#084B5B",
        HackVerdictType.hack_unsuccessful: "#D35E60",
        HackVerdictType.invalid_input: "#808585",
        HackVerdictType.ignored: "#AB6857",
        HackVerdictType.generator_crashed: "#703333",
        HackVerdictType.generator_incompilable: "#C94D4D",
        HackVerdictType.testing: "#7293CB",
        HackVerdictType.other: "#CCC210"
    }[verdict]


def load_hacks(contest_id):
    api = CodeforcesAPI()

    return api.contest_hacks(contest_id)


def load_problems(contest_id):
    api = CodeforcesAPI()

    return api.contest_standings(contest_id, count=1)['problems']


def create_layout(contest_id):
    title = 'Hack statistics for contest #{}'.format(contest_id)

    return Layout(
        title=title,
        barmode='stack',
        yaxis=YAxis(
            title='Hack count'
        ),
        xaxis=XAxis(
            title='Problem index'
        ),
        legend=Legend(
            bgcolor='#E9E9E9',
        ),
        plot_bgcolor='#F5F3F2',
        paper_bgcolor='#F5F3F2'
    )


def create_bars(hacks_count):
    """
    :param hacks_count: Hack count, grouped firstly by verdict type, secondly by problem index.
                  Should have form [(HackVerdictType, [(problem_index, hack_count)]]
    :return: iterator of Bars
    """
    return map(lambda verdict_problem_count: create_bar(x=[t[0] for t in verdict_problem_count[1]],
                                                        y=[t[1] for t in verdict_problem_count[1]],
                                                        name=get_verdict_human_readable(verdict_problem_count[0]),
                                                        color=get_verdict_color(verdict_problem_count[0])),
               hacks_count)


def plot_graph(data, contest_id):
    layout = create_layout(contest_id)
    fig = Figure(data=data, layout=layout)
    py.plot(fig, filename='contest_{}_hacks'.format(contest_id))
    return fig


def main(argv):
    contest_id = int(argv[1])

    print('Loading problems...')
    problem_indices = [problem.index for problem in load_problems(contest_id)]
    print('Problems loaded')

    print('Loading hacks...')
    hacks = load_hacks(contest_id)
    print('Hacks loaded')
    grouped_by_verdict = sorted(group_hacks_by_verdict(hacks).items(),
                                key=lambda t: get_verdict_order(t[0]),
                                reverse=True)
    grouped_by_verdict_and_problems = [
        (t[0], sorted(get_hacks_count_by_problem(t[1], problem_indices).items()))
        for t in grouped_by_verdict
    ]

    bars = create_bars(grouped_by_verdict_and_problems)

    py.sign_in('Python-Demo-Account', 'gwt101uhh0')

    data = Data(list(bars))
    fig = plot_graph(data, contest_id)
    py.image.save_as(fig, 'awesome_image.png')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print("Invalid number of arguments")
        print("Usage: python {} [contest id]".format(os.path.basename(sys.argv[0])))