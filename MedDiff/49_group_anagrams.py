from collections import defaultdict
from dataclasses import dataclass


@dataclass
class TestCase:
    id: int
    strs: list[str]
    solution: list[list[str]]


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    """
    # plan: sort letters of each word. use the sorted letters as the key in a dict

    if len(strs) == 1:
        return [strs]

    letters_map = defaultdict(list[str])

    for word in strs:
        letters = list(word)
        letters.sort()
        letters_map["".join(letters)].append(word)

    answer = []
    for _, words in letters_map.items():
        answer.append(words)

    return answer


# chatgpt 5.6 terra medium solution
def AIgroupAnagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple[int, ...], list[str]] = defaultdict(list)

    for word in strs:
        counts = [0] * 26
        for letter in word:
            counts[ord(letter) - ord("a")] += 1
        groups[tuple(counts)].append(word)

    return list(groups.values())


def runTests():
    test_cases = [
        # out of order, but still correct
        TestCase(
            1,
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        TestCase(2, [""], [[""]]),
        TestCase(3, ["a"], [["a"]]),
    ]

    for case in test_cases:
        answer = groupAnagrams(case.strs)
        if answer != case.solution:
            print(f"failed case '{case.id}', want: {case.solution}, got: {answer}")

        # AI tests
        answer = AIgroupAnagrams(case.strs)
        if answer != case.solution:
            print(f"failed case '{case.id}', want: {case.solution}, got: {answer}")
    return


runTests()
