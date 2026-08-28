class Solution:
    def isPalindromic(self, s):
        ans = ""
        for st in s:
            ac = ord(st)
            binary = format(ac, '08b')
            ans+=binary
        
        left = 0
        right = len(ans)-1
        while left < right:
            if ans[left] != ans[right]:
                return False

            left+=1
            right-=1
        return True

obj = Solution()
obj.isPalindromic(("ff"))
