class Solution(object):
    def romanToInt(self, s):
        # create dictionary of letters and their number values
        numbers = {
            "I" : 1, 
            "V" : 5, 
            "X" : 10, 
            "L" : 50, 
            "C" : 100, 
            "D" : 500, 
            "M" : 1000
            }
        # create number total place holder
        total = 0
        # the value used to itterate through the string
        i = 0
        # use while loop to go through the string
        while i < len(s):
            # if we are on the last character
            if i == len(s) - 1:
                # add to the total value of the letter
                total += numbers[s[i]]
                # return the total
                return total
            # if the value of the current letter is less than the following letter (4's and 9's)
            if numbers[s[i]] < numbers[s[i + 1]]:
                # subtract the first letter value from the second letter value
                total += numbers[s[i + 1]] - numbers[s[i]]
                # add two to the selector because we used 2 letter for the one value
                i += 2
            else: # if the letter is not part of a pair
                # add the value of the letter to the total
                total += numbers[s[i]]
                # add one to the selector to go on to the next letter
                i += 1
        # return the value once loop finishes going through the string
        return total
            
# test the code
solution_inst = Solution()
print(solution_inst.romanToInt("III")) #3
print(solution_inst.romanToInt("LVIII")) #58
print(solution_inst.romanToInt("MCMXCIV")) #1994
print(solution_inst.romanToInt("MMMCMXLIV")) #3944