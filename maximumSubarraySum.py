class Solutiuon:
    def maximumSubarraySum(self,num,k):
        left = 0
        current_sum = 0
        max = 0
        count = {}

        for start in range(len(num)):
            current_sum+=num[start]
            count[num[start]] = count.get(num[start],0)+1

            while (start-left+1) > k:
                current_sum-=num[left]
                count[num[left]] -=1
                if count[num[left]] == 0:
                    del count[num[left]]
                left+=1

            if ((start-left+1)) == k and len(count) == k:
                if current_sum > max:
                    max = current_sum
        return max

obj = Solutiuon()
ans = obj.maximumSubarraySum([1,5,4,2,9,9,9],3)
print(ans)
