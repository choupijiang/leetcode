#! /usr/bin/env python
"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        tn = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if sum(nums[i:j]) == k:
                    tn += 1
                if sum(nums[i:j]) > k:
                    break
        return tn

if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1, 1, 1], 2))