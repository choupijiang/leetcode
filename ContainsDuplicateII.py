"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j]
and the absolute difference between i and j is at most k.
"""
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lennums = len(nums)

        def mindistance(arr, k):
            mindist = 0
            for i in range(len(arr)-1):
                if arr[i + 1] - arr[i] <= k:
                    return True
            return False

        res = {}
        if k == 0:
            return False
        for i, x in enumerate(nums):
            if x not in res:
                res[x] = [i]
            else:
                res[x].append(i)
                if mindistance(res[x], k):
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate([1,2,1], 1))