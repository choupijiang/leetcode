"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        lo = 0
        hi = len(nums) - 1
        out = []
        while lo < hi:
            if nums[lo] + nums[hi]*2 < 0:
                lo += 1
            elif nums[lo]*2 + nums[hi] >0:
                hi -= 1
            else:
                v = 0 - nums[lo] - nums[hi]
                for i in range(lo+1, hi):
                    if nums[i] == v:
                        out.append([nums[lo], v, nums[hi]])
                lo += 1
        return out

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))