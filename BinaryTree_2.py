class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self,data):
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

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

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
            
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete (val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_min()
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
     
    
def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])
        
    for i in range (1,len(elements)):
        root.add_child(elements[i])

    return root   

if __name__ == '__main__':
    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("J")
    print("After deleting J", names_tree.in_order_traversal())

    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("U")
    print("After deleting U", names_tree.in_order_traversal())

    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("S")
    print("After deleting S", names_tree.in_order_traversal())

    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("T")
    print("After deleting T", names_tree.in_order_traversal())

    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("E")
    print("After deleting E", names_tree.in_order_traversal())

    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("N")
    print("After deleting N", names_tree.in_order_traversal())

    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("I")
    print("After deleting I", names_tree.in_order_traversal())

    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("C")
    print("After deleting C", names_tree.in_order_traversal())

    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("A")
    print("After deleting A", names_tree.in_order_traversal())

    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("O")
    print("After deleting O", names_tree.in_order_traversal()) 

    names_tree = build_tree(["J", "U", "S", "T", "E", "N", "N", "I", "C", "A", "N", "O", "R"])
    names_tree.delete("R")
    print("After deleting R", names_tree.in_order_traversal())    



    