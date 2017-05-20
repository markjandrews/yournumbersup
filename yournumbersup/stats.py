from itertools import chain, combinations


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(3, len(s)+1))


class CombinationCount(object):

    def __init__(self, value_set):
        self.count = 0
        self.value_set = value_set

