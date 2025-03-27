# Problem Statement:
# Construct an expression tree from the given prefix expression and
# traverse it using postorder traversal (non-recursive), and then delete the entire tree.

class TreeNode:
    """Class representing a node in the expression tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    """Class representing an expression tree."""
    def __init__(self):
        self.root = None
    
    def construct_from_prefix(self, prefix_expr):
        """Constructs an expression tree from a given prefix expression."""
        stack = []
        for symbol in reversed(prefix_expr.split()):
            node = TreeNode(symbol)
            if symbol.isalnum():  # Operand
                stack.append(node)
            else:  # Operator
                node.left = stack.pop()
                node.right = stack.pop()
                stack.append(node)
        self.root = stack.pop()
    
    def postorder_traversal(self):
        """Performs a non-recursive postorder traversal of the tree."""
        if self.root is None:
            return []
        stack1, stack2 = [self.root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        return [node.value for node in reversed(stack2)]
    
    def delete_tree(self):
        """Deletes the entire tree by setting the root to None."""
        self.root = None
        print("Tree deleted successfully.")
    
if __name__ == "__main__":
    expr_tree = ExpressionTree()
    
    while True:
        print("\nMenu:")
        print("1. Construct Expression Tree from Prefix Expression")
        print("2. Perform Postorder Traversal (Non-Recursive)")
        print("3. Delete Entire Tree")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            prefix_expr = input("Enter a prefix expression (space-separated): ")
            expr_tree.construct_from_prefix(prefix_expr)
            print("Expression tree constructed successfully.")
        elif choice == 2:
            traversal_result = expr_tree.postorder_traversal()
            print("Postorder Traversal:", traversal_result)
        elif choice == 3:
            expr_tree.delete_tree()
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
