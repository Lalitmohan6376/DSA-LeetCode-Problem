# def max_vowels(s,k):
#     count = 0

#     for i in range(k):
#         if s[i] in "aeiou":
#             count+=1

#     max_count = count

#     for i in range(k,len(s)):
#         if s[i] in "aeiou":
#             count+=1

#         if s[i-k] in "aeiou":
#             count-=1

#         max_count = max(max_count,count)
#     return max_count


# print(max_vowels("abciiidef",3))

class Solution:
    def countGoodSubstrings(self,s):
        count = 0

        for i in range(len(s)-2):
            window = s[i:i+3]

            if len(set(window)) == 3:
                count+=1

        return count

obj = Solution()
ans = obj.countGoodSubstrings("xyzzaz")
print(ans)