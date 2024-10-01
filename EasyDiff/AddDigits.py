class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # This is my very direct approach
        # type cast the number to a string to be able to itterate over it and also access the len function
        strNum = str(num)
        tempNum = 0
        longNum = True
        # do the inner loop while the number is longer than 1 digit
        while longNum:
            for n in strNum:
                tempNum += int(n)
            if len(str(tempNum)) > 1:
                # set the strNum to the tempNum as we prepare to run the loop again
                strNum = str(tempNum)
                tempNum = 0
            else:
                longNum = False
        return tempNum
    
        # This code was a solution on leet code.
        # How did they figure out that we're just looking for (num % 9)
        # if num == 0 : return 0
        # if num % 9 == 0 : return 9
        # else : return (num % 9)  

solutionInst = Solution()
print(solutionInst.addDigits(131)) # 5
print(solutionInst.addDigits(38)) # 2
print(solutionInst.addDigits(0)) # 0