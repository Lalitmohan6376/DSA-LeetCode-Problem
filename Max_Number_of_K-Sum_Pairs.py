class Solution:
    def maxOperations(self,nums,k):
        nums.sort()
        n = len(nums)
        i = 0
        j = n-1
        count = 0

        while i<j:
           s = nums[i] + nums[j]
           if s == k:
               count+=1
               i+=1
               j-=1
           elif s<k:
               i+=1
           else:
               j-=1
        return count
         
obj = Solution()
ans = obj.maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4], 2)
print(ans)
