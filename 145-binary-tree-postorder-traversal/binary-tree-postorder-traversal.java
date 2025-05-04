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

    private List<Integer> res = new ArrayList<Integer>();

    public List<Integer> postorderTraversal(TreeNode root) {
        explore(root);
        return this.res;
    }

    private void explore(TreeNode root) {
        if (root == null) {
            return;
        }
        explore(root.left);
        explore(root.right);
        this.res.add(root.val);
    }
}