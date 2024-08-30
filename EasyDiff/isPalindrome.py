class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # j is the backwards pointer
        j = len(s)-1
        # i is the forwards pointer
        i = 0
        
        # i should always be less than j other wise we are overlapping our search
        while i < j:
            # find the next letter or number for the i pointer
            while (not s[i].isalpha() and not s[i].isdigit()) and i < j:
                i += 1
            # find the next letter or number for the j pointer
            while (not s[j].isalpha() and not s[j].isdigit()) and j > i:
                j -= 1

            # compare both values, ignoring case
            if s[i].lower() != s[j].lower():
                # return false if values are different
                return False
            # if values are the same, move on to next set of values
            else:
                i += 1
                j -= 1
        # return true is we make it out of the loop
        return True

# test the code
solutionInst = Solution()
print(solutionInst.isPalindrome("A man, a plan, a canal: Panama")) #True
print(solutionInst.isPalindrome("  y yy ")) #True