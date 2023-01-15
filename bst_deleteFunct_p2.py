class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return #node already exist

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

        #visit left tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        #visit base node
        elements.append(self.data)

        #vist right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
    print("Building tree with these elements", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':

#for numbers
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 20]
    numbers_tree = build_tree(numbers)
    numbers_tree.delete(20)
    print("After deleting 20 ", numbers_tree.in_order_traversal())

    print("="*60)

#My Name
    myName = ["C", "A", "R", "L", "J", "O", "H", "N", "Z", "O", "L", "E", "T", "A"]
    myName_tree = build_tree(myName)
    myName_tree.delete("R")
    print("After deleting the letter R, the output is: \n", myName_tree.in_order_traversal())