# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode(0, head)
        if not head:
            return 
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = first.next
            first.next = temp
        return first.next