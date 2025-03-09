# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # handle cases where list size is greater than one
        slow, fast = head, head.next
        prev = None
        while fast:
            fast = fast.next
            n -= 1
            if n <= 0:
                prev = slow
                slow = slow.next
        if prev:
            prev.next = slow.next
            return head
        else:
            # if the value of n is the same as the amount of nodes present in the linked list
            return slow.next