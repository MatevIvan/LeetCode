class PalindromeNum(object):
    def isPalindrome(self, x):
        # change the number to a list of characters
        numbers = list(str(x))
        # Go through each number, up to half the number in length
        for n in range(0,len(numbers)):
            if numbers[n] != numbers[len(numbers) - 1 - n]:
                # if the current number does not equal the number in the same position from the end, return False
                return False
        # If every number was equal in each position pair, return true
        return True

# Test the Code
twoSum = PalindromeNum()

print(twoSum.isPalindrome(-121)) # False
print(twoSum.isPalindrome(121)) # True