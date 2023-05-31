class Solution:
    def findErrorNums(self, nums):
        n, a, b = len(nums), sum(nums), sum(set(nums))
        s = n*(n+1)//2
        return [a-b, s-b]

# Create an instance of the Solution class
solution = Solution()

# Call the findErrorNums method on the instance
nums = [1, 2, 2, 4]
result = solution.findErrorNums(nums)
print(result)  # Output: [2, 3]