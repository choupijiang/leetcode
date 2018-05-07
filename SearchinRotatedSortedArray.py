class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if (nums[lo] <= nums[mid] and nums[mid]< nums[hi] ):
                if nums[lo] > target or nums[hi]< target:
                    return -1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            if (nums[lo] > nums[mid] and nums[mid] < nums[hi]):
                if nums[mid] < target and nums[hi] >= target:
                    lo = mid + 1
                else:
                    hi = mid
            if (nums[lo] < nums[mid] and nums[mid] > nums[hi]):
                if nums[mid] > target and nums[hi] < target:
                    hi = mid
                else:
                    lo = mid + 1
        return lo if lo != len(nums) and nums[lo] == target else -1


if __name__ == "__main__":
    s = Solution()
    print(s.search([3, 1], 0))