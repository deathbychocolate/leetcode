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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Edge cases.
        if not head:
            return head
        if not head.next:
            return None

        # Count the number of nodes.
        node_1 = head
        count_1 = 0
        while node_1:
            node_1 = node_1.next
            count_1 += 1

        # Count up to node we want to delete, count_d.
        count_d = count_1 - n

        # Edge cases.
        if count_d == 0:  # Remove head.
            return head.next

        node_2 = head
        prev = None
        count_2 = 0
        while count_2 < count_d:
            prev = node_2
            node_2 = node_2.next
            count_2 += 1
        prev.next = node_2.next

        return head


def run_test(input_list: List[int], n: int, expected: List[int], test_name: str) -> None:
    head = build_list(input_list)
    try:
        result_head = Solution().removeNthFromEnd(head, n)
        result = to_pylist(result_head)
        ok = result == expected
        print(ok)
        if not ok:
            print(f"  input:    {input_list}, n = {n}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"{test_name}: ERROR -> {e}")


def main() -> None:
    samples = [
        # Examples from the LeetCode problem statement
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5], "Example 1"),
        ([1], 1, [], "Example 2"),
        ([1, 2], 1, [1], "Example 3"),
        # Additional tests
        ([1, 2, 3], 3, [2, 3], "Remove head (n == length)"),
        ([1, 2, 3], 1, [1, 2], "Remove tail (n == 1)"),
        ([1, 2, 3, 4], 2, [1, 2, 4], "Remove middle"),
        ([1, 1, 1, 1], 2, [1, 1, 1], "Duplicates"),
        # Optional (LeetCode constraints say at least 1 node) included for robustness
        ([], 0, [], "Empty list (robustness)"),
    ]

    for inp, n, exp, name in samples:
        run_test(inp, n, exp, name)


if __name__ == "__main__":
    main()
