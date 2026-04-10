# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = count()
        for l in lists:
            heapq.heappush(heap, (l.val, next(counter), l ))
        dummy = res = ListNode()
        while heap:
            val, _ , node = heapq.heappop(heap)
            res.next = node
            res = res.next
            if node.next:
                heapq.heappush(heap, (node.next.val, next(counter), node.next))
                
        return dummy.next