class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = "1"
        if n == 1:
            return ans

        for now in range(1, n):
            prev = ans
            ans = ""
            last, curr = 0, 0
            last_ch = prev[0]
            for i,ch in  enumerate(prev):
                if ch != last_ch:
                    pre_num = i - last
                    ans = ans + "" + str(pre_num)+""+last_ch
                    last = i
                    last_ch = ch
            ans = ans + str((len(prev) - last)) + "" + last_ch
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.countAndSay(10))