# longest_substring_with_repeating

class Solution:
    def lengthOfLongestSubstring(self, s):
        st = set()
        i = 0
        ans = 0
        for j in range(len(s)):
            while s[j] in st:
                st.remove(s[i])
                i+=1
            st.add(s[j])
            ans = max(ans,j-i+1)
        return ans

obj = Solution()
ans = obj.lengthOfLongestSubstring("abcabcbb")
print(ans)
        
