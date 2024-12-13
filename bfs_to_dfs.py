from collections import deque

def dfs(grid, start, goal):
    def neighbors(node):
        x, y = node
        # All possible operators
        candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]  # Horizontal and vertical
        return [(nx, ny) for nx, ny in candidates if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0]

 
    stack = [start]  # Stack to explore nodes
    came_from = {}
    visited = set()
    visited.add(start)

    while stack:
        current_node = stack.pop()  

        if current_node == goal:
            return reconstruct_path(came_from, start, goal)

        for next_node in neighbors(current_node):
            if next_node not in visited:
                visited.add(next_node)
                stack.append(next_node) 
                came_from[next_node] = current_node

    return None

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path[::-1]
