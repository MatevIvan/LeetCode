class Solution(object):
    def searchInsert(self, nums, target):
      # if target number is greater than the last number of the list, return the length of the list
      if target > nums[-1]:
         return len(nums)
      # itterate through each value of the nums list
      for i in range(0, len(nums)):
        #  if the current number equals the target, return the current position
         if nums[i] == target:
            return i
        # if the target is greater than the current number and less than the following number,
        # the target needs to be inserted into the next i position
         if nums[i] < target and nums[i+1]>target:
            # note that the nums[i+1] could throw an error if not for the first return 
            # statement checking to see if the target is larger than the last number
            return i + 1
      # finally return 0 because there is no other place for the target to go. it's like a default
      return 0
    
# test the code
solutionInst = Solution()
print(solutionInst.searchInsert([1,3],7)) # output: 2