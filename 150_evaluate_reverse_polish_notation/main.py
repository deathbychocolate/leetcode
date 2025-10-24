from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokens = tokens[::-1]  # ['*', '3', '+', '1', '2']
        operands = []
        z: int | None = None
        while len(tokens) > 0:
            token = tokens.pop()
            if token.lstrip("+-").isdigit():
                operands.append(int(token))
            else:  # token is operator, perform computation
                x = operands.pop()
                y = operands.pop()
                if token == "/":
                    z = int(y / x)
                elif token == "*":
                    z = y * x
                elif token == "+":
                    z = y + x
                elif token == "-":
                    z = y - x
                operands.append(z)
        return operands[0]


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
