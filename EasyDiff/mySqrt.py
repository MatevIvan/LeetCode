# This code is exremely inefficient
# I need to use binary search
class Solution(object):
    def mySqrt(self, x):
        i = 0
        while i <= x:
            if i * i == x:
                return i
            if i * i > x:
                return i - 1
            i+=1


solutionInst = Solution()
print(solutionInst.mySqrt(0))