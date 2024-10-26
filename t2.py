import pytest
from m2 import sort_list

def test_sort1():
    assert sort_list([1, 4, 2, 3, 5]) == [1, 2, 3, 4, 5]


def test_sort2():
    assert sort_list([-1, 3, 0, -2, 2]) == [-2, -1, 0, 2, 3]
