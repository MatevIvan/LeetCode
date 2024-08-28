class Solution(object):
    def lengthOfLastWord(self, s):
        # set i to the end of the string
        i = len(s) - 1
        # k will count the length of the word
        k = 0
        # check for spaces from the back and skip over them
        while s[i] == " ":
            i -= 1
        # check until a space is found or at the beginning of the string
        while s[i] != " " and i >= 0:
            # increase k: the length of the word
            k += 1
            # decrease i: working through the string backwards 
            i -= 1
        # return k
        return k

# test the code
solutionInst = Solution()
print(solutionInst.lengthOfLastWord("   fly me   to   the moon  ")) # output: 4
print(solutionInst.lengthOfLastWord("luffy is still joyboy")) # output: 6
print(solutionInst.lengthOfLastWord("Hello World")) # output: 5
print(solutionInst.lengthOfLastWord("a")) # output: 1
