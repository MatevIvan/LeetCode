from dataclasses import dataclass
from math import floor


@dataclass
class TestCase:
    id: int
    tokens: list[str]
    solution: int


def evalRRN(tokens: list[str]) -> int:
    """
    You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
    Evaluate the expression. Return an integer that represents the value of the expression.

    Constraints:
    - 1 <= tokens.length <= 104
    - tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

    Plan:
    The calculations hinge on the location of the operators and the numbers before them.
    I will need to go back and forth around the opperator to extract the number in relation to the location of the operator.
    """

    if len(tokens) == 1:
        return int(tokens[0])

    answer = 0
    current_index = 0

    while current_index < len(tokens):
        current_token = tokens[current_index]
        if isOpperator(current_token):
            num1 = int(tokens[current_index - 2])
            num2 = int(tokens[current_index - 1])

            answer = doOpperation(num1, num2, current_token)
            # print(f"{num1} {current_token} {num2} = {answer}")

            # remove the used tokens
            tokens.pop(current_index)
            tokens.pop(current_index - 1)
            tokens[current_index - 2] = str(answer)

            current_index -= 2

        current_index += 1

    return answer


# chatgpt 5.6 terra medium solution
def AIevalRRN(tokens: list[str]) -> int:
    stack: list[int] = []

    for token in tokens:
        if token not in {"+", "-", "*", "/"}:
            stack.append(int(token))
            continue

        right = stack.pop()
        left = stack.pop()
        if token == "+":
            stack.append(left + right)
        elif token == "-":
            stack.append(left - right)
        elif token == "*":
            stack.append(left * right)
        else:
            # // rounds down, so adjust to truncate toward zero.
            quotient = abs(left) // abs(right)
            stack.append(-quotient if (left < 0) != (right < 0) else quotient)

    return stack[-1]


def isOpperator(string: str) -> bool:
    return string in ["+", "-", "*", "/"]


def doOpperation(num1: int, num2: int, opperator: str) -> int:
    match opperator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return int((num1 / num2))
    return 0


def runTests():
    test_cases = [
        TestCase(1, ["2", "1", "+", "3", "*"], 9),
        TestCase(2, ["4", "13", "5", "/", "+"], 6),
        TestCase(
            3, ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22
        ),
        TestCase(4, ["18"], 18),
    ]

    for case in test_cases:
        answer = evalRRN(case.tokens)
        if answer != case.solution:
            print(f"failed case: {case.id}, expected: {case.solution}, got: {answer}")

        # test ai solution
        answer = AIevalRRN(case.tokens)
        if answer != case.solution:
            print(f"failed case: {case.id}, expected: {case.solution}, got: {answer}")
    return


runTests()
