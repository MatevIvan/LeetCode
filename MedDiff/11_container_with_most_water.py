from dataclasses import dataclass


@dataclass
class TestClass:
    id: int
    height: list[int]
    solution: int


def maxArea(height: list[int]) -> int:
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
    of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.
    """
    # initial thoughts are to create something thats O(n^2).
    # This obviously timed out (and crashed vscode) when given a large data set

    largest_area = 0
    left_index = 0
    right_index = len(height) - 1

    while left_index < len(height) - 1:
        if right_index == left_index:
            break

        left_height = height[left_index]
        right_height = height[right_index]

        smaller_height = left_height if left_height < right_height else right_height
        area = smaller_height * (right_index - left_index)
        largest_area = area if area > largest_area else largest_area

        if smaller_height == left_height:
            left_index += 1
        else:
            right_index -= 1

    return largest_area


# chatgpt 5.6 terra medium solution
def AImaxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0

    while left < right:
        best = max(best, min(height[left], height[right]) * (right - left))

        # Only moving the shorter wall can possibly improve the area.
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1

    return best


def runTests():
    large_num = 10000
    cases = [
        TestClass(1, [1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        TestClass(2, [1, 1], 1),
        TestClass(
            3,
            list(range(0, large_num)) + list(range(large_num, -1, -1)),
            50000000,
        ),
    ]

    for case in cases:
        answer = maxArea(case.height)
        if answer != case.solution:
            print(f"failed case '{case.id}', want: {case.solution}, got: {answer}")
        answer = AImaxArea(case.height)
        if answer != case.solution:
            print(f"failed case '{case.id}', want: {case.solution}, got: {answer}")

    return


runTests()
