class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root

def printTree(root):
    q ,ans =[],[]
    q.append(root)
    while q :
        cur = q.pop(0)
        if cur:
            q.append(cur.left)
            q.append(cur.right)
            ans.append(cur.val)
        else:
            ans.append('#')
    print (ans)

def createTree(node):
    if node is None or node[0]=='#' : return None
    root , q = TreeNode(node[0]) , []
    q.append(root)
    cur ,  n = q.pop(0),len(node)

    for i in range(1,n):
        if node[i]=='#' :
            if not i & 1:
                cur=q.pop(0)
            continue
        t = TreeNode(node[i])
        q.append(t)
        if i & 1:
            cur.left =  t
        else:
            cur.right = t
            cur = q.pop(0)

    return root

test = Solution()
newRoot = test.invertTree(createTree([4,2,7,1,3,6,9]))


printTree(newRoot)

