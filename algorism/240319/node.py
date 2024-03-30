arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]


class Treenode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, child):
        if not self.left:
            self.left = child
            return

        if not self.right:
            self.right = child
            return

        return

    def inorder(self):
        if self != None:
            if self.left:
                self.left.inorder()

            print(self.value, end=" ")

            if self.right:
                self.right.inorder()


nodes = [Treenode(i) for i in range(14)]

for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i + 1]
    nodes[parent_node].insert(nodes[child_node])

nodes[1].inorder()
