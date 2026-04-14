#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.

class Solution:
    
    def runningsum(self,nums):
        run = 0
        output = []
        for i in range(len(nums)):
            run+=nums[i]
            output.append(run)
        return  output

obj = Solution()
ans = obj.runningsum([1,2,3,4])
print(ans)
