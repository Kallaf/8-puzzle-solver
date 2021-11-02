# EightPuzzleSolver
<p align='center'><img src='https://github.com/Kallaf/8-puzzle-solver/blob/master/screenshots/demo.gif'/></p>

## About 8-Puzzle Game
An instance of the 8-puzzle game consists of a board holding 8 distinct movable
tiles, plusan empty space. For any such board, the empty space may be legally
swapped with any tile horizontally or vertically adjacent to it. In this assignment,
the blank space is going to be represented by the number 0. Given an initial state
of the board, the search problem is to find a sequence of moves that tran-sitions
this state to the goal state; that is, the configuration with all tiles arranged in
ascending order 0,1,2,3,4,5,6,7,8 .

## Supported Algorithms:
- **Breadth First Search (BFS)**: It is a traversing algorithm where you should start traversing from a selected node (source or starting node) and traverse the graph layerwise thus exploring the neighbour nodes (nodes which are directly connected to source node).

- **Depth First Search (DFS)**:  It is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph) and explores as far as possible along each branch before backtracking.

- **A Star Search (A\*)**: It is a graph traversal and path search algorithm, which is often used in computer science due to its completeness, optimality, and optimal efficiency. One major practical drawback is its. space complexity, as it stores all generated nodes in memory (Tried out both **Eculidean** and **Manhattan** distance metrics for heuristics).
