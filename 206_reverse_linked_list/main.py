from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev  # bc prev contains the new last known ListNode to start from.


def main() -> None:

    l1: ListNode = ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None))))))
    l2: ListNode = ListNode(val=5, next=ListNode(val=4, next=ListNode(val=3, next=ListNode(val=2, next=ListNode(val=1, next=ListNode(val=0, next=None))))))
    l3: ListNode = ListNode(val=0, next=ListNode(val=0, next=ListNode(val=0, next=ListNode(val=0, next=ListNode(val=0, next=ListNode(val=1, next=None))))))
    l4: ListNode = ListNode(val=-1, next=ListNode(val=-2, next=ListNode(val=-3, next=ListNode(val=-4, next=ListNode(val=-5, next=ListNode(val=-6, next=None))))))
    l5: ListNode = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=0, next=ListNode(val=0, next=ListNode(val=1, next=ListNode(val=2, next=None))))))

    def to_list(node: Optional[ListNode]) -> list[int]:
        vals: list[int] = []
        while node:
            vals.append(node.val)
            node = node.next
        return vals

    r1 = [5, 4, 3, 2, 1, 0] == to_list(Solution().reverseList(head=l1))
    r2 = [0, 1, 2, 3, 4, 5] == to_list(Solution().reverseList(head=l2))
    r3 = [1, 0, 0, 0, 0, 0] == to_list(Solution().reverseList(head=l3))
    r4 = [-6, -5, -4, -3, -2, -1] == to_list(Solution().reverseList(head=l4))
    r5 = [2, 1, 0, 0, 1, 1] == to_list(Solution().reverseList(head=l5))

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)


if __name__ == "__main__":
    main()
