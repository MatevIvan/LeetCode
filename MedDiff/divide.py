class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # This feels like a brute force approach and is therefore very inefficient 
        # (esspecially when the dividend is large and the divisor is small)
        sum = 0
        ans = -1
        # track the changes in signs
        isNegative = 1
        if dividend < 0:
            dividend = abs(dividend)
            isNegative *= -1
        if divisor < 0:
            divisor = abs(divisor)
            isNegative *= -1
        # if the divisor is 1, we only need the dividend returned
        if divisor == 1:
            return isNegative * dividend
        # use and addition approach
        while sum <= dividend:
            sum += divisor
            ans += 1
        # Return the sign change * ans
        return isNegative * ans

# test the code
solutionInst = Solution()
print(solutionInst.divide(10,2)) # 3
print(solutionInst.divide(7,-3)) # -2
print(solutionInst.divide(0,1)) # 0
print(solutionInst.divide(4,1)) # 4