import pytest
# import os, sys
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')
from other_sorts import merge as m

def test_merge_already_sorted():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = m.merge_sort(nums)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_merge_out_of_order():
    nums = [10, 9, 7, 4, 6, 2, 1, 5, 8, 3]
    result = m.merge_sort(nums)
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == result

def test_merge_empty():
    nothing = []
    result = m.merge_sort(nothing)
    assert [] == result