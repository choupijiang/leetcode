"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
Note:
1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""

import collections

class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        #         ans = 0
        #         Bstarts = collections.defaultdict(list)
        #         for i, x in enumerate(B):
        #             Bstarts[x].append(i)

        #         for i, x in enumerate(A):
        #             for j in Bstarts[x]:
        #                 k = 0
        #                 while i + k < len(A) and j + k < len(B) and  A[i + k] == B[j + k]:
        #                     k += 1
        #                 ans = max(ans, k)
        #         return ans

        ##---------bisect
        #         def check(length):
        #             seen = set(tuple(A[i:i+length]) for i in range(len(A) - length + 1))
        #             return any(tuple(B[i:i+length]) in seen for i in range(len(B) - length + 1))

        #         lo, hi = 0, min(len(A), len(B)) + 1
        #         while lo < hi:
        #             mid = (lo + hi)//2
        #             if check(mid):
        #                 lo = mid + 1
        #             else:
        #                 hi = mid
        #         return lo - 1

        # ---------dp
        memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    memo[i][j] = memo[i + 1][j + 1] + 1
        return max(max(row) for row in memo)

if __name__ == "__main__":
    s = Solution()
    print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))
