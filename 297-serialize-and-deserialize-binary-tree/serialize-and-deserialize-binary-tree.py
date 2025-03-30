class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
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
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = [None if not x else int(x) for x in data.split("#")]
        def preorder_build(idx: int) -> (Optional[TreeNode], int):
            nonlocal arr
            if len(arr) <= idx or None == arr[idx]:
                return None, idx + 1
            node = TreeNode(arr[idx])
            idx += 1
            node.left, idx = preorder_build(idx)
            node.right, idx = preorder_build(idx)
            return node, idx
        root, idx = preorder_build(1)
        return root