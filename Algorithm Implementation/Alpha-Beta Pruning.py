import math

# Minimax with Alpha-Beta Pruning
def alphabeta(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or type(node) == int:  # Leaf node
        return node

    if maximizingPlayer:
        maxEval = -math.inf
        for child in node:
            eval = alphabeta(child, depth-1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cutoff
        return maxEval
    else:
        minEval = math.inf
        for child in node:
            eval = alphabeta(child, depth-1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return minEval

# Helper to take user input for the tree
def build_tree():
    n = int(input("Enter number of children for this node (0 if leaf): "))
    if n == 0:
        value = int(input("Enter leaf node value: "))
        return value
    children = []
    for i in range(n):
        print(f"Building child {i+1} of this node:")
        children.append(build_tree())
    return children

# Main
print("Build your game tree:")
tree = build_tree()
result = alphabeta(tree, depth=10, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)
print("Optimal value for maximizer:", result)

