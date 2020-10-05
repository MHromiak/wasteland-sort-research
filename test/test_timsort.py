import pytest
# import os, sys
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')
from other_sorts import timsort as ts

def test_timsort_already_sorted():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ts.timSort(nums)
    assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_timsort_out_of_order():
    nums = [10, 9, 7, 4, 6, 2, 1, 5, 8, 3]
    ts.timSort(nums)
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == nums

def test_timsort_size_more_than_run():
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
            21,66,23,24,25,26,27,28,29,30,31,32,33]
    ts.timSort(nums)
    assert [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
            21,23,24,25,26,27,28,29,30,31,32,33,66] == nums

def test_timsort_empty():
    nothing = []
    ts.timSort(nothing)
    assert [] == nothing

##Helpers##

def test_timsort_insertion_already_sorted():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ts.insertionSort(nums, 0, len(nums) - 1)
    assert nums == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_timsort_insertion_out_of_order():
    nums = [10, 9, 7, 4, 6, 2, 1, 5, 8, 3]
    ts.insertionSort(nums, 0, len(nums) - 1)
    assert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == nums

def test_timsort_insertion_empty():
    nothing = []
    ts.insertionSort(nothing, 0, len(nothing) - 1)
    assert [] == nothing


def test_timsort_merge_nonempty_more_left():
    nums = [2,6,7,1,5]
    ts.merge(nums, 0, 2, 4)
    assert nums == [1,2,5,6,7]

def test_timsort_merge_nonempty_more_right():
    nums = [2,6,7,1,5,8,9]
    ts.merge(nums, 0, 2, 5)
    assert nums == [1,2,5,6,7,8, 9]

def test_timsort_merge_empty():
    nums = []
    ts.merge(nums, 0, 0, 0)
    assert nums == []