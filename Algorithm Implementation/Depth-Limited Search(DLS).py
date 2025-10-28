
# Depth Limited Search (DLS)

def dls(graph, start, goal, limit, depth=0):
    print(start, end=" ")
    
    # Goal test
    if start == goal:
        return True
    
    # Depth limit check
    if depth >= limit:
        return False

    # Explore neighbors
    for neighbor in graph.get(start, []):
        found = dls(graph, neighbor, goal, limit, depth + 1)
        if found:
            return True
    return False


# ----- User Input -----
graph = {}
n = int(input("Number of nodes: "))

for _ in range(n):
    node = input("Node name: ")
    neighbors = input(f"Neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Start node: ")
goal = input("Goal node: ")
limit = int(input("Depth limit: "))

print("\nDepth-Limited Search Traversal:")
found = dls(graph, start, goal, limit)

if found:
    print(f"\nGoal '{goal}' found within depth limit {limit}.")
else:
    print(f"\nGoal '{goal}' NOT found within depth limit {limit}.")

