class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        stack = []
        
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        max_width = 0
        
        for j in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width

obj = Solution()
print(obj.maxWidthRamp([6,0,8,2,1,5]))
