# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = dummy.next
            dummy.next = temp
        
        return dummy.next
