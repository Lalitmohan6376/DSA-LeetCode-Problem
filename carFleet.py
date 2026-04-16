class Solution:
    def carFleet(self, target, position, speed):
        car = list(zip(position,speed))
        car.sort(reverse=True)
        
        stack = []
        
        for pos,spd in car:
            time = (target-pos) / spd
            
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)

obj = Solution()
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

ans = obj.carFleet(target,position,speed)
print(ans)
