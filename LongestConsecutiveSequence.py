#!/usr/env/bin python

"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity.

"""

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        longest_len = 1
        current_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_len += 1
            if nums[i] != nums[ i -1 ] + 1 and nums[i] != nums[ i -1 ]:
                longest_len = max(longest_len, current_len)
                current_len = 1
        return max(longest_len, current_len)


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([1,2,0,1]))