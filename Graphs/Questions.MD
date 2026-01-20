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

## Course Schedule II (Medium)

You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.
Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

## Number of Connected Components in an Undirected Graph (Medium)

There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.
The nodes are numbered from 0 to n - 1.
Return the total number of connected components in that graph.

## Graph Valid Trees (Medium)

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

## Redundant Connection (Medium)

You are given a connected undirected graph with n nodes labeled from 1 to n. Initially, it contained no cycles and consisted of n-1 edges.
We have now added one additional edge to the graph. The edge has two different vertices chosen from 1 to n, and was not an edge that previously existed in the graph.
The graph is represented as an array edges of length n where edges[i] = [ai, bi] represents an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the graph is still a connected non-cyclical graph. If there are multiple answers, return the edge that appears last in the input edges.

## Network Delay Time (Medium)

You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).
ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.
Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.

## Min Cost to Connect Points (Medium)

You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.
Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

## Word Ladder (Hard)

You are given two words, beginWord and endWord, and also a list of words wordList. All of the given words are of the same length, consisting of lowercase English letters, and are all distinct.
Your goal is to transform beginWord into endWord by following the rules:
You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character, and the rest of the positions have the same characters.
You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.
Return the minimum number of words within the transformation sequence needed to obtain the endWord, or 0 if no such sequence exists.