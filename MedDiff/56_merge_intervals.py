from dataclasses import dataclass


@dataclass
class TestCase:
    id: int
    intervals: list[list[int]]
    solution: list[list[int]]


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    Given an array of intervals where intervals[i] = [starti, endi],
    merge all overlapping intervals, and return an array of the
    non-overlapping intervals that cover all the intervals in the input.
    """
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    index = 1

    while index < len(sorted_intervals):
        prev_start = sorted_intervals[index - 1][0]
        prev_end = sorted_intervals[index - 1][1]
        current_start = sorted_intervals[index][0]
        current_end = sorted_intervals[index][1]
        # print(f"\nprev: {prev_start}, {prev_end}\ncur: {current_start}, {current_end}")

        # does the current start fall in the previous range?
        if (current_start >= prev_start) and (current_start <= prev_end):
            if current_end >= prev_end:
                sorted_intervals[index - 1][1] = current_end
                sorted_intervals.pop(index)
            elif current_end < prev_end:
                sorted_intervals.pop(index)
            else:
                index += 1
        else:
            index += 1

    return sorted_intervals


def AImerge(intervals: list[list[int]]) -> list[list[int]]:
    merged: list[list[int]] = []

    for start, end in sorted(intervals):
        # Start a new range only when it cannot overlap the previous one.
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return merged


def runTests():
    test_cases = [
        TestCase(1, [[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        TestCase(2, [[1, 4], [4, 5]], [[1, 5]]),
        TestCase(3, [[4, 7], [1, 4]], [[1, 7]]),
        TestCase(4, [[1, 2]], [[1, 2]]),
        TestCase(5, [[1, 4], [1, 4]], [[1, 4]]),
        TestCase(6, [[1, 4], [2, 3]], [[1, 4]]),
    ]

    for case in test_cases:
        answer = merge(case.intervals)
        if answer != case.solution:
            print(
                f"failed case '{case.id}',\n want:\t {case.solution},\n got:\t {answer}"
            )
    return


runTests()
