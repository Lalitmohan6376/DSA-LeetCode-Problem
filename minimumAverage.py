# ## Minimum Average of Smallest and Largest Elements
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

# You repeat the following procedure n / 2 times:

# Remove the smallest element, minElement, and the largest element maxElement, from nums.
# Add (minElement + maxElement) / 2 to averages.
# Return the minimum element in averages.

class Solution:
    def minimumAverage(self,num):
        num.sort()
        output = []
        i = 0
        j = len(num)-1
        
        
        while i < j:
            avg = (num[i] + num[j])/2
            output.append(avg)
            i+=1
            j-=1
            mini = output[0]
            for k in range(1,len(output)):
                if output[k] < mini:
                    mini = output[k]
            
        print(mini)

        return output
obj = Solution()
ans = obj.minimumAverage([7,8,3,4,15,13,4,1])
print(ans)
