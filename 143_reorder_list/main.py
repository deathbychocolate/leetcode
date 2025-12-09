from typing import Optional, List


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def build_list(vals: List[int]) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    tail: Optional[ListNode] = None
    for v in vals:
        node = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node  # type: ignore
            tail = node
    return head


def to_pylist(node: Optional[ListNode]) -> List[int]:
    out: List[int] = []
    while node:
        out.append(node.val)
        node = node.next
    return out


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Edge cases.
        if not head:
            return None
        if not head.next:
            return None

        h1 = h2 = t1 = t1_prev = t2 = head

        # Find the halfway point.
        count: int = 0
        while t1 and t2:
            if count & 1 == 0:  # even
                t2 = t2.next
            elif count & 1 == 1:  # odd
                t1_prev = t1
                t1 = t1.next
                t2 = t2.next
            count += 1
        h2 = t1  # type: ignore
        t1_prev.next = None  # Split the list in half.

        # Reverse the 2nd half (h2).
        prev, curr = None, h2
        while curr:  # prev is new head
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Merge our 2 lists (h1 and prev)
        dummy = ListNode()
        current = dummy
        while h1 and prev:
            current.next = h1
            h1 = h1.next
            current = current.next

            current.next = prev
            prev = prev.next
            current = current.next

        if h1:
            current.next = h1
        elif prev:
            current.next = prev

        # Update the original head's next pointer
        head.next = dummy.next.next


def run_test(input_list: List[int], expected: List[int], test_name: str) -> None:
    head = build_list(input_list)
    try:
        Solution().reorderList(head)
        result = to_pylist(head)
        ok = result == expected
        print(f"{ok}")
        if not ok:
            print(f"  input:    {input_list}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"{test_name}: ERROR -> {e}")


def main() -> None:
    samples = [
        # Examples from the problem statement
        ([1, 2, 3, 4], [1, 4, 2, 3], "Example 1"),
        ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3], "Example 2"),
        # Additional tests
        ([1], [1], "Single node"),
        ([1, 2], [1, 2], "Two nodes"),
        ([1, 2, 3], [1, 3, 2], "Three nodes"),
        ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4], "Even length 6"),
        ([1, 1, 1, 1], [1, 1, 1, 1], "All equal values"),
        ([1, 2, 2, 3, 4], [1, 4, 2, 3, 2], "Duplicates"),
        ([10, 20, 30, 40, 50, 60, 70], [10, 70, 20, 60, 30, 50, 40], "Odd length 7"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 9, 2, 8, 3, 7, 4, 6, 5], "Odd length 9"),
        # Optional: empty list (LeetCode constraint says at least 1 node, but included for robustness)
        ([], [], "Empty list"),
    ]

    for inp, exp, name in samples:
        run_test(inp, exp, name)


if __name__ == "__main__":
    main()
