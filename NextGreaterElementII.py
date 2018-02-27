"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
"""

class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stk = []
        length = len(nums)
        res = [-1] * length
        for i in range(2 * length - 1, 0, -1):
            while len(stk) > 0 and nums[i % length] >= nums[stk[-1]]:
                stk.pop()
            res[i % length] = -1 if len(stk) == 0 else nums[stk[-1]]
            stk.append( i % length)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElements([1,2,1]))