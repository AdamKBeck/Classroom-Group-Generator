import os
import json
from typing import *
from random import shuffle


GROUP_PATH = os.path.join('group_generator', 'groups.json')


def load_students() -> Dict[str, Set[str]]:
    """ Converts the JSON data into a set of Person objects """
    with open(GROUP_PATH) as f:
        groups = json.load(f)

    return {k: set(v) for (k, v) in groups.items()}


def randomly_pair(IDs: List[str]) -> List[List[str]]:
    """ Randomly pairs IDs together, with one group of 3 if needed """
    cpy = IDs.copy()
    shuffle(cpy)
    pairs = [list(x) for x in zip(cpy[::2], cpy[1::2])]

    if len(IDs) % 2 != 0:
        pairs[0].append(IDs[-1])

    return pairs



def are_valid_pairings(pairs: List[List[str]], students: Dict[str, Set[str]]) -> bool:
    """ Determines if each group in the pairings are valid """

    def is_valid_pair(pair: List[str]) -> bool:
        """ Determines if a given pair (or group of 3) is valid """
        group_members = set()
        for p in pair:
            group_members.update(students[p])
        return all(p not in group_members for p in pair)

    return all(is_valid_pair(p) for p in pairs)

if __name__ == '__main__':
    students = load_students()
    random_pairs = randomly_pair(list(students.keys()))

    while not are_valid_pairings(random_pairs, students):
        random_pairs = randomly_pair(list(students.keys()))

    print(random_pairs)
