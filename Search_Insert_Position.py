class Solution:
    def searchInsert(self, arr, tar):
        for i in range(len(arr)):
            if arr[i] == tar:
                return i
            elif tar < arr[i]:
                return i
        return len(arr)  
         
obj = Solution()
ans = obj.searchInsert([1,2,3,5], 6)
print(ans)
