# Problem Statement: Represent a given graph using adjacency matrix/list to perform DFS  
# using adjacency list to perform BFS. Use the map of the area around the college as the  
# graph. Identify the prominent landmarks as nodes and perform DFS and BFS on that.

from collections import deque

class Graph:
    def __init__(self, num_vertices):
        """ Initialize the graph with an adjacency list and adjacency matrix """
        self.num_vertices = num_vertices
        self.adj_list = {i: [] for i in range(num_vertices)}  # For BFS
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]  # For DFS
        self.landmarks = {}

    def add_landmark(self, index, name):
        """ Maps an index to a landmark name """
        self.landmarks[index] = name

    def add_edge(self, u, v):
        """ Adds an edge between two nodes in both adjacency list and matrix """
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Assuming an undirected graph
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def bfs(self, start):
        """ Performs Breadth-First Search (BFS) using an adjacency list """
        visited = [False] * self.num_vertices
        queue = deque([start])
        visited[start] = True
        print("BFS Traversal:")

        while queue:
            node = queue.popleft()
            print(self.landmarks.get(node, node), end=" -> ")

            for neighbor in self.adj_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print("END\n")

    def dfs_util(self, node, visited):
        """ Helper function for DFS using an adjacency matrix """
        visited[node] = True
        print(self.landmarks.get(node, node), end=" -> ")

        for neighbor in range(self.num_vertices):
            if self.adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        """ Performs Depth-First Search (DFS) using an adjacency matrix """
        visited = [False] * self.num_vertices
        print("DFS Traversal:")
        self.dfs_util(start, visited)
        print("END\n")

    def display_graph(self):
        """ Displays the adjacency list representation of the graph """
        print("\nGraph Representation (Adjacency List):")
        for node in self.adj_list:
            print(self.landmarks.get(node, node), "->", [self.landmarks.get(n, n) for n in self.adj_list[node]])


# Driver Code
if __name__ == "__main__":
    num_nodes = int(input("Enter the number of landmarks (nodes): "))
    graph = Graph(num_nodes)

    print("Enter landmarks one by one:")
    for i in range(num_nodes):
        name = input(f"Enter name for landmark {i}: ")
        graph.add_landmark(i, name)

    num_edges = int(input("Enter the number of roads (edges): "))
    print("Enter edges (landmark indexes, e.g., '0 1' for a road between landmark 0 and 1):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    while True:
        print("\nMenu:")
        print("1. Display Graph")
        print("2. Perform BFS")
        print("3. Perform DFS")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            graph.display_graph()
        elif choice == 2:
            start = int(input("Enter the starting landmark index for BFS: "))
            graph.bfs(start)
        elif choice == 3:
            start = int(input("Enter the starting landmark index for DFS: "))
            graph.dfs(start)
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
