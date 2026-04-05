# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        curr = head
        while curr:
            stk.append(curr.val)
            curr = curr.next

        dummy = ListNode(0)
        curr = dummy
        while stk:
            curr.next = ListNode(stk.pop())
            curr = curr.next
        head = dummy.next
        return head


