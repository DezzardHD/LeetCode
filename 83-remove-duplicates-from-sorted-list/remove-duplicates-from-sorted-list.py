# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res, prev = head, head
        while head:
            if head.next and head.next.val != prev.val:
                setattr(prev, 'next', head.next)
                prev = head.next
            head = head.next
        if prev:
            setattr(prev, 'next', None)
        return res
