class Solution:
    def removeDuplicateLetters(self, s):
        seen = set()
        stack = []
        
        last = {}
        
        for i in range(len(s)):
            last[s[i]] = i
            
        for i in range(len(s)):
            ch = s[i]
            
            if ch in seen:
                continue
            
            while stack and ch < stack[-1] and i < last[stack[-1]]:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)
        
obj = Solution()
ans = obj.removeDuplicateLetters("cbacdcbc")
print(ans)
        
