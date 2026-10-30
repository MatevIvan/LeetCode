from dataclasses import dataclass
import heapq


@dataclass
class TestCase:
    id: int
    stones: list[int]
    solution: int


def lastStoneWeight(stones: list[int]) -> int:
    index = len(stones) - 1

    while index > 0:
        stones.sort()
        stone1 = stones.pop(-1)
        stone2 = stones.pop(-1)
        result = abs(stone1 - stone2)

        if result:
            stones.append(result)
            index -= 1
        else:
            index -= 2

    return stones[0] if stones else 0


# gpt-5.6_terra_medium
def AIlastStoneWeight(stones: list[int]) -> int:
    heap = [-stone for stone in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        heaviest = -heapq.heappop(heap)
        next_heaviest = -heapq.heappop(heap)
        if heaviest != next_heaviest:
            heapq.heappush(heap, next_heaviest - heaviest)

    return -heap[0] if heap else 0


def runTests():
    test_cases = [
        TestCase(1, [2, 7, 4, 1, 8, 1], 1),
        TestCase(2, [1], 1),
        TestCase(3, [2, 2], 0),
    ]
    failed = 0

    for case in test_cases:
        answer = lastStoneWeight(case.stones)
        if answer != case.solution:
            failed += 1
            print(f"failed case '{case.id}': want: {case.solution}, got: {answer}")
        answer = AIlastStoneWeight(case.stones)
        if answer != case.solution:
            failed += 1
            print(f"failed AI case '{case.id}': want: {case.solution}, got: {answer}")

    if not failed:
        print("completed tests with no failures")
    return


runTests()
