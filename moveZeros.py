#!/usr/bin/env python

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # zeronums = 0
        # for i in nums:
        #     zeronums += 1 if i == 0 else 0
        #
        # temp = []
        # for i in nums:
        #     if i != 0:
        #         temp.append(i)
        # temp = temp + [0] * zeronums
        # return temp

        lastNonZeroAt = 0
        for i,v in enumerate(nums):
            if v != 0:
                nums[lastNonZeroAt] = v
                lastNonZeroAt += 1
        for i in range(lastNonZeroAt, len(nums)):
            nums[i] = 0
        return nums

if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 3, 12]))