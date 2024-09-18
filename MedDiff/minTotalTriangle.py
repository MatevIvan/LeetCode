class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        minimun = triangle[0][0]
        currentIndex = 0
        for i in range(1,len(triangle)):
            if triangle[i][currentIndex] < triangle[i][currentIndex + 1]:
                minimun += triangle[i][currentIndex]
            else:
                minimun += triangle[i][currentIndex + 1]
                currentIndex = currentIndex + 1
        return minimun

solutionInst = Solution()
print(solutionInst.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
print(solutionInst.minimumTotal([[-10]]))