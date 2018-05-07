class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        self.origin = list(self.array)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array = self.origin
        self.origin = list(self.array)
        return self.array

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        import random
        sh = self.array
        ans = []
        while len(sh) > 0:
            ans.append(sh.pop(random.randint(0, len(sh) - 1)))
        return ans



# Your Solution object will be instantiated and called as such:
if __name__ == "__main__":
    nums = [1,3,2]
    obj = Solution(nums)
    param_1 = obj.reset()
    print(param_1)
    param_2 = obj.shuffle()
    print(param_2)