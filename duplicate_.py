Contains Duplicate II
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

class Solution:
    def containsNearbyDuplicate(self, nums,k):
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

            if len(seen)>k:
                seen.remove(nums[i-k])
        return False


obj = Solution()
ans = obj.containsNearbyDuplicate([1,2,3,1],3)
print(ans)
