"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        ans = 0
        if tokens:
            for v in tokens:
                if v not in "+-*/":
                    stk.append(int(v))
                else:
                    a = stk.pop()
                    b = stk.pop()
                    ans += eval(str(b) + v + str(a))
                    stk.append(int(eval(str(b) + v + str(a))))
        return stk.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["0","3","/"]))
    print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))