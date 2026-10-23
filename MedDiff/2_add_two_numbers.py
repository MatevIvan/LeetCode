from __future__ import annotations
from dataclasses import dataclass


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next: ListNode | None = next


@dataclass
class TestCase:
    id: int
    list1: list[int]
    list2: list[int]
    solution: list[int]


def addTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each node contains a single digit.

    Add the two numbers and return the sum as a linked list.
    """
    solution = ListNode()
    current = solution
    carry = 0

    while l1 is not None or l2 is not None or carry > 0:

        val1 = l1.val if l1 is not None else 0
        val2 = l2.val if l2 is not None else 0
        sum = (val1 + val2 + carry) % 10
        carry = 1 if (val1 + val2 + carry) >= 10 else 0

        current.next = ListNode(sum)
        current = current.next

        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None

    return solution.next


# GPT-5.6_terra_medium
def AIaddTwoNumbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next

        carry, digit = divmod(total, 10)
        current.next = ListNode(digit)
        current = current.next

    return dummy.next


def listToLinkedList(values: list[int]) -> ListNode | None:
    head: ListNode | None = None
    current: ListNode | None = None

    for value in values:
        node = ListNode(value)

        if head is None:
            head = node
        else:
            assert current is not None
            current.next = node

        current = node

    return head


def linkedListToList(head: ListNode | None) -> list[int]:
    values: list[int] = []
    current: ListNode | None = head

    while current is not None:
        values.append(current.val)
        current = current.next

    return values


def runTests():
    test_cases = [
        TestCase(1, [2, 4, 3], [5, 6, 4], [7, 0, 8]),
        TestCase(2, [0], [0], [0]),
        TestCase(3, [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ]

    failed = 0

    for case in test_cases:
        list1 = listToLinkedList(case.list1)
        list2 = listToLinkedList(case.list2)
        answer = linkedListToList(addTwoNumbers(list1, list2))

        if answer != case.solution:
            failed += 1
            print(f"failed case '{case.id}', want: {case.solution}, got: {answer}")

        answer = linkedListToList(AIaddTwoNumbers(list1, list2))
        if answer != case.solution:
            failed += 1
            print(f"failed AI case '{case.id}', want: {case.solution}, got: {answer}")

    if failed == 0:
        print("completed tests with no failures")

    return


runTests()
