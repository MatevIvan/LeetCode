from dataclasses import dataclass
import heapq
from datetime import datetime


@dataclass
class TestCase:
    id: int
    nums: list[int]
    k: int
    solution: int


def findKthLargest(nums: list[int], k: int) -> int:
    """
    Given an integer array nums and an integer k, return the kth largest element in the array.

    Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Can you solve it without sorting?
    """
    largest_nums = nums[0:k]
    heapq.heapify(largest_nums)

    for index in range(k, len(nums)):
        if nums[index] > largest_nums[0]:
            heapq.heapreplace(largest_nums, nums[index])

    return largest_nums[0]


# gpt-5.6_terra_medium
def AIfindKthLargest(nums: list[int], k: int) -> int:
    values = nums[:]
    target = k - 1
    left, right = 0, len(values) - 1

    while left <= right:
        pivot = values[(left + right) // 2]
        low, high = left, right

        # Partition so larger values are on the left.
        while low <= high:
            while values[low] > pivot:
                low += 1
            while values[high] < pivot:
                high -= 1
            if low <= high:
                values[low], values[high] = values[high], values[low]
                low += 1
                high -= 1

        if target <= high:
            right = high
        elif target >= low:
            left = low
        else:
            return values[target]

    raise ValueError("k must be within the length of nums")


def runTests():
    test_cases = [
        TestCase(1, [3, 2, 1, 5, 6, 4], 2, 5),
        TestCase(2, [3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        TestCase(3, [6, 4, 5, 6, 1, 2, 3, 4, 5], 5, 4),
        TestCase(4, [3, 2], 1, 3),
        TestCase(5, [3, 2, 3, 1, 2, 4, 5, 5, 6], 9, 1),
    ]

    failed = 0

    for case in test_cases:
        answer = findKthLargest(case.nums, case.k)
        if answer != case.solution:
            failed += 1
            print(f"failed case '{case.id}': want: {case.solution}, got: {answer}")
        answer = AIfindKthLargest(case.nums, case.k)
        if answer != case.solution:
            failed += 1
            print(f"failed AI case '{case.id}': want: {case.solution}, got: {answer}")

    if failed == 0:
        print("completed tests with no failures")
    return


runTests()
