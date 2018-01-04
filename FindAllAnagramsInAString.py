#!/usr/bin/env python

"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

"""

from collections import Counter

class Solution:



    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        indexs = []
        i = 0
        pmap = Counter(p)
        lenp = len(p)
        lens = len(s)
        while(i<lens-lenp+1):
            substr = s[i:i+lenp]
            if  Counter(substr) == pmap :
                indexs.append(i)
            i += 1
        return indexs


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))