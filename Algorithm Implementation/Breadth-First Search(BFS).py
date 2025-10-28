#BFS
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            if node in graph:
                for child in graph[node]:
                    if child not in visited:
                        queue.append(child)
graph = {}
n = int(input("Enter the number of nodes: "))
start_node = input("Enter the start node: ")

for i in range(n):
    node = input("Enter node name: ")
    childs = input(f"Enter childs of {node} separated by space: ").split()
    graph[node] = childs



print("\nBFS Traversal:")
bfs(graph,start_node)
