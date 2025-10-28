
# Depth First Search (DFS)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    # Print the current node
    print(start, end=" ")
    visited.add(start)

    # Visit all unvisited neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Taking graph input from user
graph = {}
n = int(input("Enter the number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
    graph[node] = neighbors

start_node = input("Enter the start node: ")

print("\nDFS Traversal:")
dfs(graph, start_node)

