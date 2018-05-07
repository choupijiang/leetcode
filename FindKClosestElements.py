class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(arr) - 1
        while lo + k <= hi:
            mid = (lo + hi) // 2
            if arr[mid] >= x:
                hi = mid
            else:
                lo = lo + 1
        return arr[lo-1:lo+k-1]

if __name__ == "__main__":
    s = Solution()
    print(s.findClosestElements([0,0,0,1,3,5,6,7,8,8], 2, 2))