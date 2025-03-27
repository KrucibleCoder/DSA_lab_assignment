#Problem Statement: Consider telephone book database on N clients. Make use of a hash 
#table implementation to quickly look up client’s telephone number. Make use of two 
#collision handling techniques and compare them using number of comparisons required to 
#find a set of telephone numbers. 
#table implementation to quickly look up client’s telephone number. Make use of two 
#collision handling techniques and compare them using number of comparisons required to 
#find a set of telephone numbers.

class Node:
    """Class representing a node in the Expression Tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree:
    """Class for constructing and evaluating an Expression Tree."""
    def __init__(self):
        self.root = None
    
    def construct_tree(self, postfix):
        """Constructs an expression tree from a given postfix expression."""
        stack = []
        for char in postfix:
            if char.isalnum():  # If operand, create node and push to stack
                stack.append(Node(char))
            else:  # If operator, pop two nodes, create new node and push back
                node = Node(char)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)
        self.root = stack.pop()
    
    def inorder_traversal(self, node):
        """Performs in-order traversal of the expression tree."""
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)
    
    def preorder_traversal(self, node):
        """Performs pre-order traversal of the expression tree."""
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def postorder_traversal(self, node):
        """Performs post-order traversal of the expression tree."""
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')
    
if __name__ == "__main__":
    exp_tree = ExpressionTree()
    postfix_expr = input("Enter a postfix expression: ")
    exp_tree.construct_tree(postfix_expr)
    
    while True:
        print("\nMenu:")
        print("1. Display In-Order Traversal")
        print("2. Display Pre-Order Traversal")
        print("3. Display Post-Order Traversal")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("In-Order Traversal:")
            exp_tree.inorder_traversal(exp_tree.root)
            print()
        elif choice == 2:
            print("Pre-Order Traversal:")
            exp_tree.preorder_traversal(exp_tree.root)
            print()
        elif choice == 3:
            print("Post-Order Traversal:")
            exp_tree.postorder_traversal(exp_tree.root)
            print()
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
