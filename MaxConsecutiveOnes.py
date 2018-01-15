#! /usr/bin/env python
"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0

        maxLen = 0
        ones = 0

        if nums[0] == 1:
            maxLen = 1
            ones = 1

        for i in range(1, len(nums)):
            if nums[i] == 1:
                if nums[i - 1] == 1:
                    ones += 1
                else:
                    ones = 1

            if nums[i] == 0:
                ones = 0
            maxLen = max(maxLen, ones)
        maxLen = max(maxLen, ones)
        return maxLen


if __name__ == "__main__":
	s = Solution()
	print(s.findMaxConsecutiveOnes([1,0,1,1,0,1]))
