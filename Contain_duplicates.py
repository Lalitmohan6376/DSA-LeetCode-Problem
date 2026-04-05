class Solution:
    def containsDuplicate(self,num):
        result = []
        for i in range(len(num)):
            if num[i] in result:
                return True
            else:
                result.append(num[i])
        return False

obj = Solution()
ans = obj.containsDuplicate([1,2,3,4])
print(ans)
