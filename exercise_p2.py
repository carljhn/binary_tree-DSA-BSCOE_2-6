class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return 

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree(["C", "A", "R", "L", "J", "O", "H", "N", "Z", "O", "L", "E", "T", "A"])
    numbers_tree.delete("J")
    print("After deleting J: \n", numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]
    print()
    print("="*60)
    print()
    numbers_tree = build_tree(["C", "A", "R", "L", "J", "O", "H", "N", "Z", "O", "L", "E", "T", "A"])
    numbers_tree.delete("R")
    print("After deleting R: \n", numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]
    print()
    print("="*60)
    print()
    numbers_tree = build_tree(["C", "A", "R", "L", "J", "O", "H", "N", "Z", "O", "L", "E", "T", "A"])
    numbers_tree.delete("O")
    print("After deleting O: \n", numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]