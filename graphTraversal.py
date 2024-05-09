# Implementation of DFS(recursive) and BFS

from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, value):
        if value not in self.adj_list:
            self.adj_list[value] = []

    def add_edge(self, src, dest):
        self.add_node(src)
        self.add_node(dest)
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def dfs(self, vertex, visited = None):
        if visited is None:
            visited = set()

        if vertex not in self.adj_list or vertex in visited:
            return []

        visited.add(vertex)
        result = [vertex]
        for neighbor in self.adj_list[vertex]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
         
        return result

    def bfs(self, start_node):
        if start_node not in self.adj_list:
            return []
        visited = set()
        queue = deque()
        queue.append(start_node)
        result = []
        while queue:
            curr = queue.pop()
            if curr not in visited:
                visited.add(curr)
                result.append(curr)

                for neighbor in self.adj_list[curr]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result

graph = Graph()

n = int(input("Enter the number of edges in the graph: "))
print("Enter the edges (source destination):")
for i in range(n):
    src, dest = input().split()
    graph.add_edge(src, dest)

start_node = input("enter the starting node: ")
dfs_result = graph.dfs(start_node)
print("DFS Recursive Traversal:", dfs_result)

bfs_result = graph.bfs(start_node)
print("BFS Traversal:", bfs_result)

