def minimax(depth, node_index, is_max, values):
    
    if depth == 3:
        return values[node_index]
    
    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, values),
            minimax(depth + 1, node_index * 2 + 1, False, values)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values),
            minimax(depth + 1, node_index * 2 + 1, True, values)
        )


user_input = input("Enter 8 space-separated leaf values: ")
values = list(map(int, user_input.strip().split()))


if len(values) != 8:
    print(" Please enter exactly 8 values.")
else:
    optimal_value = minimax(0, 0, True, values)
    print(f" The optimal value is: {optimal_value}")