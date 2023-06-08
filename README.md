# Maze Solver

## Description
The Maze Solver is a Python program that solves a maze represented by a matrix. It uses breadth-first search (BFS) and depth-first search (DFS) algorithms to find the number of possible paths and the optimal path from the start point to the end point of the maze.

## Maze Solving Algorithm
The program uses two algorithms for maze solving:

1. Breadth-First Search (BFS): It starts from the top-left corner of the maze and explores all possible paths until it reaches the bottom-right corner. It counts the number of possible paths from the start to the end.

2. Depth-First Search (DFS): It starts from the top-left corner and explores each path until it reaches a dead end or the bottom-right corner. It backtracks whenever it reaches a dead end and continues exploring other paths. It finds the optimal path from the start to the end.

## Usage
To use the Maze Solver, follow these steps:

1. Define the maze matrix: Modify the `matrix` variable in the code to represent your maze. Use 1 to represent open paths and 0 to represent walls.
2. Run the program: Execute the code to run the Maze Solver.
3. Results:
   - The program will output the number of possible paths found using the BFS algorithm.
   - It will also output the optimal path found using the DFS algorithm.

## Example
Here's an example maze matrix:

```python
matrix = [
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 1, 1]
]

# BFS Maze Solver
print("Number of possible paths (BFS):", Maze(matrix))

# DFS Maze Solver
path = Mazedfs(matrix)
print("Optimal path (DFS):", path)
Make sure to modify the matrix variable to match your desired maze configuration.

## Contributing
Contributions to the Library Management System project are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.
