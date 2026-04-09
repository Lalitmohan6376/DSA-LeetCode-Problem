class Solution:
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []

        for i in range(n*2):
            current = nums[i%n]

            while stack and nums[stack[-1]] < current:
                idx = stack.pop()

                result[idx] = current

            if i < n:
                stack.append(i)

        return result

obj = Solution()
ans = obj.nextGreaterElements([1,2,1])
print(ans)
        
