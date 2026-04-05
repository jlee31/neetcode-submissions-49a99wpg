class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or root.val == q.val or root.val == p.val:
            return root
        # Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If p and q are on opposite sides, current node is the LCA
        if left and right:
            return root

        # Otherwise, return whichever side found a result
        if left:
            return left
        else:
            return right