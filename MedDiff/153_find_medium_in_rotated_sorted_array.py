from dataclasses import dataclass
from math import inf


@dataclass
class TestCase:
    id: int
    nums: list[int]
    solution: int


def findMin(nums: list[int]) -> int:
    """
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
    For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]]
    1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

    Given the sorted rotated array nums of unique elements, return the minimum element of this array.

    You must write an algorithm that runs in O(log n) time.
    """
    if nums[0] <= nums[-1]:
        return nums[0]

    lowest_num = nums[-1]
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if nums[mid] > lowest_num:
            low = mid + 1
        else:
            high = mid - 1
            lowest_num = nums[mid]

    return lowest_num


def AIfindMin(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        # The minimum lies to the right of mid only in this case.
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


def runTests():
    test_cases = [
        TestCase(1, [3, 4, 5, 1, 2], 1),
        TestCase(2, [4, 5, 6, 7, 0, 1, 2], 0),
        TestCase(3, [11, 13, 15, 17], 11),
        TestCase(4, [2, 1], 1),
    ]
    failed = 0
    for case in test_cases:
        answer = findMin(case.nums)
        if answer != case.solution:
            failed += 1
            print(f"failed test '{case.id}': want: {case.solution}, got: {answer}")
        answer = AIfindMin(case.nums)
        if answer != case.solution:
            failed += 1
            print(f"failed AI test '{case.id}': want: {case.solution}, got: {answer}")
    if failed == 0:
        print("completed tests with no failures")
    return


runTests()
