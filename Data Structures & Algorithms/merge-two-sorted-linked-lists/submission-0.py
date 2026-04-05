# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        
        dummy = ListNode(0)
        out = dummy
        
        while head1 is not None and head2 is not None:
            if head1.val <= head2.val:
                out.next = head1
                head1 = head1.next
            else:
                out.next = head2
                head2 = head2.next
            out = out.next
        
        while head1 is not None:
            out.next = head1
            head1 = head1.next
            out = out.next
        
        while head2 is not None:
            out.next = head2
            head2 = head2.next
            out = out.next
        
        return dummy.next
        