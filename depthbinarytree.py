#104. Maximum Depth of Binary Tree

class Solution:
    def maxDepth(self, root):
        self.maximum=0
        if root==None:
            return 0
        def topToBottom(node, depth):
            if not node.left and not node.right:
                self.maximum=max(self.maximum, depth+1)
            if node.left:
                topToBottom(node.left, depth+1)
            if node.right:
                topToBottom(node.right, depth+1)
        topToBottom(root, 0)
        return self.maximum
