class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr1.sort()
        arr2.sort()

        i = 0
        j = 0
        count = 0

        while i < len(arr1):
            valid = True

            while j < len(arr2):
                if abs(arr1[i] - arr2[j]) <= d:
                    valid = False
                    break
                elif arr2[j] < arr1[i] - d:
                    j += 1
                else:
                    break

            if valid:
                count += 1

            i += 1

        return count
obj = Solution()
ans = obj.findTheDistanceValue([4,5,6],[10,9,1,8],2)
print(ans)
