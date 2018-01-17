"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        l1, l2 = len(haystack), len(needle)
        res = -1
        for i in range(l1 - l2 + 1):
            for j in range(l2):
                if haystack[i + j] == needle[j]:
                    res = i
                else:
                    res = -1
                    break
            if res != -1:
                return res
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("hello", needle = "ll"))