# Used a video for reference

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # the nth step will take the sum of the previous 2 steps' choices
        if n == 1:
            return n
        # save the preivous number of choices
        oneBefore = 1
        # track the choices from 2 steps ago
        twoBefore = 1
        choices = 0
        for i in range (2,n+1):
            # set choices to the sum of the 2 steps before
            choices = oneBefore + twoBefore
            # update the previous steps
            twoBefore = oneBefore
            oneBefore = choices            
        return choices

# test the code
solutionInst = Solution()
print(solutionInst.climbStairs(2))
print(solutionInst.climbStairs(3))
print(solutionInst.climbStairs(4))
print(solutionInst.climbStairs(5))
print(solutionInst.climbStairs(6))


# input: 4
# Logic:
# choice 1: 1 step + 1 step + 1 step + 1 step
# 
# choice 2: 2 step + 1 step + 1 step
# choice 3: 1 step + 2 step + 1 step
# choice 4: 1 step + 1 step + 2 step
# 
# choice 5: 2 step + 2 step
# output: 5
# 
# 
# input: 5
# Logic:
# choice1: 1 step + 1 step + 1 step + 1 step + 1 step 
# 
# choice2: 2 step + 1 step + 1 step + 1 step
# choice3: 1 step + 2 step + 1 step + 1 step 
# choice4: 1 step + 1 step + 2 step + 1 step
# choice5: 1 step + 1 step + 1 step + 2 step
# 
# choice6: 2 step + 2 step + 1 step
# choice7: 2 step + 1 step + 2 step
# choice8: 1 step + 2 step + 2 step
# output: 8
# 
# 
# input: 6
# Logic:
# choice1: 1 step + 1 step + 1 step + 1 step + 1 step + 1 step
# 
# choice2: 2 step + 1 step + 1 step + 1 step + 1 step
# choice3: 1 step + 2 step + 1 step + 1 step + 1 step
# choice4: 1 step + 1 step + 2 step + 1 step + 1 step
# choice5: 1 step + 1 step + 1 step + 2 step + 1 step
# choice6: 1 step + 1 step + 1 step + 1 step + 2 step
# 
# choice7: 2 + 1 + 1 + 2
# choice8: 2 + 1 + 2 + 1
# choice9: 2 + 2 + 1 + 1
# 
# choice10: 1 + 1 + 2 + 2
# choice11: 1 + 2 + 1 + 2
# choice12: 1 + 2 + 2 + 1
# 
# choice13: 2 + 2 + 2

# output: 13
