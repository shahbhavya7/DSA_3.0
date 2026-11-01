class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = []
        
        def dfs(node):
            if not node:
                res.append("null")
                return
                
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        vals = data.split(",") # converts the string into a list of values, vals is list 
        self.i = 0
        
        def dfs():
            if vals[self.i] == "null": # if the value is "null", it means there is no node, so we return None, i.e. go up the tree in the recursion
                self.i += 1
                return None
            
            node = TreeNode(int(vals[self.i])) # create a new TreeNode with the current value, and then recursively build its left and right children
            self.i += 1
            node.left = dfs() # recursively call dfs to build the left subtree for the current node
            node.right = dfs()
            return node # at the end of the recursion, we return the constructed node, which will be linked to its parent in the previous recursive call
        return dfs() # we start the recursion from the root node, which is the first value in the list vals
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))