class Solution:
    def removeDuplicates(self, nums):
        output = []
        j = 0
        k = 0 
        for i in range(len(nums)):
            if j < 2 or nums[i] != output[j-2]:
                output.append(nums[i])
                j+=1
                k+=1
                
        return len(output)
               

obj = Solution()
ans = obj.removeDuplicates([1,1,1,2,2,3,3])
print(ans)
