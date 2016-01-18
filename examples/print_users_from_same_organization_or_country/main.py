#!/usr/bin/env python3

from codeforces import CodeforcesAPI


def get_all_user_handles(ranklist_rows):
    return set(m.handle for row in ranklist_rows for m in row.party.members)


def filter_by_organization(ranklist_row, handle_to_user_mapping, organization):
    return (r for r in ranklist_row if handle_to_user_mapping[r.party.members[0].handle].organization == organization)


def filter_by_country(ranklist_row, handle_to_user_mapping, country):
    return (r for r in ranklist_row if handle_to_user_mapping[r.party.members[0].handle].country == country)


def main():
    api = CodeforcesAPI()

    ranklist = api.contest_standings(613, count=10000)
    ranklist_rows = list(ranklist['rows'])

    users = {u.handle: u for u in api.user_info(list(get_all_user_handles(ranklist_rows)))}

    print("Users from Ural FU:")
    for row in filter_by_organization(ranklist_rows, users, "Ural FU"):
        print('    {party}, points: {points}'.format(party=row.party, points=row.points))

    print()

    print("Users from Mexico:")
    for row in filter_by_country(ranklist_rows, users, "Mexico"):
        print('    {party}, points: {points}'.format(party=row.party, points=row.points))


if __name__ == '__main__':
    main()
