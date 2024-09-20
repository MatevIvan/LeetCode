class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # create a new set
        numSet = set()
        # go through each value in nums array
        for i in nums:
            # check if value exists in numSet
            if i in numSet:
                # return true if duplicate is found
                return True
            # add the value to the set 
            numSet.add(i)
        # return false if we made it through the nums array w/o duplicates
        return False

# test the code
solutionInst = Solution()
print(solutionInst.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(solutionInst.containsDuplicate([1,2]))