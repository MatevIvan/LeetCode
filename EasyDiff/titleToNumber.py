# Import math as we need to use exponents
import math
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        # set the last letter to its ascii value - 64. This is the alphabetical letter value
        colNum = ord(columnTitle[-1])-64
        # i will start at the end and we will work backwards
        # we're starting from the second to last value because the first value was already computed above
        i = len(columnTitle) - 2
        # j will count the exp power
        j = 1
        # we are working backwards to the 0th term
        while i >= 0:
            # letterValue * 26 ^ j
            # The longer the string is, the larger the value of the first letter 
            temp = (ord(columnTitle[i]) - 64) * math.pow(26,j)
            # add the value to the column number value
            colNum += temp
            # decrease i since we are working backwards
            i -= 1
            # increase j to make the exponential power larger
            j += 1
        # return the colNum value as an int
        return int(colNum)

# Test the Code
solutionInst = Solution()
print(solutionInst.titleToNumber("Z")) # 26
print(solutionInst.titleToNumber("AA")) # 1*26   +  1 =  27
print(solutionInst.titleToNumber("BA")) # 2*26   +  1 =  53
print(solutionInst.titleToNumber("ZY")) # 26*26  + 25 = 701
print(solutionInst.titleToNumber("AAA")) # 1*26*26 +  1*26 +  1 = 703
print(solutionInst.titleToNumber("AZA")) # 1*26*26 + 26*26 +  1 = 1352
print(solutionInst.titleToNumber("BAA")) # 2*26*26 +  1*26 +  1 = 1379
print(solutionInst.titleToNumber("ZZZ")) # 26*26*26 +  26*26 +  26 = 18278

