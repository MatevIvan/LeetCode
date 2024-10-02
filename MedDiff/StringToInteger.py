class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        length = len(s)
        i = 0
        tempNum = "0"
        isNegative = False
        # Check if string starts with blank spaces and skip over them
        while i < length and s[i] == " ":
            i += 1
        # Check for a sign (- or +): Set isNegative is a negative sign is found
        if i < length and s[i] == "-":
            isNegative = True
            i += 1
        elif i < length and s[i] == "+":
            i += 1
        # Check for leading 0s and skip over them
        while i < length and s[i] == "0":
            i += 1
        # while numbers are found, concatinate to the tempNum string
        while i < length and s[i].isdigit():
            tempNum += s[i]
            i += 1
        #set a new int variable num to the int value of the tempNum string
        num = int(tempNum)
        # if negative sign was found (earlier), make the num negative
        if isNegative and num:
            num *= -1
        # check if number is in bounds -2^31 to 2^31-1
        if num < -2**31:
            return -2**31
        if num > 2**31-1:
            return 2**31-1
        return num

# Test cases
solutionInst = Solution()
print(solutionInst.myAtoi("   -042")) #-42
print(solutionInst.myAtoi("42")) #42
print(solutionInst.myAtoi("1337c0d3")) #1337
print(solutionInst.myAtoi("0-1")) #0
print(solutionInst.myAtoi("words and 987")) #0
print(solutionInst.myAtoi("-+12")) #0
print(solutionInst.myAtoi(" ")) #0
