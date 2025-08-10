from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        l_result = ListNode(head.val)
        l_pivot = l_result
        while head.next:
            head = head.next
            if head.val != l_pivot.val:
                l_pivot.next = ListNode(head.val)
                l_pivot = l_pivot.next
        return l_result
