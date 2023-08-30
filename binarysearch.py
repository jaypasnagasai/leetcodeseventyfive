#700. Search in a Binary Search Tree

class Solution:
  def searchBST(self, root, val):
    if not root:
      return None
    if root.val == val:
      return root
    if root.val > val:
      return self.searchBST(root.left, val)
    return self.searchBST(root.right, val)
