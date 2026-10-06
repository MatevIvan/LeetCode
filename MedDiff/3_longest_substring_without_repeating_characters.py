from dataclasses import dataclass

@dataclass
class TestCase:
  string: str
  solution: int


def lengthOfLongestSubstring(s: str) -> int:
  """
  Given a string s, find the length of the longest substring without duplicate characters.
  """
  characters = list(s)
  longest_subset = 0
  left = 0

  for right in range(len(s)):
    seen_characters = set()

    for char in characters[left:right+1]:
      if char not in seen_characters:
        seen_characters.add(char)
      else:
        left+=1

    if longest_subset < right - left +1:
      longest_subset = right-left +1

  return longest_subset

def runTests():
  cases = [
    TestCase("", 0),
    TestCase("a", 1),
    TestCase("abcabcbb", 3),
    TestCase("bbbbb", 1),
    TestCase("pwwkew", 3),
  ]

  for case in cases:
    actual = lengthOfLongestSubstring(case.string)
    passed = actual == case.solution
    if not passed:
      print(f"failed case '{case.string}', expected: {case.solution}, got: {actual}\n")
  return

runTests()