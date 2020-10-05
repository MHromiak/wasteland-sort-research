import pytest
# import os, sys
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')
from other_sorts import heapsort as hs

def test_heap_already_sorted():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    hs.heap_sort(nums)
    assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_heap_out_of_order():
    nums = [10, 9, 7, 4, 6, 2, 1, 5, 8, 3]
    hs.heap_sort(nums)
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == nums

def test_heap_empty():
    nothing = []
    hs.heap_sort(nothing)
    assert [] == nothing