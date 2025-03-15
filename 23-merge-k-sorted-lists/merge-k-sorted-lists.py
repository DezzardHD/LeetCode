# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = dummy = ListNode()
        while True:
            minNode = -1
            for idx, ls in enumerate(lists):
                if not ls:
                    continue
                if minNode == -1 or lists[minNode].val > ls.val:
                    minNode = idx
            if minNode == -1:
                break
            dummy.next = lists[minNode]
            dummy = dummy.next
            lists[minNode] = lists[minNode].next
        return res.next