from collections import deque

# Function to read the maze from a file and convert it to a list
def read_maze(filename):
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            row = [int(cell) for cell in line.strip()]  # Convert each character to an integer
            maze.append(row)
    return maze

# Breadth-First Search algorithm to find a path in the maze
def bfs(maze, start, goal):
    queue = deque([start])  # Initialize a queue with the starting position
    visited = set([start])  # Create a set to keep track of visited positions
    parent = {}  # Dictionary to store parent-child relationships for path reconstruction
    expansions = 0  # Counter to keep track of the number of expansions

    while queue:
        current_position = queue.popleft()  # Dequeue the current position

        if current_position == goal:  # If the goal is reached, return the path
            return True, parent, expansions

        row, col = current_position
        # Define the neighboring positions (up, down, left, right)
        neighbors = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]

        for neighbor in neighbors:
            row, col = neighbor

            # Check if the neighbor is within the maze boundaries not a wall (maze[row][col] == 0) and has not been visited yet
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0 and neighbor not in visited:
                queue.append(neighbor)  # Enqueue the neighbor
                visited.add(neighbor)  # Mark the neighbor as visited
                parent[neighbor] = current_position  # Set the parent of the neighbor
                expansions += 1  # Increment the expansions counter

    return False, parent, expansions  # If no path is found, return False

# Depth-First Search algorithm to find a path in the maze
def dfs(maze, start, goal):
    stack = [start]  # Initialize a stack with the starting position
    visited = set([start])  # Create a set to keep track of visited positions
    parent = {}  # Dictionary to store parent-child relationships for path reconstruction
    expansions = 0  # Counter to keep track of the number of expansions

    while stack:
        current_position = stack.pop()  # Pop the current position from the stack

        if current_position == goal:  # If the goal is reached, return the path
            return True, parent, expansions

        row, col = current_position
        # Define the neighboring positions (up, down, left, right)
        neighbors = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]

        for neighbor in neighbors:
            row, col = neighbor

            # Check if the neighbor is within the maze boundaries not a wall (maze[row][col] == 0) and has not been visited yet
            if 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0 and neighbor not in visited:
                stack.append(neighbor)  # Push the neighbor onto the stack
                visited.add(neighbor)  # Mark the neighbor as visited
                parent[neighbor] = current_position  # Set the parent of the neighbor
                expansions += 1  # Increment the expansions counter

    return False, parent, expansions  # If no path is found, return False

# Start of the main program

# Reading the maze from a file
maze = read_maze('maze.txt')

# Define the start and end points (these coordinates depend on the specific maze)
start = (17, 1)
goal = (1, 17)

# Call the BFS and DFS methods to find paths
bfs_path_found, bfs_parent, bfs_expansions = bfs(maze, start, goal)
dfs_path_found, dfs_parent, dfs_expansions = dfs(maze, start, goal)

# If a path is found by BFS, mark the path with '2' in the maze
if bfs_path_found:
    current_position = goal
    while current_position != start:
        maze[current_position[0]][current_position[1]] = 2
        current_position = bfs_parent[current_position]

# Print the maze with the marked path for both BFS and DFS
print("This is BFS")
for row in maze:
    print(' '.join(str(cell) for cell in row))
print("Expansions for BFS:", bfs_expansions)

# If a path is found by DFS, mark the path with '3' in the maze
if dfs_path_found:
    current_position = goal
    while current_position != start:
        maze[current_position[0]][current_position[1]] = 3
        current_position = dfs_parent[current_position]

print("\nThis is DFS")
for row in maze:
    print(' '.join(str(cell) for cell in row))
print("Expansions for DFS:", dfs_expansions)
