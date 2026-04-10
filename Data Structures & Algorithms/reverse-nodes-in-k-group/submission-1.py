# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def can_reverse(head, curr_count):
            count = 0
            if curr_count == 0:
                while head and count < k:
                    head = head.next
                    count += 1
                    print(count)

                if count == k:
                    return True
                else:
                    return False
            return True
        if k == 1:
            return head
            
        dummy = prev = ListNode(0, head)
        run = 0
        while head and head.next:
            if can_reverse(head, run):
                temp = head.next
                head.next = temp.next
                temp.next = prev.next
                prev.next = temp
                run += 1
                if run == k-1:
                    prev = head
                    head = head.next
                    run = 0
            else:
                break

        return dummy.next