class Node:
    def __init__(self, value, right, left):
        self.value: int = value
        self.right: Node = right
        self.left: Node = left

    def insert_node(self, value: int):
        if self.value is not None:
            if self.value < value:
                if self.right is None:
                    self.right = Node(value, None, None)
                else:
                    self.right.insert_node(value)
            if self.value > value:
                if self.left is None:
                    self.left = Node(value, None, None)
                else:
                    self.left.insert_node(value)
        else:
            self.value = value

    def search(self, value) -> bool:
        if self.value == value:
            return True
        else:
            if self.value < value and self.right is not None:
                return self.right.search(value)
            if self.value > value and self.left is not None:
                return self.left.search(value)
            else:
                return False

    def print(self):
        if self.left:
            self.left.print()
        print(self.value),
        if self.right:
            self.right.print()


tree = Node(None, None, None)
tree.insert_node(2)
tree.insert_node(7)
tree.insert_node(19)
tree.insert_node(4)
print(tree.search(21))
tree.print()
