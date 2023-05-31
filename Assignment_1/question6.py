class Solution(object):
    def containsDuplicate(self, nums):
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            else:
                hset.add(idx)

# Create an instance of the Solution class
solution = Solution()

# Call the containsDuplicate method on the instance
nums = [1, 2, 3, 1]
result = solution.containsDuplicate(nums)
print(result)  # Output: True