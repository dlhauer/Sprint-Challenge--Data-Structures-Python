class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = BinarySearchTree(value)
        if value < self.value:
            if not self.left:
                self.left = node
            else:
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = node
            else:
                self.right.insert(value)
        else:
            return

    def contains(self, target):
        if not self.value:
            return False
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False