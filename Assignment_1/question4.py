class Solution(object):
    def plusOne(self, digits):
        digits = [str(i) for i in digits]
        s = ''.join(digits)
        a = int(s) + 1
        l = list(str(a))
        l = [int(i) for i in l]
        return l

# Create an instance of the Solution class
solution = Solution()

# Define the input digits
digits = [1, 2, 3]

# Call the plusOne method on the instance
result = solution.plusOne(digits)

# Print the resulting list
print(result)