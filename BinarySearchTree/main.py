# Binary trees are realy just pointer to a root node that in turn connects to each child node
# so we'll run with that idea
class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    
    def insert(self, val):
        if not self.val:
            self.val = val
            
        elif val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)
        elif self.right:
            self.right.insert(val)
        else:
            self.right = BSTNode(val)

bst = BSTNode()
bst.insert(1)
print(bst)