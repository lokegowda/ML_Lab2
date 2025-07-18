from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    open_list = PriorityQueue()
    open_list.put((0 + heuristic[start], 0, start, [start]))
    visited = set()

    while not open_list.empty():
        f, g, current, path = open_list.get()

        if current == goal:
            return g, path

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:
                total_cost = g + cost
                estimated_cost = total_cost + heuristic.get(neighbor, float('inf'))
                open_list.put((estimated_cost, total_cost, neighbor, path + [neighbor]))

    return None, []

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 2), ('D', 5)],
    'B': [('D', 1)],
    'C': [('G', 5)],
    'D': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 4,
    'D': 2,
    'G': 0
}

start_node = 'S'
goal_node = 'G'

cost, path = a_star_search(graph, start_node, goal_node, heuristic)

if path:
    print(f" Path found: {' -> '.join(path)} with cost {cost}")
else:
    print(" No path found.")
