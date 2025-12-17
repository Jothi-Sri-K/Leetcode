# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev=None
        while head!=None:
            if rev==None:
                rev=ListNode(head.val)
                rev.next=None
            else:
                newnode=ListNode(head.val)
                newnode.next=rev
                rev=newnode
            head=head.next
        return rev
        
        