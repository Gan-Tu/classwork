# Introduction
These are general graph traversal algorithms implementation.

The algorithm traverses from the bottom left corner to upper right corner.

# Disclaimer
I did not implement some of the utility tools in this files, and they are developed by other developers.

I developed mainly the traversal algorithms and cycle detection.

# Set Up
To compile all java files, type in the terminal:
```
make
```

To manually configure the maze, apply changes to the file 'maze.config'.

* **N**: sets the size of the maze (N by N)
* **rseed**: the random seed to use for the maze setup
* **MazeType**: there are three types of maze type provided
    * **SINGLE_GAP**: does not allow multiple gaps to create open space and cycles
    * **POPEN_SOLVABLE**: allow multiple gaps to create open space and cycles
    * **BLANK**: a blank maze
    * You can ONLY use ONE maze type at a time. To select one, delete the '%' sign in front of the maze type line, and add '%' to comment out other types.
* **pOpen**: the probability (e.g. 0.35) that each 1x1 node position has an open side. The lower the rate, the more likely there will be a dead end closed cycle/path.
* **DRAW_DELAY_MS**: the delay of time when drawing each node traversed. The higher the number, the slower the GUI displays the traversal.

# Demo
For a demo of A Star Search, type in the terminal:
```
make astar
```

For a demo of Breadth First Search (BFS), type in the terminal:
```
make bfs
```

For a demo of Depth First Search (DFS), type in the terminal:
```
make dfs
```

For a demo of Trivial Graph Search, type in the terminal:
```
make trivial
```

For a demo of cycle detection, type in the terminal:
```
make cycle
```

# Cleanup
To remove all .class files quickly, type in the terminal:
```
make clean
```

# Version
You need java 1.8 or above.
