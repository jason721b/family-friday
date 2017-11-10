import random


# TODO: How to specify seed
def random_group(members, seed=None):
    """

    Parameters
    ----------
    members: list<any>
    seed: hashable

    Returns
    -------
    list<list<any>>

    """

    random.seed(seed)

    # If there are less than GROUP_MAX_SIZE (which is 5) people, just get one table
    if len(members) <= 5:
        return [members]

    # NOTE: If we care about performance and are willing to mutate the input `member`
    #   we can also use `random.shuffle` method
    shuffled_members = random.sample(members, len(members))

    return _split_by_group(shuffled_members)


def _split_by_group(members):
    """

    Parameters
    ----------
    members: list<any>

    Returns
    -------
    list<list<any>>

    """
    # TODO: Is there a way we don't need to hard-code the group size number
    groups = []

    # Try to split all members by 5
    for i in range(0, len(members), 5):
        groups.append(members[i:i+5])

    # Assume there are at least two groups
    assert len(groups) >= 2

    # However, last group may have less than 3 people
    last_group = groups[-1]

    # If the last group only has 1 person,
    #   we will add this person to the second last group (which has 5 people)
    #   and then split them into 2 3-people group
    if len(last_group) == 1:
        last_group = groups.pop()
        second_last_group = groups.pop()
        groups.append(second_last_group[:3])
        groups.append(second_last_group[3:] + last_group)

    # Similarly, if the last group only has 2 people,
    #   we will add these 2 people to the second last group (which has 5 people)
    #   and then split them into one 4-people and one 3-people group
    elif len(last_group) == 2:
        last_group = groups.pop()
        second_last_group = groups.pop()
        groups.append(second_last_group[:4])
        groups.append(second_last_group[4:] + last_group)

    return groups

