
class Solution:
    def nextGreaterElement(self,num1,num2):
        stack = []
        num_map = {}
    
        for num in num2:
            while stack and num > stack[-1]:
                num_map[stack.pop()] = num
            stack.append(num)
        
        result = []
    
        for num in num1:
             result.append(num_map.get(num, -1))
        return result
    
num1 = [2,1]        
num2 = [2,1,3]
    
obj = Solution()
ans = obj.nextGreaterElement(num1,num2)
print(ans)
        
