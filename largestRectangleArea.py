class Solution:
    def largestRectangleArea(self, heights):
        n = len(heights)
        stack = []
        max_area = 0
        
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                if not stack:
                    width = i
            
                else:
                    width = i - stack[-1]-1
                max_area = max(max_area,h*width)
                
            stack.append(i)
            
        while stack:
            h = heights[stack.pop()]
            
            if not stack:
                width = n
            else:
                width = n-stack[-1]-1
              
            max_area = max_area = max(max_area,h*width)
        return max_area
        
        
obj = Solution()        
ans = obj.largestRectangleArea([2,1,5,6,2,3])
print(ans)
        

        
        
