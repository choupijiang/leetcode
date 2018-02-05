"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memo = [[0] * n] * m

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    memo[i][j] = 1
                else:
                    memo[i][j] = memo[i][j - 1] + memo[i - 1][j]
        return memo[m - 1][n - 1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 2))