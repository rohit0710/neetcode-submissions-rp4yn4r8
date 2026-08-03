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
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        prev = slow.next
        while prev and prev.next:
            temp = prev.next
            prev.next = temp.next
            temp.next = slow.next
            slow.next = temp
        temp = slow.next
        slow.next = None
        slow = temp
        while slow:
            temp = head.next
            temp2 = slow.next

            head.next = slow
            slow.next = temp
            slow = temp2
            head = temp
        #     print(head.val, head.next.val)

        