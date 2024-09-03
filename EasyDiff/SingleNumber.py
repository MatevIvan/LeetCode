class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Sort the array
        nums.sort()
        # i will be our itterator
        i = 0
        # i will go up to 2 less than the length of nums
        while i < len(nums) - 2:
            if nums[i] == nums[i+1]:
                # if the number pairs are the same, go up by 2
                i+=2
            else:
                # if the numbers weren't equal, return that unique number
                return nums[i]
        # if we get out of the loop, the last number is the unique number
        return nums[i]

# Test the code
solutionInst = Solution()
print(solutionInst.singleNumber([4,1,2,1,2])) # 4
print(solutionInst.singleNumber([2,2,1])) # 1
print(solutionInst.singleNumber([1])) # 1
