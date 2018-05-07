"""
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30]
"""

import collections
class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        myDict = {}
        for word in words:
            for k in range(len(word)):
                if word[:k] in words:
                    myDict[word] = myDict.get(word, 0) + 1
        print(myDict)
        dict2 = collections.defaultdict(list)
        maxlen = 0
        for k,v in myDict.items():
            if v > maxlen:
                maxlen = v
            dict2[v].append(k)
        return sorted(dict2[maxlen])[0]


if __name__ == "__main__":
    s = Solution()
    print(s.longestWord(["a","banana","app","appl","ap","apply","apple"]))
    print(s.longestWord(["ogz","eyj","e","ey","hmn","v","hm","ogznkb","ogzn","hmnm","eyjuo","vuq","ogznk","og","eyjuoi","d"]))