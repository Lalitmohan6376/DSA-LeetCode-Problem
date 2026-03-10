class Solution:
    def reverseWords(self,s):
        n = len(s)
        end = n-1
        result = []
        
        while end >= 0:
            if s[end] == " ":
                end-=1
                continue

            start = end
        
            while start >= 0 and s[start]!= " ":
                start-=1

            result.append(s[start+1:end+1])

            end = start-1

        return " ".join(result)
            
                
obj = Solution()
ans = obj.reverseWords("  hello world  ")
print(ans)
