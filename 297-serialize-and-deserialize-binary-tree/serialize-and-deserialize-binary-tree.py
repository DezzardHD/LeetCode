# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # preorder traversal
        res = ""
        def preorder(node):        
            nonlocal res
            if not node:
                res = res + "#"
                return
            res = res + "#" + str(node.val)
            preorder(node.left)
            preorder(node.right)
            return
        preorder(root)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = [None if not x else int(x) for x in data.split("#")]
        print(arr)
        def preorder_build(idx: int) -> (Optional[TreeNode], int):
            nonlocal arr
            if len(arr) <= idx or arr[idx] == None:
                return None, idx + 1
            node = TreeNode(arr[idx])
            idx += 1
            node.left, idx = preorder_build(idx)
            node.right, idx = preorder_build(idx)
            return node, idx
        root, idx = preorder_build(1)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))