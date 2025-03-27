# Problem Statement:
# Convert a given Binary Tree into a Threaded Binary Tree.

class TreeNode:
    """Class representing a node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.is_threaded = False  # Indicates if right pointer is a thread

class ThreadedBinaryTree:
    """Class representing a Threaded Binary Tree."""
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Inserts a node into the binary tree."""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        """Helper function to insert nodes recursively."""
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    def convert_to_threaded(self):
        """Converts the binary tree into a threaded binary tree."""
        def threaded_inorder(node, prev):
            if node:
                prev = threaded_inorder(node.left, prev)
                if prev and prev.right is None:
                    prev.right = node
                    prev.is_threaded = True
                prev = node
                return threaded_inorder(node.right, prev)
            return prev
        threaded_inorder(self.root, None)
    
    def inorder_traversal(self):
        """Performs an inorder traversal of the threaded binary tree."""
        current = self.root
        while current and current.left:
            current = current.left
        
        while current:
            print(current.value, end=" ")
            if current.is_threaded:
                current = current.right
            else:
                current = self._leftmost(current.right)
        print()
    
    def _leftmost(self, node):
        """Finds the leftmost node in a tree."""
        while node and node.left:
            node = node.left
        return node
    
    def display_relationships(self, node, parent=None):
        """Displays the parent-child relationships in the tree."""
        if node:
            parent_info = f"Parent: {parent.value}" if parent else "Root Node"
            left_info = f"Left Child: {node.left.value}" if node.left else "No Left Child"
            right_info = f"Right Child: {node.right.value}" if node.right and not node.is_threaded else "No Right Child"
            thread_info = f"Threaded to: {node.right.value}" if node.is_threaded else "Not Threaded"
            
            print(f"Node {node.value}: {parent_info}, {left_info}, {right_info}, {thread_info}")
            self.display_relationships(node.left, node)
            if not node.is_threaded:
                self.display_relationships(node.right, node)
    
if __name__ == "__main__":
    tbt = ThreadedBinaryTree()
    
    while True:
        print("\nMenu:")
        print("1. Insert node")
        print("2. Convert to Threaded Binary Tree")
        print("3. Perform Inorder Traversal")
        print("4. Display Node Relationships")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            value = int(input("Enter value to insert: "))
            tbt.insert(value)
        elif choice == 2:
            tbt.convert_to_threaded()
            print("Tree converted to Threaded Binary Tree.")
        elif choice == 3:
            print("Inorder Traversal of Threaded Binary Tree:")
            tbt.inorder_traversal()
        elif choice == 4:
            print("Node Relationships:")
            tbt.display_relationships(tbt.root)
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
