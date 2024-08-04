import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue for the open set
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start), start))
    
    # Dictionaries to keep track of costs and paths
    g_costs = {start: 0}
    came_from = {}
    
    while open_set:
        # Get the node with the lowest f value
        current_cost, current_node = heapq.heappop(open_set)
        
        # Check if the goal has been reached
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            tentative_g_cost = g_costs[current_node] + weight
            
            # If this path is better or neighbor has not been visited
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor)
                heapq.heappush(open_set, (f_cost, neighbor))
                came_from[neighbor] = current_node
    
    return None  # No path found

# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list with weights
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    
    # Define a heuristic function (e.g., Manhattan distance)
    def heuristic(node):
        heuristics = {
            'A': 7,
            'B': 6,
            'C': 2,
            'D': 0
        }
        return heuristics.get(node, float('inf'))
    
    # Run A* algorithm
    start_node = 'A'
    goal_node = 'D'
    path = a_star(graph, start_node, goal_node, heuristic)
    
    # Print results
    if path:
        print("Path found:", " -> ".join(path))
    else:
        print("No path found")
