class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        pattern = re.compile(r'^(\s)*(\+|\-)?([1-9]|\s)+(\d|\s)*')
        match = pattern.match(str)
        if not match:
            return 0
        digitStr = re.sub(r'(\s)*', '', match.group(0))
        if digitStr in ("","-"):
            return 0
        digit = int(digitStr)
        if digit > (2**31-1):
            digit = (2**31-1)
        if digit < -(2**31):
            digit = -2**31

        return digit


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi("3.14"))