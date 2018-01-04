#! /usr/bin/env python
"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space
"""

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern_map1 = {}
        pattern_map2 = {}
        str_splits = str.split(" ")
        for (p,word) in zip(pattern, str_splits):
            if not p in pattern_map1.keys():
                pattern_map1[p] = word

            if not word in pattern_map2.keys():
                pattern_map2[word] = p

            if pattern_map1[p] != word or pattern_map2[word] != p:
                return False

        return True


if __name__ == "__main__":
    s = Solution()
    print(s.wordPattern("abba", "dog dog dog dog"))