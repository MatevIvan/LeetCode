class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                k += 1
            else:
                i += 1
        return k

solutionInst = Solution()
# print(solutionInst.removeElement([3,2,2,3],3))
nums = [0,1,2,2,3,0,4,2]
print(solutionInst.removeElement(nums,2))
print(nums)


