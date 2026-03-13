# #Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


class NumArray:

    def __init__(self, nums):
        self.prefix = [0] * len(nums)
        if nums:
            self.prefix[0] = nums[0]
            for i in range(1, len(nums)):
                self.prefix[i] = self.prefix[i-1] + nums[i]

    def sumRange(self, left, right):
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]


nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))  
print(obj.sumRange(2, 5))  
print(obj.sumRange(0, 5))  

