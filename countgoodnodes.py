#1448. Count Good Nodes in Binary Tree

class Solution:
    def goodNodes(self, root):
        if not root:
            return 0
        
        def dfs(node, curMax):
            if not node:
                return
            if node.val >= curMax:
                count[0] += 1
                curMax = node.val
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        
        count = [0]
        dfs(root, root.val)
        
        return count[0]
