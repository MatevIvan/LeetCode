class Solution(object):
    def strStr(self, haystack, needle):
        # i goes through the heystack characters
        i = 0
        # j goes through the needle characters
        j = 0
        # i needs to stay in the bounds of the haystack size - the needle size
        for i in range(len(haystack) - len(needle) + 1):
            # first needle letter and haystack letter are the same -> start the check 
            if haystack[i] == needle[j]:
                # k will go through and test the potential section of the haystack
                k = i
                # k needs to be less than the location of i and the length of needle
                while k <= i + len(needle):
                    # j is the length of the needle when all the letters have been the same
                    if j == len(needle):
                        # return the location of i
                        return i
                    # check to see if the current value of haystack is the same as needle
                    if haystack[k] == needle[j]:
                        # increase k and j to continue checking values
                        k += 1
                        j += 1
                    else:
                        # if haystack and needle values are not alike, reset j and set k to the breaking value
                        j = 0
                        k = i + len(needle) + 1
        # return -1 if no matching set was found
        return -1
        
# test the code
solutionInst = Solution()
print(solutionInst.strStr("mississippi","issip")) # output: 4
print(solutionInst.strStr("a","a")) # output: 0
