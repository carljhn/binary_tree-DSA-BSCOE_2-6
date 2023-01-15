#class BinarySearchTreeNode

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return 

        if data < self.data:
            # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else: 
            # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        
        # visits left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # visits the base node
        elements.append(self.data)

        # visits right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

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

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 1]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.search(20))
    print(numbers_tree.in_order_traversal())
    print("="*40)

    myName = ["C", "A", "R", "L", "J", "O", "H", "N", "Z", "O", "L", "E", "T", "A"]
    myName_tree = build_tree(myName)
    print("Does L exists in the list?: ", myName_tree.search("L"))
    print("Does M exists in the list?: ", myName_tree.search("M"))
    print(myName_tree.in_order_traversal())