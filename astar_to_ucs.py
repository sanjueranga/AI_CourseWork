import heapq
import math

def ucs(grid, start, goal):

    def neighbors(node):
        x, y = node
        candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1),
                      (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]
        result = []
        for nx, ny in candidates:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                if (dx := abs(nx - x)) == 1 and (dy := abs(ny - y)) == 1:
                    if grid[x][ny] == 0 and grid[nx][y] == 0:  # Check both diagonal neighbors
                        result.append((nx, ny))
                else:
                    result.append((nx, ny))
        return result


    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    cost_so_far = {start: 0}

    while open_set:
        current_cost, current_node = heapq.heappop(open_set)

        if current_node == goal:
            path = reconstruct_path(came_from, start, goal)
            return path

        for next_node in neighbors(current_node):
            dx = abs(next_node[0] - current_node[0])
            dy = abs(next_node[1] - current_node[1])
            step_cost = 3 if dx == 1 and dy == 1 else 1  
            new_cost = cost_so_far[current_node] + step_cost
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost 
                heapq.heappush(open_set, (priority, next_node))
                came_from[next_node] = current_node

    return None

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path[::-1]
