# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        speed = head.next
        while speed:
            if head == speed:
                return True
            head = head.next
            if speed.next and speed.next.next:
                speed = speed.next.next
            else:
                return False
        return False