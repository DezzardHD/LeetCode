"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = {}
        l1 = head
        start = dummy = Node(0)
        while l1:
            l2 = Node(l1.val)
            dummy.next = l2
            dummy = l2
            hm[l1] = l2
            l1 = l1.next

        l1 = head
        dummy = start.next
        while l1:
            if l1.random:
                dummy.random = hm[l1.random]
            dummy = dummy.next
            l1 = l1.next

        return start.next