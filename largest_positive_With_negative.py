class solution:
    def find(self,num):
        seen = set()
        ans = -1

        for i in num:
            if -i in seen:
                ans = max(ans,abs(i))
            seen.add(i)
        return ans

obj = solution()
ans = obj.find([1,2,3,-3])
print(ans)
