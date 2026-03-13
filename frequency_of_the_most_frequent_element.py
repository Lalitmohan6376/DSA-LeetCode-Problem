# most freauThe frequency of an element is the number of times it occurs in an array.
#You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
#Return the maximum possible frequency of an element after performing at most k operations.

class Solution:
    def maxFrequency(self,num,k):
        num.sort()

        left = 0
        total = 0
        max_freq = 0

        for right in range(len(num)):
            total+=num[right]


            while num[right] * (right-left+1)-total>k:
                total-=num[left]
                left+=1

            max_freq = max(max_freq,right-left+1)

        return max_freq
    
obj = Solution()
ans = obj.maxFrequency([1,2,4],5)
print(ans)
