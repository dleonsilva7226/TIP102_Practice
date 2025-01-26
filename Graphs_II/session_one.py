from collections import deque
# Standard Problem Set 1

# Problem 1: Seeking Safety
# def next_moves(position, grid):
#     neighbors = [(-1, 0), (0, -1), (1, 0), (0, 1)]
#     safe_spaces = []
#     height = len(grid)
#     width = len(grid[0])
#     for i, j in neighbors:
#         y = position[0] + i
#         x = position[1] + j
#         if 0 <= y < height and 0 <= x < width and grid[y][x] == 1:
#             safe_spaces.append((y,x))
        
#     return safe_spaces



# grid = [
#     [0, 0, 0, 1, 1], # Row 0
#     [0, 0, 0, 1, 1], # Row 1
#     [1, 1, 1, 0, 0], # Row 2
#     [1, 1, 1, 1, 0], # Row 3
#     [0, 0, 0, 1, 0]  # Row 4
# ]

# position_1 = (3, 2)
# position_2 = (0, 4)
# position_3 = (0, 1)

# print(next_moves(position_1, grid))
# print(next_moves(position_2, grid))
# print(next_moves(position_3, grid))







# Problem 2: Escape to the Safe Haven

# Matrices Algorithms
# BFS Code:
# - Start from a cell, add it to a queue, and mark it as visited.
# - While the queue isn't empty, take the cell at the front of the queue, and check its neighboring cells 
#   (up, down, left, right).
# - For each neighbor, if it hasn't been visited, add it to the queue and mark it as visited.
# - Repeat this process until all reachable cells are visited.



# Pseudocode for DFS on a Matrix:

# - Start from a cell, mark it as visited.
# - Recursively move to one of its neighboring cells (up, down, left, right) if it hasn't been visited.
# - If no unvisited neighbors remain, backtrack to the previous cell and explore the next possible direction.
# - Repeat this process until all reachable cells are visited.


# def can_move_safely(position, grid):
#     visited = set()
#     queue = deque()
#     height = len(grid)
#     width = len(grid[0])
#     visited.add(position)
#     queue.append(position)
#     neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     while queue:
#         popped = queue.popleft()
#         for i, j in neighbors:
#             y = popped[0] + i
#             x = popped[1] + j
#             if (y, x) == (height - 1, width - 1):
#                 return True
#             if 0 <= y < height and 0 <= x < width and (y,x) not in visited and grid[y][x] == 1: 
#                 visited.add((y,x))
#                 queue.append((y,x))

#     return False

# grid = [
#     [1, 0, 1, 1, 0], # Row 0
#     [1, 1, 1, 1, 0], # Row 1
#     [0, 0, 1, 1, 0], # Row 2
#     [1, 0, 1, 1, 1]  # Row 3
# ]

# position_1 = (0, 0) # true
# position_2 = (0, 4) # true
# position_3 = (3, 0) # false

# print(can_move_safely(position_1, grid))
# print(can_move_safely(position_2, grid))
# print(can_move_safely(position_3, grid))







# Problem 3: List All Escape Routes 

# def list_all_escape_routes(grid):
#     height = len(grid)
#     width = len(grid[0])
#     valid_routes = []
#     for i in range(height):
#         for j in range(width):
#             if grid[i][j] == 1 and can_move_safely((i,j), grid):
#                 valid_routes.append((i,j))
#     return valid_routes

# grid = [
#     [1, 0, 1, 0, 1], # Row 0
#     [1, 1, 1, 1, 0], # Row 1
#     [0, 0, 1, 0, 0], # Row 2
#     [1, 0, 1, 1, 1]  # Row 3
# ]

# print(list_all_escape_routes(grid))




# Problem 4: Largest Safe Zone

# def largest_safe_zone(grid):
#     max_connected_size = -1
#     queue = deque()
#     visited = set()
#     neighbors = [(1, 0), (-1, 0), (0, -1), (0, 1)]
#     height = len(grid)
#     width = len(grid[0])
#     for i in range(height):
#         for j in range(width):
#             if (i, j) not in visited and grid[i][j] == 1:
#                 visited.add((i, j))
#                 queue.append((i, j))
#                 curr_component_size = 1
#                 while queue:
#                     y, x = queue.popleft()
#                     for a, b in neighbors:
#                         curr_y = y + a
#                         curr_x = x + b
#                         if 0 <= curr_y < height and 0 <= curr_x < width and (curr_y, curr_x) not in visited and grid[curr_y][curr_x] == 1:
#                             visited.add((curr_y, curr_x))
#                             queue.append((curr_y, curr_x))
#                             curr_component_size += 1
#                 if max_connected_size < curr_component_size:
#                     max_connected_size = curr_component_size

#     return max_connected_size


# grid = [
#     [0, 0, 0, 1, 1], # Row 0
#     [0, 0, 0, 1, 1], # Row 1
#     [1, 1, 1, 0, 0], # Row 2
#     [1, 1, 1, 1, 0], # Row 3
#     [0, 0, 0, 1, 0]  # Row 4
# ]

# print(largest_safe_zone(grid))


# Problem 5: Zombie Spread

# def time_to_infect(grid):
#     height = len(grid)
#     width = len(grid[0])
#     neighbors = [(1,0),(0,1),(-1,0),(0,-1)]
#     queue = deque()
#     visited = set()
#     total_people = 0
#     minute = 0
#     for i in range(height):
#         for j in range(width):
#             if grid[i][j] == 1 or grid[i][j] == 2:
#                 total_people += 1
#             if (i, j) not in visited and grid[i][j] == 2:
#                 visited.add((i,j))
#                 queue.append((i, j, 0))
#                 while queue:
#                     popped = queue.popleft()
#                     minute = popped[2]
#                     for i, j in neighbors:
#                         y = popped[0] + i
#                         x = popped[1] + j
#                         if 0 <= y < height and 0 <= x < width:
#                             if (y, x) not in visited and grid[y][x] == 1:
#                                 grid[y][x] = 2
#                                 visited.add((y,x))
#                                 queue.append((y,x, minute + 1))
#     if len(visited) == total_people:
#         return minute
#     return -1

# grid_1 = [
#         [2,1,1],
#         [1,1,0],
#         [0,1,1]]

# grid_2 = [
#         [2,1,1],
#         [0,1,1],
#         [1,0,1]]

# grid_3 = [[0,2]]

# print(time_to_infect(grid_1))
# print(time_to_infect(grid_2))
# print(time_to_infect(grid_3))

