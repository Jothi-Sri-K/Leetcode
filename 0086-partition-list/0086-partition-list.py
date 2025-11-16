# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head = ListNode(0)   # dummy head for nodes < x
        after_head  = ListNode(0)   # dummy head for nodes >= x

        before = before_head
        after = after_head
        curr = head

        while curr:
            next_node = curr.next  # save next
            curr.next = None       # detach to avoid accidental cycles
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = next_node

        # connect the two partitions
        before.next = after_head.next
        return before_head.next
