class Solution(object):
    def addBinary(self, a, b):
        # the end of the first string
        i = len(a) - 1
        # the end of the second string
        j = len(b) - 1
        # placeholder for result
        result = ""
        # placeholder for the carried 1
        carry = 0
        while i >= 0 or j >= 0 or carry:
            # set the current total to the carry at the start of every loop
            total = carry

            # itterate through both strings at the same time and store their values to the total
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1

            # total % 2 will only return a 1 or a 0
            result = str(total%2) + result
            # if the total is a 2 or 3, the carry will be 1
            carry = int(total/2)

        return result

# Test the code
solutionInst = Solution()
print(solutionInst.addBinary("11","1")) # 100
print(solutionInst.addBinary("1010","1011")) # 10101