# Maximum Product of First and Last Elements of a Subsequence
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# You are given an integer array nums and an integer m.

# Return the maximum product of the first and last elements of any subsequence of nums of size m.

class Solution:
    def fimaximumProductnd(self,num,m):
        n = len(num)
        if m>n:
            return -1
        
        max_left = num[0]
        min_left = num[0]
        ans = float('-inf')

        for j in range(m-1,n):
            if j-(m-1)>0:
                i = j-(m-1)
                max_left = max(max_left,num[i])
                min_left = min(min_left,num[i])

            ans = max(
                ans,max_left*num[j],
                min_left*num[j]
            )
        return ans
    
obj = Solution()
ans = obj.maximumProduct([1,2,3,4,5],2)
print(ans)
