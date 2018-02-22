"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.
"""

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        if n == 0:
            return
        if m == 0:
            nums1.extend(nums2)

        while j < n:
            if nums1[i] >= nums2[j] and i - j < m:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
            elif nums1[i] < nums2[j] and i - j < m:
                i += 1
            else:
                nums1.extend(nums2[j:])
                break


if __name__ == "__main__":
    s = Solution()
    nums1, m, nums2, n = [0], 0, [1], 1
    print(nums1)
    print(m)
    s.merge(nums1, m, nums2, n)
    print(nums1)