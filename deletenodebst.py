#450. Delete Node in a BST

class Solution:
    
    # get the left mode node
    # this will used when we are deleting a node that has both child
    def getLeftMostNode(self, node):
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        # if key is less that value at root, go to left of the root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # if key is more that value at root, go to right of the root
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            # if node has only right 
            # set node to its right and delete node
            if root.left is None:
                temp = root.right
                root = None
                return temp
            
            # if node has only left
            # set node to its left and delete node
            elif root.right is None:
                temp = root.left
                root = None
                return temp
        
            
            # if node has both child
            
            # get the left most child of current node's right child (successor node)
            temp = self.getLeftMostNode(root.right)
            
            # set current node val to its successor node
            root.val = temp.val
            
            # then set the current node's right to node available after deleting its right
            root.right = self.deleteNode(root.right, temp.val)

        return root
