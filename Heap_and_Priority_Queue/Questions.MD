# Descriptions and any additional notes for every questions written below

## Kth Largest Element In A Stream (Easy)

Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
Implement the following methods:
constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

Idea: The idea here is to create a minheap out of the numbers array in the constructor, and while in the constructor, remove the smallest elements until there are k elements left. The reason we do this is because we want to keep k elements in the minheap so that finding the kth largest element is just finding the smallest element in the heap. In the add function, we add the value to the heap, and if the length of the heap is larger than k, we remove the smallest element, and then at the end we return the smallest element in the heap. This runs in O(mlogk) runtime complexity, where m is the number of times add is called, and O(k) space.