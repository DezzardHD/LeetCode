# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return
        
        tail_list1 = slow = fast = head
        while fast and fast.next:
            tail_list1 = slow
            slow = slow.next
            fast = fast.next.next
            #print("slow: {}".format(slow.val))
            #print("fast: {}".format(fast.val if fast else None))
        setattr(tail_list1, 'next', None)

        #print("head")
        #while head:
        #    print(head.val)
        #    head = head.next

        #print("slow")
        #while slow:
        #    print(slow.val)
        #    slow = slow.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        #print("prev")
        #while prev:
        #    print(prev.val)
        #    prev = prev.next

        start = dummy = ListNode()
        while head:
            dummy.next = head
            head = head.next
            dummy = dummy.next
            dummy.next = prev
            prev = prev.next
            dummy = dummy.next
        if prev:
            dummy.next = prev
        head = start.next

        #dummy = head
        #while dummy:
        #    print(dummy.val)
        #    dummy = dummy.next