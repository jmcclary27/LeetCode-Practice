# Descriptions and any additional notes for every questions written below

## Number of Islands (Medium)

Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.
An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

Idea: The idea is to create a nested iterative BFS algorithm that seraches for all connecting piece of a single island, and changes their values to 0 so that these pieces aren't accidentally found again. We then loop through each square, and whenever we come across a value of "1", we apply the BFS function and increment a counter keeping track of the number of islands. This runs in O(m * n) for time and space complexity.

## Max Area of Islands (Medium)

You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).
An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.
The area of an island is defined as the number of cells within the island.
Return the maximum area of an island in grid. If no island exists, return 0.

Idea: The idea is similar to last problem, with the only difference being our BFS algorithm tracks how many squares are in the island, and outside the BFS we have a variable updating to be the largest number of islands. This code runs in O(m * n) for time and space complexity.

## Clone Graph (Medium)

Given a node in a connected undirected graph, return a deep copy of the graph.
Each node in the graph contains an integer value and a list of its neighbors.
class Node {
    public int val;
    public List<Node> neighbors;
}
The graph is shown in the test cases as an adjacency list. An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list is the same as the node's value (1-indexed).
The input node will always be the first node in the graph and have 1 as the value.

Idea: The idea is to use a hash map that maps the nodes of the old graph to the new graph. We fill this map by creating a nested recursive DFS function that gets applied to all the neighbors of the current node. This code runs in O(V + E) time complexity and O(V) space complexity.

## Surrounded Regions (Medium)

You are given a 2-D matrix board containing 'X' and 'O' characters.
If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.
Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

## Course Schedule (Medium)

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
The pair [0, 1], indicates that must take course 1 before taking course 0.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return true if it is possible to finish all courses, otherwise return false.