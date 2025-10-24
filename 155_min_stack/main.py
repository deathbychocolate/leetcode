class MinStack:

    def __init__(self):
        self._stack: list[tuple[int, int]] = []  # value, min-value when value was added

    def push(self, val: int) -> None:
        if len(self._stack) <= 0:
            self._stack.append((val, val))  # first val is min val
        else:
            _, mv = self._stack[-1]
            self._stack.append((val, min(val, mv)))
        return None

    def pop(self) -> None:
        if len(self._stack) <= 0:
            return None
        else:
            self._stack.pop()

    def top(self) -> int:
        if len(self._stack) <= 0:
            return None
        else:
            v, _ = self._stack[-1]
            return v

    def getMin(self) -> int:
        if len(self._stack) <= 0:
            return None
        else:
            _, mv = self._stack[-1]
            return mv


def main() -> None:
    min_stack = MinStack()
    r1 = None == min_stack.push(1)
    r2 = None == min_stack.push(2)
    r3 = None == min_stack.push(0)
    r4 = 0 == min_stack.getMin()
    r5 = None == min_stack.pop()
    r6 = 2 == min_stack.top()
    r7 = 1 == min_stack.getMin()
    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(r7)


if __name__ == "__main__":
    main()
