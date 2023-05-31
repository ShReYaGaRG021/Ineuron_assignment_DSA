class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d:
                return [d[r], i]
            d[j] = i

# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method on the instance
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]