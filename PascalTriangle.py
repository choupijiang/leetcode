#! /usr/bin/env python
"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for row in range(numRows):
            if row == 0:
                res.append([1])
            if row == 1:
                res.append([1, 1])
            if row > 1:
                temp = [1, 1]
                for col in range(1, row):
                    temp.insert(-1, sum(res[row-1][col-1:col+1]))
                res.append(temp)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.generate(5))