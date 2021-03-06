
#represents individual node in BST
class Node:
    def __init__(self, d, idx):
        self.index = idx
        self.val = d
        self.left = None
        self.right = None

    def insert(self, d, idx):
        if self.val == d:
            return False
        elif d < self.val:
            if self.left:
                return self.left.insert(d, idx)
            else:
                self.left = Node(d, idx)
                return True
        else:
            if self.right:
                return self.right.insert(d, idx)
            else:
                self.right = Node(d, idx)
                return True

    def inorder(self, l):
        if self.left:
            self.left.inorder(l)
        l.append(self.val)
        if self.right:
            self.right.inorder(l)
        return l

    def find(self, d):
        if self.val == d:
            return self.index
        elif d < self.val and self.left:
            return self.left.find(d)
        elif d > self.val and self.right:
            return self.right.find(d)
        return False

class BST:

    def __init__(self):
        self.root = None
        self.idx = 0

    def insert(self, val):
        if self.root:
            self.idx+=1
            return self.root.insert(val, self.idx)
        else:
            self.root = Node(val, self.idx)
            return True

    def inorder(self):
        if self.root:
            return self.root.inorder([])
        else:
            return []

    def find(self, d):
        if self.root:
            return self.root.find(d)
        else:
            return False