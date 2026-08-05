# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(head1, head2):
            dummy = node = ListNode()
            while head1 and head2:
                if head1.val > head2.val:
                    node.next = head2
                    head2 = head2.next
                else:
                    node.next = head1
                    head1 = head1.next
                node = node.next
            
            if head1:
                node.next = head1
            
            if head2:
                node.next = head2

            return dummy.next
        if not lists or len(lists) == 0:
            return 
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                head1 = lists[i]
                head2 = lists[i+1] if (i+1) < len(lists) else None
                merged.append(mergeLists(head1, head2))
            lists = merged
        return lists[0]