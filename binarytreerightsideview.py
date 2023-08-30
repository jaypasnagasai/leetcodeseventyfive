#199. Binary Tree Right Side View

class Solution:
    def rightSideView(self, root):
        if root==None:
            return []
        q=deque([[root,0]])
        d={}
        while q:
            node,line=q.popleft()
            d[line]=node.val
            if node.left:
                q.append([node.left,line+1])
            if node.right:
                q.append([node.right,line+1])
        ans=[]
        for k in sorted(d):
            ans.append(d[k])
        return ans
