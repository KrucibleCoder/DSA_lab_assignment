// Problem Statement: Given a sorted sequence of keys with search probabilities, 
// construct an Optimal Binary Search Tree (OBST) to minimize search cost.

#include <iostream>
#include <vector>
#include <limits>

using namespace std;

// Function to construct an Optimal Binary Search Tree
void optimalBST(vector<int>& keys, vector<float>& prob, int n) {
    vector<vector<float>> cost(n + 1, vector<float>(n + 1, 0)); // Cost matrix
    vector<vector<int>> root(n + 1, vector<int>(n + 1, 0));     // Root matrix

    // Cumulative probability sum array
    vector<float> sumProb(n + 1, 0);
    for (int i = 1; i <= n; i++)
        sumProb[i] = sumProb[i - 1] + prob[i - 1];

    // Fill the diagonal elements (single node trees)
    for (int i = 0; i < n; i++)
        cost[i][i] = prob[i];

    // Compute the cost for trees of increasing size
    for (int L = 2; L <= n; L++) { // L is the chain length
        for (int i = 0; i <= n - L; i++) {
            int j = i + L - 1;
            cost[i][j] = numeric_limits<float>::max();

            // Try making each key in range i to j as root
            for (int r = i; r <= j; r++) {
                float leftCost = (r > i) ? cost[i][r - 1] : 0;
                float rightCost = (r < j) ? cost[r + 1][j] : 0;
                float totalCost = leftCost + rightCost + sumProb[j + 1] - sumProb[i];

                // Select the root with the minimum cost
                if (totalCost < cost[i][j]) {
                    cost[i][j] = totalCost;
                    root[i][j] = r;
                }
            }
        }
    }

    // Display the computed cost matrix
    cout << "\nOptimal BST Cost Table:\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i <= j)
                cout << cost[i][j] << "\t";
            else
                cout << " - \t";
        }
        cout << endl;
    }

    cout << "\nMinimum Cost of Optimal BST: " << cost[0][n - 1] << endl;
}

// Main function to take input and call the OBST function
int main() {
    int n;
    cout << "Enter number of keys: ";
    cin >> n;

    vector<int> keys(n);
    vector<float> prob(n);

    cout << "Enter sorted keys: ";
    for (int i = 0; i < n; i++)
        cin >> keys[i];

    cout << "Enter search probabilities for each key: ";
    for (int i = 0; i < n; i++)
        cin >> prob[i];

    // Construct the Optimal Binary Search Tree
    optimalBST(keys, prob, n);

    return 0;
}
