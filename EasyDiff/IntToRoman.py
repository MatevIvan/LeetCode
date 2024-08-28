import math

class Solution(object):
    def intToRoman(self, num):
        numbers = {
            1 : "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        value = ""

        ones = num % 10
        num -= ones
        tens = num % 100
        num -= tens
        hundreds = num % 1000
        num -= hundreds
        thousands = num % 10000

solutionInst = Solution()
solutionInst.intToRoman(3944)
# print(solutionInst.intToRoman(3724))