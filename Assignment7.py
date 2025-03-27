# Problem Statement: You have a business with several offices; you want to lease phone lines 
# to connect them up with each other; and the phone company charges different amounts of 
# money to connect different pairs of cities. You want a set of lines that connects all your 
# offices with a minimum total cost. Solve the problem by suggesting an appropriate data structure.

import heapq

class Graph:
    def __init__(self, num_vertices):
        """ Initialize a graph with given number of offices (vertices) """
        self.num_vertices = num_vertices
        self.edges = []  # For Kruskal's algorithm
        self.adj_list = {i: [] for i in range(num_vertices)}  # For Prim's algorithm
        self.office_names = {}

    def add_office(self, index, name):
        """ Maps an index to an office (city) name """
        self.office_names[index] = name

    def add_connection(self, u, v, cost):
        """ Adds a connection (edge) with cost between two offices """
        self.edges.append((cost, u, v))  # Used in Kruskal's algorithm
        self.adj_list[u].append((cost, v))  # Used in Prim's algorithm
        self.adj_list[v].append((cost, u))  # Undirected graph

    def prims_mst(self):
        """ Computes the Minimum Spanning Tree using Prim's Algorithm """
        visited = [False] * self.num_vertices
        min_heap = [(0, 0)]  # (cost, starting office)
        total_cost = 0
        mst_edges = []

        while len(mst_edges) < self.num_vertices - 1 and min_heap:
            cost, u = heapq.heappop(min_heap)
            if visited[u]:
                continue
            visited[u] = True
            total_cost += cost

            if u != 0:  # Exclude the first node as it has no parent in MST
                mst_edges.append((cost, self.office_names[u]))

            for next_cost, v in self.adj_list[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (next_cost, v))

        print("\nPrim's MST Total Cost:", total_cost)
        print("Selected Connections:", mst_edges)

    def find_parent(self, parent, node):
        """ Finds the parent node in the Disjoint Set (for Kruskal's algorithm) """
        if parent[node] == node:
            return node
        return self.find_parent(parent, parent[node])

    def union(self, parent, rank, u, v):
        """ Performs Union operation in Disjoint Set """
        root_u = self.find_parent(parent, u)
        root_v = self.find_parent(parent, v)
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

    def kruskals_mst(self):
        """ Computes the Minimum Spanning Tree using Kruskal's Algorithm """
        self.edges.sort()  # Sorting edges by cost
        parent = [i for i in range(self.num_vertices)]
        rank = [0] * self.num_vertices
        total_cost = 0
        mst_edges = []

        for cost, u, v in self.edges:
            if self.find_parent(parent, u) != self.find_parent(parent, v):
                self.union(parent, rank, u, v)
                total_cost += cost
                mst_edges.append((cost, self.office_names[u], self.office_names[v]))

        print("\nKruskal's MST Total Cost:", total_cost)
        print("Selected Connections:", mst_edges)


# Driver Code
if __name__ == "__main__":
    num_offices = int(input("Enter the number of offices (nodes): "))
    graph = Graph(num_offices)

    print("Enter office names one by one:")
    for i in range(num_offices):
        name = input(f"Enter name for office {i}: ")
        graph.add_office(i, name)

    num_connections = int(input("Enter the number of possible connections (edges): "))
    print("Enter connections with costs (format: 'office1_index office2_index cost'):")
    for _ in range(num_connections):
        u, v, cost = map(int, input().split())
        graph.add_connection(u, v, cost)

    while True:
        print("\nMenu:")
        print("1. Compute Minimum Spanning Tree using Prim's Algorithm")
        print("2. Compute Minimum Spanning Tree using Kruskal's Algorithm")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            graph.prims_mst()
        elif choice == 2:
            graph.kruskals_mst()
        elif choice == 3:
            break
        else:
            print("Invalid choice! Please enter a valid option.")
