/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    private List<Integer> res = new ArrayList();
    
    public List<Integer> preorderTraversal(TreeNode root) {
        explore(root);
        return res;
    }

    private void explore(TreeNode root) {
        if (root == null) {
            return;
        }
        res.add(root.val);
        explore(root.left);
        explore(root.right);
    }
}