class Solution:
    def intersection(self, num1, num2):
        num1.sort()
        num2.sort()
        
        i, j = 0, 0
        result = []
        
        while i < len(num1) and j < len(num2):
            if num1[i] == num2[j]:
                # duplicate avoid
                if len(result) == 0 or result[-1] != num1[i]:
                    result.append(num1[i])
                i += 1
                j += 1
            elif num1[i] < num2[j]:
                i += 1
            else:
                j += 1
        
        return result

obj = Solution()
print(obj.intersection([1,2,3,4],[1,5,2,6]))
