class Solution(object):
    def removeDuplicates(self, nums):
        # goes threw every element in the nums list
        for i in range(0,len(nums) - 1):
            # creates a new variable to track the value after i
            j = i+1
            # j is kept within the size of the nums list
            while j < len(nums):
                if nums[i] == nums[j]:
                    # if the current value is equal to the next value, remove the next value
                    # this happens over and over again until the values are different
                    nums.pop(j)
                else:
                    # if the value are different, break out of the while loop to move on to next number
                    break
        # Return the modified list
        return nums
    
# Test the code
solutionInst = Solution()
print(solutionInst.removeDuplicates([0,0,0,0,0,1]))
print(solutionInst.removeDuplicates([0,0,1,1,1,2,3,3,3,4,4]))
print(solutionInst.removeDuplicates([-10,-10,1,1,4,4,4,5]))
print(solutionInst.removeDuplicates([1]))
print(solutionInst.removeDuplicates([]))
