#872. Leaf-Similar Trees

class Solution(object):
    def leafSimilar(self, root1, root2):
        def findleaf(root):
            left = []
            right = []
            if root.left == None and root.right == None:
                return [root.val]
            else:
                if root.left != None:
                    left = findleaf(root.left)
                if root.right != None:
                    right = findleaf(root.right)
                return (left + right)

        leaf1 = findleaf(root1)
        leaf2 = findleaf(root2)

        return leaf1 == leaf2
