def alpha_beta_prune(depth, node_index, is_max_turn, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_max_turn:
        best = float('-inf')
        for i in range(2):
            val = alpha_beta_prune(depth + 1, node_index * 2 + i, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alpha_beta_prune(depth + 1, node_index * 2 + i, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best


import math


max_depth = int(input("Enter tree depth (number of levels from root to leaf, e.g., 3 for 8 leaves): "))

num_leaves = 2 ** max_depth

print(f"Enter values for the {num_leaves} leaf nodes (space separated):")
user_input = input()
values = list(map(int, user_input.strip().split()))

if len(values) != num_leaves:
    print(f" You must enter exactly {num_leaves} values.")
else:
    result = alpha_beta_prune(0, 0, True, values, float('-inf'), float('inf'), max_depth)
    print(f"\nBest value determined by Alpha-Beta Pruning: {result}")
