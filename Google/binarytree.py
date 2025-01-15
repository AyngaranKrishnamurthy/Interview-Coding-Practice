class Node(object):
    def __init__(self,val):
        self.value = val
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)