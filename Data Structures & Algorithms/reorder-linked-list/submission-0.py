# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        dummy = ListNode(0, head)
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        rev_head = slow.next

        while rev_head and rev_head.next:
            temp = rev_head.next
            rev_head.next = temp.next
            temp.next = slow.next
            slow.next = temp

        
        while slow and slow.next:
            temp = head.next
            to_order = slow.next

            slow.next = to_order.next
            to_order.next = temp
            head.next = to_order
            head = temp
