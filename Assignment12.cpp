// Problem Statement: A dictionary stores keywords and meanings. Provide facility for:
// 1. Adding new keywords
// 2. Deleting keywords
// 3. Updating values of any entry
// 4. Displaying data in ascending/descending order
// 5. Finding the maximum number of comparisons required for searching a keyword
// Use an AVL tree for height balancing.

#include <iostream>
#include <string>
using namespace std;

// Node structure for AVL tree
struct Node {
    string keyword;
    string meaning;
    Node* left;
    Node* right;
    int height;

    Node(string key, string value) {
        keyword = key;
        meaning = value;
        left = right = nullptr;
        height = 1;
    }
};

// Function to get the height of a node
int getHeight(Node* node) {
    return (node == nullptr) ? 0 : node->height;
}

// Function to calculate balance factor
int getBalanceFactor(Node* node) {
    return (node == nullptr) ? 0 : getHeight(node->left) - getHeight(node->right);
}

// Right rotation for balancing
Node* rotateRight(Node* y) {
    Node* x = y->left;
    Node* T = x->right;

    x->right = y;
    y->left = T;

    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;
    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;

    return x;
}

// Left rotation for balancing
Node* rotateLeft(Node* x) {
    Node* y = x->right;
    Node* T = y->left;

    y->left = x;
    x->right = T;

    x->height = max(getHeight(x->left), getHeight(x->right)) + 1;
    y->height = max(getHeight(y->left), getHeight(y->right)) + 1;

    return y;
}

// Insert a keyword into the AVL tree
Node* insert(Node* root, string key, string value) {
    if (root == nullptr)
        return new Node(key, value);

    if (key < root->keyword)
        root->left = insert(root->left, key, value);
    else if (key > root->keyword)
        root->right = insert(root->right, key, value);
    else {
        root->meaning = value; // Update meaning if keyword already exists
        return root;
    }

    // Update height
    root->height = max(getHeight(root->left), getHeight(root->right)) + 1;

    // Get balance factor and perform rotations if needed
    int balance = getBalanceFactor(root);

    // Left Heavy (Right Rotation)
    if (balance > 1 && key < root->left->keyword)
        return rotateRight(root);

    // Right Heavy (Left Rotation)
    if (balance < -1 && key > root->right->keyword)
        return rotateLeft(root);

    // Left-Right Heavy (Left-Right Rotation)
    if (balance > 1 && key > root->left->keyword) {
        root->left = rotateLeft(root->left);
        return rotateRight(root);
    }

    // Right-Left Heavy (Right-Left Rotation)
    if (balance < -1 && key < root->right->keyword) {
        root->right = rotateRight(root->right);
        return rotateLeft(root);
    }

    return root;
}

// Find the node with the minimum key value (used for deletion)
Node* minValueNode(Node* node) {
    Node* current = node;
    while (current->left != nullptr)
        current = current->left;
    return current;
}

// Delete a keyword from the AVL tree
Node* deleteNode(Node* root, string key) {
    if (root == nullptr)
        return root;

    if (key < root->keyword)
        root->left = deleteNode(root->left, key);
    else if (key > root->keyword)
        root->right = deleteNode(root->right, key);
    else {
        // Node with only one child or no child
        if (root->left == nullptr || root->right == nullptr) {
            Node* temp = (root->left) ? root->left : root->right;
            delete root;
            return temp;
        }

        // Node with two children: Get the inorder successor (smallest in right subtree)
        Node* temp = minValueNode(root->right);
        root->keyword = temp->keyword;
        root->meaning = temp->meaning;
        root->right = deleteNode(root->right, temp->keyword);
    }

    // Update height
    root->height = max(getHeight(root->left), getHeight(root->right)) + 1;

    // Get balance factor
    int balance = getBalanceFactor(root);

    // Perform rotations if unbalanced
    if (balance > 1 && getBalanceFactor(root->left) >= 0)
        return rotateRight(root);

    if (balance > 1 && getBalanceFactor(root->left) < 0) {
        root->left = rotateLeft(root->left);
        return rotateRight(root);
    }

    if (balance < -1 && getBalanceFactor(root->right) <= 0)
        return rotateLeft(root);

    if (balance < -1 && getBalanceFactor(root->right) > 0) {
        root->right = rotateRight(root->right);
        return rotateLeft(root);
    }

    return root;
}

// Search for a keyword in the AVL tree
bool search(Node* root, string key, int& comparisons) {
    comparisons++;
    if (root == nullptr)
        return false;

    if (key == root->keyword)
        return true;
    else if (key < root->keyword)
        return search(root->left, key, comparisons);
    else
        return search(root->right, key, comparisons);
}

// Display dictionary in ascending order (inorder traversal)
void inorder(Node* root) {
    if (root != nullptr) {
        inorder(root->left);
        cout << root->keyword << " : " << root->meaning << endl;
        inorder(root->right);
    }
}

// Display dictionary in descending order (reverse inorder traversal)
void reverseInorder(Node* root) {
    if (root != nullptr) {
        reverseInorder(root->right);
        cout << root->keyword << " : " << root->meaning << endl;
        reverseInorder(root->left);
    }
}

// Main function to handle user input
int main() {
    Node* root = nullptr;
    int choice;
    string key, meaning;

    do {
        cout << "\nDictionary Operations:\n";
        cout << "1. Add a keyword\n2. Delete a keyword\n3. Search for a keyword\n4. Display (Ascending)\n5. Display (Descending)\n6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                cout << "Enter keyword: ";
                cin >> key;
                cout << "Enter meaning: ";
                cin.ignore();
                getline(cin, meaning);
                root = insert(root, key, meaning);
                break;

            case 2:
                cout << "Enter keyword to delete: ";
                cin >> key;
                root = deleteNode(root, key);
                break;

            case 3:
                int comparisons = 0;
                cout << "Enter keyword to search: ";
                cin >> key;
                if (search(root, key, comparisons))
                    cout << "Keyword found! Comparisons: " << comparisons << endl;
                else
                    cout << "Keyword not found! Comparisons: " << comparisons << endl;
                break;

            case 4:
                cout << "Dictionary in Ascending Order:\n";
                inorder(root);
                break;

            case 5:
                cout << "Dictionary in Descending Order:\n";
                reverseInorder(root);
                break;

            case 6:
                cout << "Exiting program...\n";
                break;

            default:
                cout << "Invalid choice! Try again.\n";
        }
    } while (choice != 6);

    return 0;
}
