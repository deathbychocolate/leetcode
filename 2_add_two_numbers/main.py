from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    # Convenience for debugging when needed
    def __repr__(self):
        return f"ListNode({self.val})"


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = node = ListNode(val=0, next=None)
        sm: int = 0
        carryover: int = 0
        while l1 or l2 or carryover:

            # Compute sum and carry.
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sm = v1 + v2 + carryover
            carryover = sm // 10
            node.next = ListNode(val=sm % 10, next=None)
            node = node.next

            # Iterate.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carryover and carryover > 0: # Add.
            node.next = ListNode(val=carryover, next=None)
            node = node.next

        return head.next


# Helper: convert Python list (digits in reverse order) to linked list
def list_to_linked(nums: List[int]) -> Optional[ListNode]:
    if not nums:
        return None
    head = ListNode(nums[0])
    cur = head
    for v in nums[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


# Helper: convert linked list back to Python list (digits in reverse order)
def linked_to_list(node: Optional[ListNode]) -> List[int]:
    res = []
    cur = node
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res


def run_test(l1_list: List[int], l2_list: List[int], expected: List[int], test_name: str) -> None:
    try:
        l1 = list_to_linked(l1_list)
        l2 = list_to_linked(l2_list)
        result_node = Solution().addTwoNumbers(l1, l2)
        result = linked_to_list(result_node)
        ok = result == expected
        print(ok)
        if not ok:
            print(f"  l1:       {l1_list}")
            print(f"  l2:       {l2_list}")
            print(f"  expected: {expected}")
            print(f"  got:      {result}")
    except Exception as e:
        print(f"{test_name}: ERROR -> {e}")


def main() -> None:
    samples = [
        # Problem examples
        ([2, 4, 3], [5, 6, 4], [7, 0, 8], "Example 1 (342 + 465 = 807)"),
        ([0], [0], [0], "Example 2 (0 + 0 = 0)"),
        ([9,9,9,9,9,9,9], [9,9,9,9], [8,9,9,9,0,0,0,1], "Example 3 (long carry)"),
        # Additional tests / edge cases
        ([5], [5], [0,1], "Carry creates new most-significant node (5+5=10)"),
        ([1,2], [9,9,9], [0,2,0,1], "Different lengths with carry across many nodes (21+999=1020)"),
        ([0,1], [0,9], [0,0,1], "Zeros and carries inside (10 + 90 = 100)"),
        ([1,8], [0], [1,8], "Adding zero to a multi-digit number"),
        ([9,9], [1], [0,0,1], "Short + long with carry to new digit (99+1=100)"),
        ([0,0,0], [0,0,0], [0,0,0], "Multiple zeros (representing 0)"),
        # Longer constructed case
        ([9]*10, [1], [0]*10 + [1], "Long chain of 9s plus 1 -> new leading 1"),
    ]

    for l1, l2, expected, name in samples:
        run_test(l1, l2, expected, name)


if __name__ == "__main__":
    main()