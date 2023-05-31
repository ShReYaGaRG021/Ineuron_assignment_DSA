class Solution:
    def moveZeroes(self, nums):
        i = 0
        c = 0
        while (len(nums) - nums.count(0) - 1) >= i:
            if nums[i] == 0:
                nums.pop(i)
                c += 1
                i -= 1
            i += 1
        for i in range(c):
            nums.append(0)

# Create an instance of the Solution class
solution = Solution()

# Call the moveZeroes method on the instance
nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)

# Print the modified nums list
print(nums)  # Output: [1, 3, 12, 0, 0]
