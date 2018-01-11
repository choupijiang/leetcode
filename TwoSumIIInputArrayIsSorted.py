"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""
class Solution:
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numslen = len(nums)
        lo = 0
        hi = numslen -1
        while lo < hi:
            if nums[lo] + nums[hi] < target:
                lo += 1
            elif nums[lo] + nums[hi] > target:
                hi -= 1
            else:
                return [lo+1, hi+1]
        return []