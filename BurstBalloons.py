"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
 Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""

class Solution:

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsx = [1] + [x for x in nums if x > 0] + [1]
        n  = len(numsx)
        memo = [[0] * n] * n

        return (self.burst(memo, numsx, 0, n - 1))

    def burst(self, memo, numsx, left, right):
        if left + 1 == right:
            return 0
        if memo[left][right] > 0:
            return memo[left][right]

        for i in range(left + 1, right):
            memo[left][right] = max(memo[left][right],
                    self.burst(memo, numsx, left, i) +
                    self.burst(memo, numsx, i, right) +
                    numsx[left] * numsx[i] * numsx[right]
                    )
        return memo[left][right]

if __name__ == "__main__":
    s = Solution()
    print(s.maxCoins([3, 1, 5, 8]))
        

