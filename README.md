# Flight Route Planning System

Graph-based flight route optimizer using BFS and Dijkstra's algorithm.

## Features

- **Minimum Stops** - BFS algorithm, O(V+E) complexity
- **Cheapest Fare** - Dijkstra's algorithm, O(E log V) complexity  
- **Fastest Route** - Dijkstra's algorithm, O(E log V) complexity
- Stop limits and fare filters
- Indian city flight network with real airlines

## Algorithms

| Strategy | Algorithm | Time Complexity | Space Complexity |
|----------|-----------|-----------------|------------------|
| Min Stops | BFS | O(V + E) | O(V) |
| Cheapest | Dijkstra | O(E log V) | O(V) |
| Fastest | Dijkstra | O(E log V) | O(V) |
