class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if the array only has one item, return it
        if len(nums) == 1: return nums[0]

        nums.sort() # sort the array
        i = 1 # our index through the array
        k = nums[0] # placeholder for our return value
        currentCounter = 1 # counter for the current number
        highestCounter = 0 # stores the highest number of duplicates

        while i < len(nums): # loop through the array
            # while the current value is the same as the last value, 
            # add to the counter and the index
            while nums[i] == nums[i-1]: 
                currentCounter += 1
                i += 1
                if i == len(nums): break # break if we hit the end of the array
            if currentCounter > highestCounter: # Check if the current number has more duplicates than the high
                highestCounter = currentCounter # replace the high with current
                k = nums[i-1] # update the return value to the previous number
            currentCounter = 1 # reset the counter
            i += 1 # move on to the next value
            
        return k # return the value

# test the code
solutionInst = Solution()
print(solutionInst.majorityElement([3,2,3])) #3
print(solutionInst.majorityElement([2,2,1,1,1,2,2])) #2
print(solutionInst.majorityElement([6,6,6,7,7])) #6
print(solutionInst.majorityElement([6,6,6,7,7,8,8,8,8])) #8
print(solutionInst.majorityElement([6, 8, 9, 6, 5, 7, 1, 8, 6, 1, 6, 2, 9, 6, 6, 2, 8, 3, 6, 8])) #6 this is a generated array
