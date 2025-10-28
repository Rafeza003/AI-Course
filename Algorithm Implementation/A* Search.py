
def a_star_search(graph, start, goal, h):
    open_queue = [(start, 0)]  # (node, g)
    closed_queue = []
    parents = {start: None}
    g_values = {start: 0}

    while open_queue:
        # ---- Find node with lowest f = g + h ----
        lowest_index = 0
        lowest_f = open_queue[0][1] + h[open_queue[0][0]]
        for i in range(1, len(open_queue)):
            node_i, g_i = open_queue[i]
            f_i = g_i + h[node_i]
            if f_i < lowest_f:
                lowest_f = f_i
                lowest_index = i

        node, g = open_queue.pop(lowest_index)
        closed_queue.append(node)

        # ---- Goal check ----
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parents[node]
            path.reverse()
            print("\n✅ Goal found!")
            print("Path:", " -> ".join(path))
            print("Total cost (g):", g_values[goal])
            return

        # ---- Explore neighbors ----
        for neighbor, cost in graph[node].items():
            temp_g = g + cost
            if neighbor in closed_queue:
                continue

            # if neighbor not visited yet OR found a cheaper path
            if (neighbor not in [n for n, _ in open_queue]) or (temp_g < g_values.get(neighbor, float('inf'))):
                parents[neighbor] = node
                g_values[neighbor] = temp_g
                open_queue.append((neighbor, temp_g))

    print("\n❌ Goal not found!")


def main():
    n = int(input("Number of nodes: "))
    graph = {}
    h = {}

    for _ in range(n):
        node = input("Node name: ")
        neighbors_input = input(f"Neighbors of {node} with cost (format: B-2 C-5): ").split()
        graph[node] = {}
        for nb in neighbors_input:
            if nb:
                name, cost = nb.split('-')
                graph[node][name] = int(cost)
        h[node] = int(input(f"Heuristic value of {node}: "))

    start = input("Start node: ")
    goal = input("Goal node: ")

    a_star_search(graph, start, goal, h)


if __name__ == "__main__":
    main()

