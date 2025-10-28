def beam_search(graph, start, goal, h, beam_width):
    visited = []
    frontier = [start]

    while frontier:
    
        def heuristic_value(node):                
            return h[node]

    
        frontier.sort(key=heuristic_value )


        frontier = frontier[:beam_width]

        current = frontier.pop(0)
        print("Visiting:", current)

        if current == goal:
            print("Goal reached:", goal)
            return

        if current not in visited:
            visited.append(current)
            for neighbor in graph[current]:
                if neighbor not in visited and neighbor not in frontier:
                    frontier.append(neighbor)

    print("Goal not found!")


def main():
    n = int(input("Number of nodes: "))
    graph = {}
    h = {}

    for _ in range(n):
        node = input("Node name: ")
        neighbors = input(f"Neighbors of {node} (space separated): ").split()
        graph[node] = neighbors
        h[node] = int(input(f"Heuristic value of {node}: "))

    start = input("Start node: ")
    goal = input("Goal node: ")
    beam_width = int(input("Enter beam width: "))

    beam_search(graph, start, goal, h, beam_width)
if __name__ =="__main__":
    main()





