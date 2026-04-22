# Define two arrays leftSum and rightSum where:-
# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

class Solution:
    def leftRightDifference(self,nums):
        total_sum = sum(nums)
        left_sum = 0
        ans = []
        for i in range(len(nums)):
            right_sum = total_sum-left_sum-nums[i]
            
            diff = abs(left_sum-right_sum)
            ans.append(diff)
            
            left_sum+=nums[i]
        return ans
       
obj = Solution()
ans = obj.leftRightDifference([10,4,8,3])
print(ans)
