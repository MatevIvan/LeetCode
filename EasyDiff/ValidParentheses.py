class Solution(object):
    def isValid(self, s):
        nextToClose = [] # This list will update to the order of closing brackets needed 
        for c in s:
            # This first section checks for opening brackets and adds the closing brackets to list
            if c == "(":
                nextToClose.append(")")
                continue
            if c == "[":
                nextToClose.append("]")
                continue
            if c == "{":
                nextToClose.append("}")
                continue

            # This second section handles the closing brackets
            # If there is a closing bracket, but no brackets are stored, return False
            # This happens when the string begins with a closing bracket and not an opening bracket
            if len(nextToClose) > 0: 
                # Checks if the current closing bracket is equal to the last bracket saved in the list
                # If the wrong bracket is found, the brackets are out of order. Return False
                if c == nextToClose[-1]:
                    # If correct bracket is present, remove from list and continue
                    nextToClose.pop()
                else:
                    return False
            else:
                return False
        # Return true only if the length of the list is 0 meaning that all brackets have been closed
        return not(len(nextToClose))

# Code testing
solutionInst = Solution()
print(solutionInst.isValid("()")) # True
print(solutionInst.isValid("()[]{}")) # True
print(solutionInst.isValid("([)]")) # False
print(solutionInst.isValid("}")) # False
print(solutionInst.isValid("")) # True