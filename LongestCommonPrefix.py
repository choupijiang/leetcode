class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0 or "" in strs:
            return ""

        ans = ""
        for i in range(1, len(strs[0])+1):
            lcp = strs[0][:i]
            for w in strs:
                if w.find(lcp) != 0:
                    ans = strs[0][:i - 1]
                    return ans
                else:
                    ans = strs[0][:i]
        return ans


if __name__ == "__main__":
    strs = ["c","acc","ccc"]
    s = Solution()
    print(s.longestCommonPrefix(strs))