class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # if the number of rows is 1 or 2, hardcode the return value
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        # create the basic triangle for larger triangles
        triangle = [[1],[1,1]]
        # the first loop will go from the 2nd row up to the desired size
        for i in range(2,numRows):
            # create a temp array at the start of every loop with just the number 1
            temp = [1]
            # This second loop will go through the section of the triangle above itself and do the math for the new row
            for j in range(0,len(triangle[i-1])-1):
                temp.append(triangle[i-1][j]+triangle[i-1][j+1])
            # add a 1 at the end of the current row
            temp.append(1)
            # add the temp array to the existing triangle array
            triangle.append(temp)
        # return the 2d triangle array
        return triangle

# test the code 
solutionInst = Solution()
print(solutionInst.generate(5)) # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]