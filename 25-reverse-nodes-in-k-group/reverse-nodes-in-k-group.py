# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = dummy = ListNode(0, head)
        while dummy:
            dummy = self.logic(dummy.next, dummy, k)
        return res.next

    def logic(self, node, node_prev_group, k):
        # reverse until k nodes were reverse
        k_tmp, last_node, head_node_next_group = self.reverse(node, k)
        # undo the reverse if a group is uncomplete (i.e. there are less than k elements present in the list)
        if(k_tmp != 0):
            self.reverse(last_node, k-k_tmp)
            return head_node_next_group
        # connect last visited node with previous group (no matter what)
        node_prev_group.next = last_node
        # connect the last element of our current reversed group to the next group
        node.next = head_node_next_group  
        # return node from next group -> Some/None
        return node

    def reverse(self, node, k) -> (int, ListNode, ListNode):
        prev = None
        while k != 0 and node:
            k -= 1
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return (k, prev, node)

# sub-problems
# - reversing k nodes within a group
# - connecting two groups