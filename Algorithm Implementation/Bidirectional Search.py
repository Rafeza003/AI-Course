from collections import deque

# -------- Bidirectional Search Function --------
def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    # Queues for both directions
    forward_queue = deque([start])
    backward_queue = deque([goal])

    # Visited dictionaries to track paths
    forward_visited = {start: None}
    backward_visited = {goal: None}

    while forward_queue and backward_queue:
        # ---- Forward Search ----
        current_f = forward_queue.popleft()
        for neighbor in graph.get(current_f, []):
            if neighbor not in forward_visited:
                forward_visited[neighbor] = current_f
                forward_queue.append(neighbor)

                if neighbor in backward_visited:  # Meeting point found
                    return build_path(forward_visited, backward_visited, neighbor)

        # ---- Backward Search ----
        current_b = backward_queue.popleft()
        for neighbor in graph.get(current_b, []):
            if neighbor not in backward_visited:
                backward_visited[neighbor] = current_b
                backward_queue.append(neighbor)

                if neighbor in forward_visited:  # Meeting point found
                    return build_path(forward_visited, backward_visited, neighbor)

    return None


# -------- Path Construction Function --------
def build_path(forward_visited, backward_visited, meeting_point):
    # Path from start to meeting point
    path1 = []
    node = meeting_point
    while node is not None:
        path1.append(node)
        node = forward_visited[node]
    path1.reverse()

    # Path from meeting point to goal
    path2 = []
    node = backward_visited.get(meeting_point)
    while node is not None:
        path2.append(node)
        node = backward_visited.get(node)

    # Combine and return
    return path1 + path2


# -------- Main Program (User Input) --------
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node name: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter Start Node: ")
goal = input("Enter Goal Node: ")

path = bidirectional_search(graph, start, goal)

if path:
    print("\nShortest Path:", " -> ".join(path))
else:
    print("\nNo path found!")

