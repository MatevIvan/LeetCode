class Solution(object):
    def longestCommonPrefix(self, strs):
        # Placeholder for longest prefix
        longestPrefix = ""
        # Placeholder fot temporary prefix
        tempPrefix = ""
        # j will be increased to find the longest prefix
        j = 1
        
        # make sure the prefix is never larger than the first word
        while j <= len(strs[0]):
            # set the temporary prefix to the first letter of the first word. 
            # Each time we go through the while loop, the temporary prefix will increase by one letter
            tempPrefix = strs[0][0:j]
            # itterate through every word in the given string list
            for i in range(1, len(strs)):
                if tempPrefix != strs[i][0:j]:
                    # if the temporary prefix is not found in the other words, return the currently saved longest prefix
                    return longestPrefix
            # if the temporary prefix was found in all the words, update the longest prefix valu
            longestPrefix = tempPrefix
            # increase the range of the prefix by 1
            j += 1
        # if the entire first word is found in the remaining words, this code will return the entire first word
        return longestPrefix

# Test the code
solution_inst = Solution()
print(solution_inst.longestCommonPrefix(["flower","flow","flight"])) # fl
print(solution_inst.longestCommonPrefix(["dog","racecar","car"])) # ""
print(solution_inst.longestCommonPrefix(["a"])) # a
print(solution_inst.longestCommonPrefix([""])) # ""
print(solution_inst.longestCommonPrefix(["words"])) # "words"