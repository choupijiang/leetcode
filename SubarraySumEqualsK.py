"""
Input:nums = [1,1,1], k = 2
Output: 2
"""


class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # #1
        # from functools import reduce
        # sum_of_nums = [0]
        # for i, v in enumerate(nums):
        #     sum_of_nums.append(  v + sum_of_nums[-1])
        # res = 0
        # for i in range(len(sum_of_nums)):
        #     for j in range(i + 1, len(sum_of_nums)):
        #         if sum_of_nums[j] - sum_of_nums[i] == k:
        #             res += 1
        # return res

        # #2
        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             count += 1
        # return count


        #3 hash map
        counter = 0
        hmap = {0:1}
        sum_of_nums = 0
        for i, v in enumerate(nums):
            sum_of_nums += v
            if sum_of_nums - k in hmap:
                counter += hmap[sum_of_nums - k]
            hmap[sum_of_nums] = hmap.get(sum_of_nums, 0) + 1
        return counter



if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1,1,1], 2))

