class Solution(object):
    def plusOne(self, digits): 
      # set i to the last digit
      i = len(digits) - 1

      # if the last digit is not a 9, add one and return the array
      if digits[i] < 9:
          digits[i] += 1
          return digits

      # while the digits are 9 repeating, keep changing them to 0
      while digits[i] == 9 and i > 0:
          digits[i] = 0
          i -= 1
      
      # if the current digit is 9, set it to 0 and add a 1 to the front
      # this only can happen if all the previous numbers were 9 and the first number is a 9
      if digits[i] == 9:
          digits[i] = 0
          digits.insert(0,1)
      else:
          # add one if the digit is not a 9
          digits[i] += 1

      # return the array
      return digits

# test the code
solutionInst = Solution()
print(solutionInst.plusOne([1,2,3])) # [1,2,4]
print(solutionInst.plusOne([4,3,2,1])) # [4,3,2,2]
print(solutionInst.plusOne([9,8,9])) # [9,9,0]