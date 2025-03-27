# Problem Statement:
# Beginning with an empty binary search tree, construct a binary search tree by inserting
# the values in the order given. After constructing the binary tree:
# a) Insert a node
# b) Search for a key value and output whether it is found or not

class Node:
    """Class representing a node in a binary search tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """Class representing a Binary Search Tree (BST)."""
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        """Inserts a key into the BST."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        """Helper function to insert a key recursively."""
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)
    
    def search(self, key):
        """Searches for a key in the BST and returns True if found, otherwise False."""
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        """Helper function to search for a key recursively."""
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)
    
    def inorder_traversal(self, node):
        """Performs an in-order traversal and prints the BST keys."""
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.key, end=" ")
            self.inorder_traversal(node.right)
    
if __name__ == "__main__":
    bst = BST()
    
    while True:
        print("\nMenu:")
        print("1. Insert node")
        print("2. Search for a key")
        print("3. Display BST in-order")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            key = int(input("Enter value to insert: "))
            bst.insert(key)
        elif choice == 2:
            key = int(input("Enter value to search: "))
            print("Found" if bst.search(key) else "Not Found")
        elif choice == 3:
            print("BST in-order traversal:")
            bst.inorder_traversal(bst.root)
            print()
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
