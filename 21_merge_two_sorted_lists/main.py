from typing import Optional


def build_list(vals: list[int]) -> ListNode | None:
    head: ListNode | None = None
    tail: ListNode | None = None
    for v in vals:
        node: ListNode | None = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def to_pylist(node: ListNode | None) -> list[int]:
    out: list[int] = []
    while node:
        out.append(node.val)
        node = node.next
    return out


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head_1 = list1
        head_2 = list2
        head = node = ListNode()  # Important technique, keep track of head and use node to iterate over 'new' list

        while head_1 and head_2:
            if head_1.val < head_2.val:
                node.next = head_1
                head_1 = head_1.next
            elif head_1.val >= head_2.val:
                node.next = head_2
                head_2 = head_2.next
            else:
                print("A condition you did not account for has occurred.")
            node = node.next

        # sometimes we have values left over in the lists, select the one that has more values
        node.next = head_1 or head_2

        return head.next  # Because the first node has no value


def main() -> None:

    sample_pairs = [
        ([1, 3, 4], [2, 5]),
        ([1, 2, 4], [1, 3, 4]),
        ([1, 1, 2, 3], [1, 2, 2, 4]),
        ([1, 3, 5, 7, 9], [2, 4, 6]),
        ([-3, -1, 2], [-2, 0, 1]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], []),
        ([0, 0, 1, 1, 2, 3, 5, 8, 13, 21], [0, 1, 1, 2, 2, 3, 5, 8, 13, 21]),
        ([5], [1]),
        ([], [0]),
        ([], []),
        ([1, 2, 4], [1, 3, 4]),
    ]

    samples = [(build_list(a), build_list(b)) for a, b in sample_pairs]

    r1 = [1, 2, 3, 4, 5] == to_pylist(Solution().mergeTwoLists(list1=samples[0][0], list2=samples[0][1]))
    r2 = [1, 1, 2, 3, 4, 4] == to_pylist(Solution().mergeTwoLists(list1=samples[1][0], list2=samples[1][1]))
    r3 = [1, 1, 1, 2, 2, 2, 3, 4] == to_pylist(Solution().mergeTwoLists(list1=samples[2][0], list2=samples[2][1]))
    r4 = [1, 2, 3, 4, 5, 6, 7, 9] == to_pylist(Solution().mergeTwoLists(list1=samples[3][0], list2=samples[3][1]))
    r5 = [-3, -2, -1, 0, 1, 2] == to_pylist(Solution().mergeTwoLists(list1=samples[4][0], list2=samples[4][1]))
    r6 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] == to_pylist(Solution().mergeTwoLists(list1=samples[5][0], list2=samples[5][1]))
    r7 = [0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 5, 8, 8, 13, 13, 21, 21] == to_pylist(Solution().mergeTwoLists(list1=samples[6][0], list2=samples[6][1]))
    r8 = [1, 5] == to_pylist(Solution().mergeTwoLists(list1=samples[7][0], list2=samples[7][1]))
    r9 = [0] == to_pylist(Solution().mergeTwoLists(list1=samples[8][0], list2=samples[8][1]))
    r10 = [] == to_pylist(Solution().mergeTwoLists(list1=samples[9][0], list2=samples[9][1]))
    r11 = [1, 1, 2, 3, 4, 4] == to_pylist(Solution().mergeTwoLists(list1=samples[10][0], list2=samples[10][1]))

    print(r1)
    print(r2)
    print(r3)
    print(r4)
    print(r5)
    print(r6)
    print(r7)
    print(r8)
    print(r9)
    print(r10)
    print(r11)


if __name__ == "__main__":
    main()
