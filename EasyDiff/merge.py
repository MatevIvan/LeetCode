class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # create a loop to go through the second set of numbers
        for i in range(0,n):
            # insert the values of the second array in the first array (after the m value)
            nums1[m+i] = nums2[i]
        # sor the array
        nums1.sort()

        # print the array (optional - for debugging)
        # print(nums1)
                
# test the code
solutionInst = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solutionInst.merge(nums1,m,nums2,n)