"""
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""


class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[0] * n] * n
        # for j in range(n):
        #     dp[j][j] = 1
        #     for i in range(0, j):
        #
        #         if s[i] == s[j]:
        #             dp[i][j] = dp[i+1][j-1] + 2
        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        # for r in dp:
        #     print(r)
        # return dp[0][n-1]



        # n = len(s)
        # dp = [[0] * n] * n
        # for i in range(n-1, -1, -1):
        #     dp[i][i] = 1
        #     for j in range(i+1, n):
        #         if s[i] == s[j]:
        #             dp[i][j] = 2 + dp[i+1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        #
        # return dp[0][n-1]


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindromeSubseq("bbbab" ))