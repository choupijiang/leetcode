"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        psnums = sorted([i for i in nums if i >0])
        if psnums == []:
            return 1
        for i,v in enumerate(psnums):
            if v != i + 1:
                return i + 1
        return psnums[-1]+1


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1,2,0 ]))