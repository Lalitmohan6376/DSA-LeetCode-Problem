class Solution:
    def twoSum(self, nums, target):
        arr = []
        for i in range(len(nums)):
            arr.append((nums[i], i))
        
        arr.sort()
        left = 0
        right = len(nums) - 1
        
        while left < right:
            curr_sum = arr[left][0] + arr[right][0]
            
            if curr_sum == target:
                return [arr[left][1], arr[right][1]]
            
            elif curr_sum < target:
                left += 1
            else:
                right -= 1

obj = Solution()
result = obj.twoSum([2, 7, 11, 15], 9)
print(result)
