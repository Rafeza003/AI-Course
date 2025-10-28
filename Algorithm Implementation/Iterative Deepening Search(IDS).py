
# Iterative Deepening Search (IDS)

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


def iterative_deepening_search(graph, start, goal, max_limit):
    for limit in range(max_limit + 1):
        print(f"\nDepth Limit = {limit}: ", end="")
        found = dls(graph, start, goal, limit)
        if found:
            print(f"\nGoal '{goal}' found at depth limit {limit}.")
            return True
    print(f"\nGoal '{goal}' NOT found within max depth limit {max_limit}.")
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
max_limit = int(input("Maximum depth limit: "))

print("\nIterative Deepening Search Traversal:")
iterative_deepening_search(graph, start, goal, max_limit)

