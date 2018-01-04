#! /usr/bin/env python

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""

class Solution:
     def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        array = []
        f1 = 0
        f2 = 0
        stop = True
        if nums1 == []:
            array = nums2
            stop = False
        if nums2 == []:
            array = nums1
            stop =False
        while(stop):
            if nums1[f1] < nums2[f2]:
                array.append(nums1[f1])
                f1 += 1
            else:
                array.append(nums2[f2])
                f2 += 1
            if f1 >= len(nums1) or f2>=len(nums2):
                array.extend(nums1[f1:])
                array.extend(nums2[f2:])
                stop = False
        l = len(array)
        if l % 2 == 1:
            return array[l//2]*1.0
        else:
            return (array[l//2]+array[l//2-1])/2.0


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1,3] ,[2]))
    print(s.findMedianSortedArrays([1,2] ,[3, 4]))