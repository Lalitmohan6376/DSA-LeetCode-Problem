class Solution:
    def removeElement(self,nums,val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]

        return k 

print(Solution().removeElement([1,2,2,3],3))
