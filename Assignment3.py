class Node:
    """Class representing a node in the binary search tree."""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """Binary Search Tree implementation."""
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserts a new key into the BST."""
        self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node
    
    def search(self, key):
        """Searches for a key in the BST."""
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def delete(self, key):
        """Deletes a key from the BST."""
        self.root = self._delete(self.root, key)
    
    def _delete(self, node, key):
        if node is None:
            return node
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)
        return node
    
    def _min_value_node(self, node):
        """Finds the node with the minimum value in the BST."""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder(self):
        """Displays the BST in In-Order traversal."""
        self._inorder(self.root)
        print()
    
    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)
    
    def preorder(self):
        """Displays the BST in Pre-Order traversal."""
        self._preorder(self.root)
        print()
    
    def _preorder(self, node):
        if node:
            print(node.key, end=' ')
            self._preorder(node.left)
            self._preorder(node.right)
    
    def postorder(self):
        """Displays the BST in Post-Order traversal."""
        self._postorder(self.root)
        print()
    
    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key, end=' ')
    
if __name__ == "__main__":
    bst = BST()
    
    while True:
        print("\nMenu:")
        print("1. Insert an element")
        print("2. Search for an element")
        print("3. Delete an element")
        print("4. Display In-Order")
        print("5. Display Pre-Order")
        print("6. Display Post-Order")
        print("7. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            key = int(input("Enter element to insert: "))
            bst.insert(key)
        elif choice == 2:
            key = int(input("Enter element to search: "))
            result = bst.search(key)
            print("Element found" if result else "Element not found")
        elif choice == 3:
            key = int(input("Enter element to delete: "))
            bst.delete(key)
            print("Element deleted successfully")
        elif choice == 4:
            print("In-Order Traversal:")
            bst.inorder()
        elif choice == 5:
            print("Pre-Order Traversal:")
            bst.preorder()
        elif choice == 6:
            print("Post-Order Traversal:")
            bst.postorder()
        elif choice == 7:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
