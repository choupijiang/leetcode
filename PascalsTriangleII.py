"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex == 1:
            return [1]
        if rowIndex == 2:
            return [1, 1]
        lastrow = [1, 1]
        for i in range(3, rowIndex + 1):
            currentrow = [1, 1]
            for j in range(1, i - 1):
                currentrow.insert(-1, lastrow[j - 1] + lastrow[j])
            lastrow = currentrow
        return lastrow

if __name__ == "__main__":
    s = Solution()
    print(s.getRow(3))