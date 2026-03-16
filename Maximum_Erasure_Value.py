# Maximum Erasure Value

class Solution:
    def maximumUniqueSubarray(self,num):
        start = 0
        max_sum = 0
        sum = 0
        seen = set()

        for end in range(len(num)):
            while num[end] in seen:
                seen.discard(num[start])
                sum-=num[start]
                start+=1
              
    
            seen.add(num[end])
            sum+=num[end]
                 
            max_sum=max(max_sum,sum)    

        return max_sum
    
obj = Solution()
ans = obj.maximumUniqueSubarray([4,2,4,5,6])
print(ans)
