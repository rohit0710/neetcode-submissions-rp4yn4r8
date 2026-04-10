# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, list1)
        prev = dummy
        while list1 and list2:
            if list1.val < list2.val:
                list1 = list1.next
                prev = prev.next
            else:
                temp = list2
                list2 = list2.next
                temp.next = prev.next
                prev.next = temp
                list1 = temp

        if list2:
            prev.next = list2
            
        return dummy.next
        
