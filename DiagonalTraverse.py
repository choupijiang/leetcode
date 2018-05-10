"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        self.res = []
        def getStep(matrix, r, c, direction = 1):
            m = len(matrix)
            n = len(matrix[0])
            if r < m  and c < n :
                self.res.append(matrix[r][c])
            if r == m - 1 and c == n - 1:
                return
            nr, nc, nextDir = r, c, direction
            if direction == 1:
                if r == 0 and c < n - 1:
                    nr = r
                    nc = c + 1
                    nextDir = 0
                elif c == n - 1:
                    nr = r + 1
                    nc = c
                    nextDir = 0
                else:
                    nr = r - 1
                    nc = c + 1
            else:
                if r == m - 1 and c > 0:
                    nr = r
                    nc = c + 1
                    nextDir = 1
                elif c == 0:
                    nr = r + 1
                    nc = c
                    nextDir = 1
                else:
                    nr = r + 1
                    nc = c - 1
            getStep(matrix, nr, nc, nextDir)
        getStep(matrix, 0, 0, 1)
        return self.res

if __name__ == "__main__":
    s = Solution()
    print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]] ))
    print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]] ))
