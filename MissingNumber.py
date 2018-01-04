#!/usr/bin/env python

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

"""

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1
        # return (set(range(len(nums)+1)) - set(nums)).pop()
        # 2 XOR
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


if __name__ == "__main__":
    s = Solution()
    print(s.missingNumber([3, 0, 1]))
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))