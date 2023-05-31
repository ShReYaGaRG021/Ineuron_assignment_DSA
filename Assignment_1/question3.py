class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

# Create an instance of the Solution class
solution = Solution()

# Call the searchInsert method on the instance
nums = [1, 3, 5, 6]
target = 4
result = solution.searchInsert(nums, target)
print(result)  # Output: 2