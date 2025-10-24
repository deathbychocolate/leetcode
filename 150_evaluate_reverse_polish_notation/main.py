from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        z: int | None = None
        for token in tokens:
            if token.lstrip("+-").isdigit():
                stack.append(int(token))
            else:  # token is operator, perform computation
                y = stack.pop()
                x = stack.pop()
                if token == "/":
                    z = int(x / y)
                elif token == "*":
                    z = x * y
                elif token == "+":
                    z = x + y
                elif token == "-":
                    z = x - y
                stack.append(z)
        return stack[0]


def main() -> None:
    tokens_1 = ["2","1","+","3","*"]
    tokens_2 = ["4","13","5","/","+"]
    tokens_3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    r1 = 9 == Solution().evalRPN(tokens=tokens_1)
    r2 = 6 == Solution().evalRPN(tokens=tokens_2)
    r3 = 22 == Solution().evalRPN(tokens=tokens_3)
    print(r1)
    print(r2)
    print(r3)


if __name__ == "__main__":
    main()
