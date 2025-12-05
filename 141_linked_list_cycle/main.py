from typing import Optional, List, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' | None = None):
        self.val = val
        self.next = next


def build_list(vals: List[int], pos: int = -1) -> Optional[ListNode]:
    if not vals:
        return None
    nodes: List[ListNode] = []
    for v in vals:
        nodes.append(ListNode(v))
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        if 0 <= pos < len(nodes):
            nodes[-1].next = nodes[pos]
        else:
            raise ValueError("pos out of range")
    return nodes[0]


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # Edge cases.
        if head is None:
            return False

        fast: ListNode | None = head
        slow: ListNode | None = head
        count: int = 0
        while fast:

            if count & 1 == 0:  # even
                fast = fast.next
            elif count & 1 == 1:  # odd
                fast = fast.next
                slow = slow.next

            if fast == slow:
                return True

            count += 1

        return False

        # # Leetcode accepts the solution though it is not the requested space complexity of O(1).
        # # Time O(n); Space O(n)
        # previous_nodes: set[ListNode] = set()
        # while head:
        #     if head in previous_nodes:
        #         return True
        #     previous_nodes.add(head)
        #     head = head.next
        # return False


def run_tests() -> None:
    # Tests: (vals, pos, expected_has_cycle)
    tests: List[Tuple[List[int], int, bool]] = [
        # Examples from the problem
        ([3, 2, 0, -4], 1, True),      # example 1: cycle at index 1
        ([1, 2], 0, True),             # example 2: cycle at index 0
        ([1], -1, False),              # example 3: no cycle

        # Additional tests (edge cases and variants)
        ([], -1, False),               # empty list
        ([1], 0, True),                # single node that points to itself
        ([1, 2, 3, 4, 5], -1, False),  # longer list without cycle
        ([1, 2, 3, 4, 5], 0, True),    # cycle linking tail to head
        ([1, 2, 3, 4, 5], 2, True),    # cycle linking tail to middle
        ([1, 2], -1, False),           # two nodes without cycle
        ([1, 1, 1], 2, True),          # duplicates, tail points to last node (self-cycle)
        ([0, -1, 2, -2, 3], 4, True)   # tail points to itself / index 4
    ]

    solution = Solution()

    for i, (vals, pos, expected) in enumerate(tests, start=1):
        head = build_list(vals, pos)
        result = solution.hasCycle(head)
        print(f"Test #{i}: {expected == result}")


if __name__ == "__main__":
    run_tests()
