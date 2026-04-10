# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return

        dummy = prev = ListNode(0, head)
        while head and n > 0:
            head = head.next
            n -= 1

        while head:
            head = head.next
            prev = prev.next

        prev.next = prev.next.next if prev and prev.next else None
        return dummy.next